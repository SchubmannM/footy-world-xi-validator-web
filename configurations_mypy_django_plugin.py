import os

from configurations.importer import install
from mypy.version import __version__
from mypy_django_plugin import main


def plugin(version):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "footy_world_xi_validator.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")
    install()
    return main.plugin(version)
