"""Attributes used in the annotation."""

mesh_mask_attrs = {}

# longitude fields
mesh_mask_attrs.update(
    {
        f"glam{hgrid}": {
            "long_name": f"longitude of {hgrid.upper()}-grid points",
            "units": "degrees_east",
            "standard_name": "longitude",
            "nemo_cf_hgrid": hgrid,
        }
        for hgrid in ["t", "u", "v", "f"]
    }
)

# latitude fields
mesh_mask_attrs.update(
    {
        f"gphi{hgrid}": {
            "long_name": f"latitude of {hgrid.upper()}-grid points",
            "units": "degrees_north",
            "standard_name": "latitude",
            "nemo_cf_hgrid": hgrid,
        }
        for hgrid in ["t", "u", "v", "f"]
    }
)

# depth fields
mesh_mask_attrs.update(
    {
        f"gdep{vgrid}_1d": {
            "long_name": f"depth of {vgrid.upper()}-grid points",
            "units": "meters",
            "positive": "down",
            "standard_name": "depth",
            "nemo_cf_vgrid": vgrid,
        }
        for vgrid in ["t", "w"]
    }
)

# zonal grid constants
mesh_mask_attrs.update(
    {
        f"e1{hgrid}": {
            "long_name": f"grid spacing on {hgrid.upper()}-grid in u direction",
            "units": "meters",
            "coordinates": f"glam{hgrid} gphi{hgrid}",
            "nemo_cf_hgrid": hgrid,
        }
        for hgrid in ["t", "u", "v", "f"]
    }
)

# meridional grid constants
mesh_mask_attrs.update(
    {
        f"e2{hgrid}": {
            "long_name": f"grid spacing on {hgrid.upper()}-grid in v direction",
            "units": "meters",
            "coordinates": f"glam{hgrid} gphi{hgrid}",
            "nemo_cf_hgrid": hgrid,
        }
        for hgrid in ["t", "u", "v", "f"]
    }
)

# vertical grid constants
mesh_mask_attrs.update(
    {
        f"e3{vgrid}_1d": {
            "long_name": f"grid spacing on {vgrid.upper()}-grid in w direction",
            "units": "meters",
            "coordinates": f"gdep{vgrid}_1d",
            "nemo_cf_vgrid": vgrid,
        }
        for vgrid in ["t", "w"]
    }
)

# masks
# Note that the f-mask lives on vertical T levels
# (c/f NEMO book)
mesh_mask_attrs.update(
    {
        f"{hgrid}mask": {
            "long_name": f"mask for {hgrid.upper()}-grid",
            "flag_meanings": "land, water",
            "flag_values": "0, 1",
            "coordinates": f"gdept_1d glam{hgrid} gphi{hgrid}",
            "nemo_cf_hgrid": hgrid,
            "nemo_cf_vgrid": "t",
        }
        for hgrid in ["t", "u", "v", "f"]
    }
)

# util masks
mesh_mask_attrs.update(
    {
        f"{hgrid}maskutil": {
            "long_name": f"mask for {hgrid.upper()}-grid without halo",
            "flag_meanings": "land, water",
            "flag_values": "0, 1",
            "coordinates": f"glam{hgrid} gphi{hgrid}",
            "nemo_cf_hgrid": hgrid,
        }
        for hgrid in ["t", "u", "v", "f"]
    }
)

# coriolis paramter
mesh_mask_attrs.update(
    {
        "ff": {
            "long_name": "Coriolis parameter on F-grid",
            "units": "s-1",
            "coordinates": "glamf gphif",
            "nemo_cf_hgrid": "t",
        }
    }
)

# number of wet grid points
mesh_mask_attrs.update(
    {
        "mbathy": {
            "long_name": "number of ocean levels at xy grid point",
            "coordinates": "glamt gphit",
            "nemo_cf_hgrid": "t",
        }
    }
)
