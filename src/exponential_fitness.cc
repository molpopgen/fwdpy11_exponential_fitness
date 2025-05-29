#include <cmath>
#include <pybind11/pybind11.h>

#include <fwdpp/fitness_models.hpp>
#include <fwdpy11/genetic_values/DiploidGeneticValue.hpp>

class ll_ExponentialFitness : public fwdpy11::DiploidGeneticValue
{
  private:
    double scaling;
    fwdpp::additive_diploid additive;

  public:
    ll_ExponentialFitness(double _scaling)
        : fwdpy11::DiploidGeneticValue{1, nullptr, nullptr}, scaling{_scaling},
          additive(fwdpp::trait(_scaling))
    {
    }

    double
    calculate_gvalue(const fwdpy11::DiploidGeneticValueData data) override final
    {
        auto pop = data.pop.get();
        auto label = data.offspring_metadata.get().label;
        auto a = this->additive(pop.haploid_genomes[pop.diploids[label].first],
                                pop.haploid_genomes[pop.diploids[label].second],
                                pop.mutations);
        return std::exp(a);
    }

    void
    update(const fwdpy11::DiploidPopulation &) override final
    {
    }
};

PYBIND11_MODULE(_exponential_fitness, m)
{
    pybind11::object base_class
        = pybind11::module::import("fwdpy11").attr("DiploidGeneticValue");
    pybind11::class_<ll_ExponentialFitness, fwdpy11::DiploidGeneticValue>(
        m, "ll_ExponentialFitness")
        .def(pybind11::init<double>());
}
