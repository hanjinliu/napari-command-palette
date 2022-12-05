from __future__ import annotations

import napari
from magicgui import magicgui
from napari.plugins import plugin_manager
from qt_command_palette import get_palette

palette = get_palette("napari")


def _get_widget(plugin_name: str, widget_name: str):
    if plugin_name in plugin_manager._function_widgets:
        functions = plugin_manager._function_widgets[plugin_name]
        if widget_name in functions:
            return functions[widget_name], "function"
    return plugin_manager.get_widget(plugin_name, widget_name)[0], "widget"


def create_plugin_runner(plugin_name: str, widget_name: str):
    """Define a function that run a plugin widget."""

    def runner(viewer: napari.Viewer):
        widget, widget_type = _get_widget(plugin_name, widget_name)

        if widget_type == "function":
            viewer.window.add_dock_widget(
                magicgui(widget),
                area="right",
                name=plugin_name + ": " + widget_name,
            )
        else:
            viewer.window.add_plugin_dock_widget(plugin_name, widget_name)

    return runner


for _, (plugin_name, widgets) in plugin_manager.iter_widgets():
    for widget_name in widgets.keys():
        plugin_group = palette.add_group(plugin_name)
        plugin_group.register(
            create_plugin_runner(plugin_name, widget_name),
            desc=widget_name,
            tooltip=f"Open {widget_name}",
        )
