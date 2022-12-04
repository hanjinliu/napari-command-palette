from __future__ import annotations

from qt_command_palette import get_palette
from qtpy import QtWidgets as QtW

palette = get_palette("napari")


class QNapariCommandPalette(QtW.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setLayout(QtW.QVBoxLayout())
        button = QtW.QPushButton("Show Command Palette")
        self.layout().addWidget(button)
        button.clicked.connect(self.show_command_palette)
        self._installed = False

    def show_command_palette(self):
        ins = self
        while parent := ins.parent():
            ins = parent
            if isinstance(ins, QtW.QMainWindow):
                break
        if not self._installed:
            palette.install(ins, "Ctrl+Shift+@")
            self._installed = True
        palette.get_widget(ins).show()
