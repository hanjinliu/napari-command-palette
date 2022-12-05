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
storage.mark_getter("open_paths")(
    lambda: show_file_dialog(mode="rm", caption="Open files")
)
storage.mark_getter("open_dirs")(
    lambda: show_file_dialog(mode="d", caption="Open folder")
)
storage.mark_getter("save_path")(
    lambda: show_file_dialog(mode="w", caption="Save at")
)

file_group = palette.add_group("File")
view_group = palette.add_group("View")


@file_group.register("Close napari window")
def close(viewer: napari.Viewer):
    viewer.close()


@file_group.register("Preferences")
def preferences(viewer: napari.Viewer):
    viewer.window.file_menu._open_preferences()


@file_group.register("Open file(s)")
def open_file(viewer: napari.Viewer, open_paths: str | None):
    if open_paths:
        viewer.open(open_paths)


@file_group.register("Open files as stack")
def open_files_as_stack(viewer: napari.Viewer, open_paths: str | None):
    if open_paths:
        viewer.open(open_paths, stack=True)


@file_group.register("Open folder")
def open_folder(viewer: napari.Viewer, open_dir: str | None):
    if open_dir:
        viewer.open(open_dir, stack=True)


@file_group.register("Save screenshot")
def save_screenshot(viewer: napari.Viewer, save_path: str | None):
    if save_path:
        viewer.screenshot(save_path, canvas_only=True)


@file_group.register("Save screenshot with viewer")
def save_screenshot_with_viewer(viewer: napari.Viewer, save_path: str | None):
    if save_path:
        viewer.screenshot(save_path, canvas_only=False)


@view_group.register("Reset view")
def reset_view(viewer: napari.Viewer):
    viewer.reset_view()


@view_group.register("Toggle full screen")
def toggle_fullscreen(viewer: napari.Viewer):
    viewer.window._toggle_fullscreen()


@view_group.register("Toggle menubar visibility")
def toggle_menubar_visibility(viewer: napari.Viewer):
    viewer.window._toggle_menubar_visible()


@view_group.register("Toggle play")
def toggle_play(viewer: napari.Viewer):
    viewer.window._toggle_play()


@view_group.register("Toggle axes visibility")
def toggle_axes_visibility(viewer: napari.Viewer):
    viewer.axes.visible = not viewer.axes.visible


@view_group.register("Toggle axes colored")
def toggle_axes_colored(viewer: napari.Viewer):
    viewer.axes.colored = not viewer.axes.colored


@view_group.register("Toggle axes dashed")
def toggle_axes_dashed(viewer: napari.Viewer):
    viewer.axes.dashed = not viewer.axes.dashed


@view_group.register("Toggle axes labels")
def toggle_axes_labels(viewer: napari.Viewer):
    viewer.axes.labels = not viewer.axes.labels


@view_group.register("Toggle axes arrows")
def toggle_axes_arrows(viewer: napari.Viewer):
    viewer.axes.arrows = not viewer.axes.arrows


@view_group.register("Toggle scale bar visibility")
def toggle_scale_bar_visibility(viewer: napari.Viewer):
    viewer.scale_bar.visible = not viewer.scale_bar.visible


@view_group.register("Toggle scale bar colored")
def toggle_scale_bar_colored(viewer: napari.Viewer):
    viewer.scale_bar.colored = not viewer.scale_bar.colored


@view_group.register("Toggle scale bar ticks")
def toggle_scale_bar_ticks(viewer: napari.Viewer):
    viewer.scale_bar.ticks = not viewer.scale_bar.ticks


@view_group.register("Transpose dimensions")
def transpose_dims(viewer: napari.Viewer):
    viewer.dims.transpose()


@view_group.register("Toggle 3D mode")
def toggle_ndisplay(viewer: napari.Viewer):
    ndisplay = viewer.dims.ndisplay
    if ndisplay == 3:
        viewer.dims.ndisplay = 2
    else:
        viewer.dims.ndisplay = 3
