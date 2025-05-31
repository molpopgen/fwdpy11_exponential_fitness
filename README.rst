fwdpy11_exponential_fitness
*********************************

Installing system dependencies
++++++++++++++++++++++++++++++

See the file `.github/workflows/test_apt_install.yml` for what commands to execute on `ubuntu` Linux.
For other Linux distros, brew, etc., modify the `apt` commands appropriately.

Do not install this package from a clone of the repo as done in the above workflow file.
Rather, install it as a `git` dependency in the usual way for Python packages.
See below for an example.

Installation using `pip`
++++++++++++++++++++++++++++++

With the following content in a `requirements.txt` file:

::

    fwdpy11_exponential_fitness @ git+https://github.com/molpopgen/fwdpy11_exponential_fitness


The following commands will install the package and the correct version of `fwdpy11`:


.. code-block:: bash

   python -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt --no-binary fwdpy11

