"""Main module."""

from .cf_attributes import mesh_mask_attrs


def update_all_vars_attrs(dataset, attrs=None):
    """Update attributes of all vars."""
    for varname, new_attrs in attrs.items():
        dataset[varname].attrs.update(new_attrs)
    return dataset


def update_mesh_mask_attrs(dataset, attrs=mesh_mask_attrs):
    """Update a mesh_mask dataset to have CF compliant metadata."""
    return update_all_vars_attrs(dataset, attrs=attrs)


def safely_drop_labels(dataset, labels=None):
    """Drop labels dataset if they are present."""
    valid_labels = filter(lambda label: label in dataset, labels)
    return dataset.drop_labels(valid_labels)
