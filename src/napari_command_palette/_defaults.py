from __future__ import annotations

import napari
from magicgui.widgets import show_file_dialog
from qt_command_palette import get_palette, get_storage

palette = get_palette("napari")
storage = get_storage("napari")

storage.mark_getter("viewer")(napari.current_viewer)
storage.mark_getter("open_path")(
    lambda: show_file_dialog(mode="r", caption="Open file")
)
storage.mark_getter("save_path")(
    lambda: show_file_dialog(mode="w", caption="Save at")
)

napari_global_group = palette.add_group("")


@napari_global_group.register("Close napari window")
def close(viewer: napari.Viewer):
    viewer.close()


@napari_global_group.register("napari preferences")
def preferences(viewer: napari.Viewer):
    viewer.window.file_menu._open_preferences()


@napari_global_group.register("Open file")
def open_file(viewer: napari.Viewer, open_path: str | None):
    if open_path:
        viewer.open(open_path)


@napari_global_group.register("Reset view")
def reset_view(viewer: napari.Viewer):
    viewer.reset_view()


@napari_global_group.register("Save screenshot")
def save_screenshot(viewer: napari.Viewer, save_path: str | None):
    if save_path:
        viewer.screenshot(save_path, canvas_only=True)


@napari_global_group.register("Save screenshot with viewer")
def save_screenshot_with_viewer(viewer: napari.Viewer, save_path: str | None):
    if save_path:
        viewer.screenshot(save_path, canvas_only=False)


@napari_global_group.register("Toggle axes visibility")
def toggle_axes(viewer: napari.Viewer):
    viewer.axes.visible = not viewer.axes.visible


@napari_global_group.register("Transpose dimensions")
def transpose_dims(viewer: napari.Viewer):
    viewer.dims.transpose()


@napari_global_group.register("Toggle 3D mode")
def transpose_ndisplay(viewer: napari.Viewer):
    ndisplay = viewer.dims.ndisplay
    if ndisplay == 3:
        viewer.dims.ndisplay = 2
    else:
        viewer.dims.ndisplay = 3
