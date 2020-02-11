"""Auxiliary functionality for nemo_cf."""

import zipfile
import urllib.request


def download_and_extract_zip_file(target_dir=None, url=None):
    """Download zip file from `url` and extract to `target_dir`."""
    filehandle = urllib.request.urlretrieve(url)[0]
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    zip_file_object.extractall(target_dir)
