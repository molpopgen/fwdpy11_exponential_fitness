import fwdpy11

from ._exponential_fitness import ll_ExponentialFitness


class ExponentialFitness(ll_ExponentialFitness):
    def __init__(self, scaling: float):
        self.scaling = scaling
        super(ExponentialFitness, self).__init__(scaling)

    def validate_timings(
        self, deme: int, demography: fwdpy11.ForwardDemesGraph
    ) -> None:
        pass
