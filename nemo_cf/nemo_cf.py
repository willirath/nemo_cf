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
