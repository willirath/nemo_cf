#!/usr/bin/env python

"""Tests for the `nemo_cf.cli` package."""

import pytest

from nemo_cf.nemo_cf import (
    update_all_vars_attrs,
    safely_drop_vars,
    update_mesh_mask_dataset,
)
from nemo_cf.aux import download_and_extract_zip_file

from pathlib import Path
import xarray as xr


@pytest.fixture(scope="session")
def test_data_dir(tmpdir_factory):
    test_data_dir = tmpdir_factory.mktemp("test_data")
    download_and_extract_zip_file(
        target_dir=test_data_dir,
        url=(
            "https://zenodo.org/record/3634491/files/"
            "NEMO_GYRE_test_data_all_files.v2020.02.03.1.zip"
        ),
        force=True,
    )
    return Path(str(test_data_dir))


def test_update_all_vars_attrs_works():

    dataset = xr.DataArray([], name="var_01").to_dataset()
    new_attrs = {"var_01": {"units": "meters", "coordinates": ""}}

    dataset = update_all_vars_attrs(dataset, attrs=new_attrs)

    assert dataset["var_01"].attrs["units"] == "meters"
    assert dataset["var_01"].attrs["coordinates"] == ""


def test_safe_var_dropper():
    dataset = xr.DataArray([], name="var_01").to_dataset()

    assert "var_01" in safely_drop_vars(dataset, ["var_02", "var_03"])

    assert "var_01" not in safely_drop_vars(dataset, ["var_01", "var_02"])


def test_mesh_mask_updating(test_data_dir):
    mesh_mask_file = test_data_dir / "mesh_mask.nc"
    mesh_mask_ds = xr.open_dataset(mesh_mask_file)
    mesh_mask_ds_updated = update_mesh_mask_dataset(mesh_mask_ds)

    assert "nav_lev" not in mesh_mask_ds_updated.data_vars
    assert "nav_lat" not in mesh_mask_ds_updated.data_vars
    assert "nav_lon" not in mesh_mask_ds_updated.data_vars
