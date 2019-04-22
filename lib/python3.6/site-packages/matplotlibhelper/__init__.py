from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .matplotlib_helper import (
    ready, img, img_path,
    dump2D, stex,
    GR, inch, cm, mm, figsize
)
