"""Console script for nemo_cf."""
import sys
from pprint import pprint
import click

from .aux import download_and_extract_zip_file
from .cf_attributes import mesh_mask_attrs


@click.command()
@click.argument("target-dir")
@click.option("--force", is_flag=True)
@click.option(
    "--url",
    default=(
        "https://zenodo.org/record/3634491/files/"
        "NEMO_GYRE_test_data_all_files.v2020.02.03.1.zip"
    ),
)
def download_data(target_dir, force, url):
    """Download NEMO example data."""

    download_and_extract_zip_file(url=url, target_dir=target_dir, force=force)

    return 0


@click.command()
def print_info():
    """Print info about NEMO cf."""

    print("nemo_cf will apply the following attributes:\n")
    pprint(mesh_mask_attrs)

    return 0


if __name__ == "__main__":
    sys.exit(print_info())  # pragma: no cover
