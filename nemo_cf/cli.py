"""Console script for nemo_cf."""
import sys
import click

from .aux import download_and_extract_zip_file


@click.command()
@click.argument('target-dir')
@click.option(
    '--url',
    default=(
        'https://zenodo.org/record/3634491/files/'
        'NEMO_GYRE_test_data_all_files.v2020.02.03.1.zip'
    )
)
def main(target_dir, url):
    """Download NEMO example data."""

    download_and_extract_zip_file(url=url, target_dir=target_dir)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
