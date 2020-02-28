"""Attributes used in the annotation."""

mesh_mask_attrs = {}

# longitude fields
mesh_mask_attrs.update(
    {
        f"glam{grid}": {
            "long_name": f"longitude of {grid.upper()}-grid points",
            "units": "degrees_east",
            "standard_name": "longitude",
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# latitude fields
mesh_mask_attrs.update(
    {
        f"gphi{grid}": {
            "long_name": f"latitude of {grid.upper()}-grid points",
            "units": "degrees_north",
            "standard_name": "latitude",
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# depth fields
mesh_mask_attrs.update(
    {
        f"gdep{grid}_1d": {
            "long_name": f"depth of {grid.upper()}-grid points",
            "units": "meters",
            "positive": "down",
            "standard_name": "depth",
        }
        for grid in ["t", "w"]
    }
)

# zonal grid constants
mesh_mask_attrs.update(
    {
        f"e1{grid}": {
            "long_name": f"grid spacing on {grid.upper()}-grid in u direction",
            "units": "meters",
            "coordinates": f"glam{grid} gphi{grid}",
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# meridional grid constants
mesh_mask_attrs.update(
    {
        f"e2{grid}": {
            "long_name": f"grid spacing on {grid.upper()}-grid in v direction",
            "units": "meters",
            "coordinates": f"glam{grid} gphi{grid}",
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# vertical grid constants
mesh_mask_attrs.update(
    {
        f"e3{grid}_1d": {
            "long_name": f"grid spacing on {grid.upper()}-grid in w direction",
            "units": "meters",
            "coordinates": f"gdep{grid}_1d",
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
            "long_name": f"mask for {grid.upper()}-grid",
            "flag_meanings": "land, water",
            "flag_values": "0, 1",
            "coordinates": f"gdept_1d glam{grid} gphi{grid}",
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# util masks
mesh_mask_attrs.update(
    {
        f"{grid}maskutil": {
            "long_name": f"mask for {grid.upper()}-grid without halo",
            "flag_meanings": "land, water",
            "flag_values": "0, 1",
            "coordinates": f"glam{grid} gphi{grid}",
        }
        for grid in ["t", "u", "v", "f"]
    }
)

# coriolis paramter
mesh_mask_attrs.update(
    {
        "ff": {
            "long_name": "Coriolis parameter on F-grid",
            "units": "s-1",
            "coordinates": "glamf gphif",
        }
    }
)

# number of wet grid points
mesh_mask_attrs.update(
    {
        "mbathy": {
            "long_name": "number of ocean levels at xy grid point",
            "coordinates": "glamt gphit",
        }
    }
)
