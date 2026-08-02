# ==========================================================
# Pixel Foundry
# Toggle Button
# ==========================================================

from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt


class PFToggleButton(QPushButton):

    def __init__(
        self,
        text="",
        callback=None,
        parent=None
    ):
        super().__init__(text, parent)

        self.callback = callback

        self.setCheckable(True)
        self.setFocusPolicy(Qt.NoFocus)

        if self.callback:
            self.clicked.connect(self.callback)
