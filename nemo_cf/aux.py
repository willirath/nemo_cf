"""Auxiliary functionality for nemo_cf."""

from pathlib import Path
import urllib.request
import zipfile


def are_nc_files_in_dir(directory):
    directory = Path(directory)
    nc_files = list(directory.glob("*.nc"))
    nc_files += list(directory.glob("**/*.nc"))
    print(nc_files)
    return len(nc_files) > 0


def download_and_extract_zip_file(target_dir=None, url=None, force=False):
    """Download zip file from `url` and extract to `target_dir`."""
    if force or (not are_nc_files_in_dir(target_dir)):
        filehandle = urllib.request.urlretrieve(url)[0]
        zip_file_object = zipfile.ZipFile(filehandle, "r")
        zip_file_object.extractall(target_dir)
