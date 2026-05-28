#
# Author: Lars B. Rollik <L.B.Rollik@protonmail.com>
# License: BSD 3-Clause
import warnings

warnings.warn(
    "rpi-camera-colony is deprecated and will receive no further updates. "
    "Use rpi-camera-ensemble instead.",
    DeprecationWarning,
    stacklevel=2,
)

from rpi_camera_colony.readers import read_session_data

__all__ = [
    "read_session_data",
]

__version__ = "1.0.0"
__author__ = "Lars B. Rollik"
