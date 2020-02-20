# NEMO CF

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/willirath/nemo_cf/master)
[![PyPi status](https://img.shields.io/pypi/v/nemo_cf.svg)](https://pypi.python.org/pypi/nemo_cf)
[![Travis Status](https://img.shields.io/travis/willirath/nemo_cf.svg)](https://travis-ci.com/willirath/nemo_cf)
[![Docs status](https://readthedocs.org/projects/nemo-cf/badge/?version=latest)](https://nemo-cf.readthedocs.io/en/latest/?badge=latest)

Make NEMO output CF compliant

## Purpose of this tool

Starting from standard NEMO / XIOS2 output, we aim at creating datasets that have the following properties:

1. no un-ambiguous names and labels,
2. every variable contains information about the attached coordinates,
3. every variable has a unit, a long name, if possible a standard name.

Note that 1. implies that coordinate names like `nav_lon` and `nav_lat` should be replaced by the respective `glam?` and `gphi` fields.

## Materials

- [NEMO book (pdf)](https://www.nemo-ocean.eu/wp-content/uploads/NEMO_book.pdf)
- [CF conventions (v1.7)](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html)


## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage) project template.
