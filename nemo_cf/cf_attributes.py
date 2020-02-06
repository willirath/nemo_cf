"""Attributes used in the annotation."""

mesh_mask_attrs = {}

# longitude fields
mesh_mask_attrs.update(
    {
        f"glam{grid}": {
            "long_name": "longitude",
            "units": "degrees_east",
            "standard_name": "longitude"
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# latitude fields
mesh_mask_attrs.update(
    {
        f"gphi{grid}": {
            "long_name": "latitude",
            "units": "degrees_north",
            "standard_name": "latitude"
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# depth fields
mesh_mask_attrs.update(
    {
        f"gdep{grid}_1d": {
            "long_name": "depth",
            "units": "meters",
            "positive": "down",
            "standard_name": "depth"
        }
        for grid in ["t", "w"]
    }
)

# zonal grid constants
mesh_mask_attrs.update(
    {
        f"e1{grid}": {
            "long_name": "zonal grid constant",
            "units": "meters",
            "coordinates": f"glam{grid} gphi{grid}"
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# meridional grid constants
mesh_mask_attrs.update(
    {
        f"e2{grid}": {
            "long_name": "meridional grid constant",
            "units": "meters",
            "coordinates": f"glam{grid} gphi{grid}"
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# vertical grid constants
mesh_mask_attrs.update(
    {
        f"e3{grid}_1d": {
            "long_name": "vertical grid constant",
            "units": "meters",
            "coordinates": f"gdep{grid}_1d"
        }
        for grid in ["t", "w"]
    }
)

# masks
# Note that the f-mask lives on vertical T levels
# (c/f NEMO book)
mesh_mask_attrs.update(
    {
        f"{grid}mask": {
            "long_name": "land point mask",
            "units": "boolean",
            "coordinates": f"gdept_1d glam{grid} gphi{grid}"
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# util masks
mesh_mask_attrs.update(
    {
        f"{grid}maskutil": {
            "long_name": "land point mask",
            "units": "boolean",
            "coordinates": f"glam{grid} gphi{grid}"
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# number of wet grid points
mesh_mask_attrs.update({
    "mbathy": {
        "long_name": "number of ocean levels at xy grid point",
        "coordinates": "glamt gphit"
    }
})
