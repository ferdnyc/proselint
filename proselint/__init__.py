# flake8: noqa

"""Proselint applies advice from great writers to your writing."""
from . import tools
from .version import __version__
from .logger import log
from . import checks
from .config_paths import proselint_path as path
from .config_base import proselint_base as config_default

__all__ = ["tools", "log", "checks", "path", "config_default"]
