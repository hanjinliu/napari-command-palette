from __future__ import annotations

from typing import Callable, TypeVar, overload

from qt_command_palette import get_palette

_F = TypeVar("_F", bound=Callable)
NAPARI = "napari"


def add_group(title: str):
    """
    Add a command group to the napari global command palette.

    Examples
    --------
    >>> group = add_group("My Commands")
    """
    return get_palette(NAPARI).add_group(title)


@overload
def register(
    func: _F,
    title: str | None,
    desc: str | None = None,
    tooltip: str | None = None,
) -> _F:
    ...


@overload
def register(
    title: str | None,
    desc: str | None = None,
    tooltip: str | None = None,
) -> Callable[[_F], _F]:
    ...


def register(*args, **kwargs):
    """
    Register a function to the napari global command palette.

    Examples
    --------
    >>> @register
    ... def my_command():
    ...     print("Hello World!")
    >>> @register("My Command")
    ... def my_command():
    ...     print("Hello World!")
    """
    return get_palette(NAPARI).register(*args, **kwargs)
