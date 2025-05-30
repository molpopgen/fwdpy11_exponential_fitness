from collections import Counter
from dataclasses import dataclass
import math

import fwdpy11
import fwdpy11_exponential_fitness
import numpy as np


@dataclass
class ManualCalculation:

    def __call__(self, pop, _):
        some = False
        for i, d in enumerate(pop.diploids):
            c = Counter(
                pop.haploid_genomes[d.first].smutations.tolist()
                + pop.haploid_genomes[d.second].smutations.tolist()
            )
            sum = 0.0
            for mutation, genotype in c.items():
                some = True
                if genotype == 1:
                    sum += pop.mutations[mutation].s * pop.mutations[mutation].h
                elif genotype == 2:
                    sum += 2.0 * pop.mutations[mutation].s
                else:
                    raise RuntimeError("this is really really bad...")
            w = math.exp(sum)
            assert np.isclose(
                w, pop.diploid_metadata[i].w
            ), f"{pop.haploid_genomes[d.first].smutations} {pop.haploid_genomes[d.second].smutations} {c}"
        assert some is True


def test_via_simulation():
    demog = fwdpy11.ForwardDemesGraph.tubes([1000], burnin=1)

    pdict = {
        "gvalue": fwdpy11_exponential_fitness.ExponentialFitness(2.0),
        "demography": demog,
        "sregions": [fwdpy11.ExpS(0.0, 1000.0, 1.0, -1e-2, h=0.25)],
        "nregions": [],
        "recregions": [fwdpy11.PoissonInterval(0.0, 1000.0, 1e-3)],
        "rates": (0.0, 1e-2, None),
        "prune_selected": True,
        "simlen": 10,
    }
    params = fwdpy11.ModelParams(**pdict)
    pop = fwdpy11.DiploidPopulation(demog.initial_sizes, 1000.0)
    rng = fwdpy11.GSLrng(8654123)
    fwdpy11.evolvets(
        rng, pop, params, simplification_interval=100, recorder=ManualCalculation()
    )
