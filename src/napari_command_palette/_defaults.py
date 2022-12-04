from __future__ import annotations

import napari
from qt_command_palette import get_palette

palette = get_palette("napari")

napari_global_group = palette.add_group("")


@napari_global_group.register("Close window")
def close():
    viewer = napari.current_viewer()
    viewer.close()


@napari_global_group.register("Preferences")
def preferences():
    viewer = napari.current_viewer()
    viewer.window.file_menu._open_preferences()
