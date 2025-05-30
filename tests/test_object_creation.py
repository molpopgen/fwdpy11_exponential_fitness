import math

import fwdpy11_exponential_fitness


def test_object_creation():
    e = fwdpy11_exponential_fitness.ExponentialFitness(1.0)
    assert e.scaling == 1.0


def test_object_creation_bad_values():
    try:
        _ = fwdpy11_exponential_fitness.ExponentialFitness(math.nan)
    except ValueError:
        pass
