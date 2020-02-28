"""Main module."""

from .cf_attributes import mesh_mask_attrs


def update_all_vars_attrs(dataset, attrs=None):
    """Update attributes of all vars."""
    for varname, new_attrs in attrs.items():
        dataset[varname].attrs.update(new_attrs)
    return dataset


def safely_drop_vars(dataset, vars=None):
    """Drop labels dataset if they are present."""
    valid_vars = filter(lambda var: var in dataset, vars)
    return dataset.drop_vars(valid_vars)


def update_mesh_mask_attrs(dataset, attrs=mesh_mask_attrs):
    """Update a mesh_mask dataset to have CF compliant metadata."""
    return update_all_vars_attrs(dataset, attrs=attrs)


def update_mesh_mask_dataset(
    dataset,
    attrs=mesh_mask_attrs,
    drop_vars=("nav_lev", "nav_lat", "nav_lon"),
    squeeze_singleton=True,
):
    """Add attributes and drop un-wanted variables."""
    dataset = update_mesh_mask_attrs(dataset, attrs=attrs)
    dataset = safely_drop_vars(dataset, vars=drop_vars)
    if squeeze_singleton:
        dataset = dataset.squeeze()
    return dataset


def safely_rename_dims(dataset, rename_dims_dict=None):
    valid_rename_dims_dict = {
        dim: rename_dims_dict[dim]
        for dim in filter(lambda dim: dim in dataset.dims, rename_dims_dict)
    }

    return dataset.rename_dims(valid_rename_dims_dict)


def safely_rename_vars(dataset, rename_vars_dict=None):
    valid_rename_vars_dict = {
        var: rename_vars_dict[var]
        for var in filter(lambda var: var in dataset.data_vars, rename_vars_dict)
    }

    return dataset.rename_vars(valid_rename_vars_dict)


def update_data_file_coords(dataset, grid=None):
    """Ensure spatial coords are consistent."""

    rename_dims_dict = {f"depth{grid.lower()}": "z"}
    dataset = safely_rename_dims(dataset, rename_dims_dict=rename_dims_dict)

    rename_vars_dict = {
        f"depth{grid.lower()}": f"gdep{grid.lower()}_1d",
        "nav_lat": f"gphi{grid.lower()}",
        "nav_lon": f"glam{grid.lower()}",
    }
    dataset = safely_rename_vars(dataset, rename_vars_dict=rename_vars_dict)

    for v in dataset.data_vars:
        if "coordinates" in dataset[v].attrs:
            for old, new in rename_vars_dict.items():
                dataset[v].attrs["coordinates"] = (
                    dataset[v].attrs["coordinates"].replace(old, new)
                )

    return dataset
