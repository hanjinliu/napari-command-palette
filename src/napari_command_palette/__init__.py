__version__ = "0.0.1"

# Run all the "register" functions in the submodules
from . import _defaults  # noqa
from . import _ndimage  # noqa
from . import _plugins  # noqa
from ._install import install

__all__ = ["install"]
