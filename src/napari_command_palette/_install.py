from __future__ import annotations

import napari
from qt_command_palette import get_palette
from qtpy import QtWidgets as QtW

palette = get_palette("napari")


def install(
    viewer: napari.Viewer | None = None,
    keys: str = "F1",
):
    """
    Install command palette to napari viewer.

    Parameters
    ----------
    viewer : napari.Viewer, optional
        napari viewer to install command palette to. By default current
        viewer is used.
    keys : str, default "F1"
        Key sequence to open command palette.
    """
    if viewer is None:
        viewer = napari.current_viewer()
        if viewer is None:
            raise RuntimeError("No viewer found")

    ins = viewer.window._qt_viewer
    while parent := ins.parent():
        ins = parent
        if isinstance(ins, QtW.QMainWindow):
            palette.install(ins, keys)
            return
    raise RuntimeError("No MainWindow found")
