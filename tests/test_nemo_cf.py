#!/usr/bin/env python

"""Tests for the `nemo_cf.cli` package."""

from nemo_cf.nemo_cf import update_all_vars_attrs, safely_drop_labels

import xarray as xr


def test_update_all_vars_attrs_works():

    dataset = xr.DataArray([], name="var_01").to_dataset()
    new_attrs = {
        "var_01": {
            {"units": "meters", "coordinates": ""}
        }
    }

    dataset = update_all_vars_attrs(dataset, attrs=new_attrs)

    assert dataset["var_01"].attrs["units"] == "meters"
    assert dataset["var_01"].attrs["coordinates"] == ""


def test_safe_label_dropper():
    dataset = xr.DataArray([], name="var_01").to_dataset()

    assert "var_01" in safely_drop_labels(dataset, ["var_02", "var_03"])

    assert "var_01" not in safely_drop_labels(dataset, ["var_01", "var_02"])
