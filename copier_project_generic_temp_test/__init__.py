"""Test project created using copier-project's python project template."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as import_version

try:
    version = import_version("copier-project-generic-temp-test")
except PackageNotFoundError:  # pragma: no cover
    version = "0.0.0"
