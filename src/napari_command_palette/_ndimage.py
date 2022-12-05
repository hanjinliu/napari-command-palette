from typing import Callable, Literal

import napari
from magicgui import magicgui
from magicgui.widgets import Dialog
from napari.types import ImageData
from scipy import ndimage as ndi

from ._api import add_group


def _as_dialog(func: Callable):
    mgui = magicgui(func, call_button=False)

    def wrapper(viewer: napari.Viewer):
        dlg = Dialog(widgets=mgui, parent=viewer.window._qt_viewer)
        dlg.reset_choices()
        if dlg.exec():
            mgui()

    return wrapper


ndi_group = add_group("scipy.ndimage")


@ndi_group.register("Gaussian filter")
@_as_dialog
def gaussian_filter(
    image: ImageData,
    sigma: float = 1.0,
    order: Literal[0, 1, 3] = 3,
    mode: Literal[
        "reflect", "constant", "nearest", "mirror", "wrap"
    ] = "reflect",
    cval: str = "0",
) -> ImageData:
    return ndi.gaussian_filter(
        image, sigma, order=order, mode=mode, cval=float(cval)
    )


@ndi_group.register("Median filter")
@_as_dialog
def median_filter(
    image: ImageData,
    size: int = 3,
    mode: Literal[
        "reflect", "constant", "nearest", "mirror", "wrap"
    ] = "reflect",
    cval: str = "0",
) -> ImageData:
    return ndi.median_filter(image, size, mode=mode, cval=float(cval))


@ndi_group.register("Uniform filter")
@_as_dialog
def uniform_filter(
    image: ImageData,
    size: int = 3,
    mode: Literal[
        "reflect", "constant", "nearest", "mirror", "wrap"
    ] = "reflect",
    cval: str = "0",
) -> ImageData:
    return ndi.uniform_filter(image, size, mode=mode, cval=float(cval))


@ndi_group.register("Laplace filter")
@_as_dialog
def laplace(
    image: ImageData,
    mode: Literal[
        "reflect", "constant", "nearest", "mirror", "wrap"
    ] = "reflect",
    cval: str = "0",
) -> ImageData:
    return ndi.laplace(image, mode=mode, cval=float(cval))


@ndi_group.register("Sobel filter")
@_as_dialog
def sobel(
    image: ImageData,
    axis: Literal[-1, 0, 1, 2] = -1,
    mode: Literal[
        "reflect", "constant", "nearest", "mirror", "wrap"
    ] = "reflect",
    cval: str = "0",
) -> ImageData:
    return ndi.sobel(image, axis=axis, mode=mode, cval=float(cval))


@ndi_group.register("Prewitt filter")
@_as_dialog
def prewitt(
    image: ImageData,
    axis: Literal[-1, 0, 1, 2] = -1,
    mode: Literal[
        "reflect", "constant", "nearest", "mirror", "wrap"
    ] = "reflect",
    cval: str = "0",
) -> ImageData:
    return ndi.prewitt(image, axis=axis, mode=mode, cval=float(cval))
