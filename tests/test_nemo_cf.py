#!/usr/bin/env python

"""Tests for the `nemo_cf.cli` package."""

from nemo_cf.nemo_cf import update_all_vars_attrs

import xarray as xr


def test_update_all_vars_attrs_works():

    dataset = xr.DataArray([], dims=(), name="var_01").to_dataset()
    new_attrs = {
        "var_01": {
            {"units": "meters", "coordinates": ""}
        }
    }

    dataset = update_all_vars_attrs(dataset, attrs=new_attrs)

    assert dataset["var_01"].attrs["units"] == "meters"
    assert dataset["var_01"].attrs["coordinates"] == ""
