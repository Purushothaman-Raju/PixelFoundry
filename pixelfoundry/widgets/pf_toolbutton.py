# ==========================================================
# Pixel Foundry
# Tool Button
# ==========================================================

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QToolButton


class PFToolButton(QToolButton):

    def __init__(
        self,
        icon="",
        tooltip="",
        click_callback=None,
        right_click_callback=None,
        parent=None
    ):
        super().__init__(parent)

        self.click_callback = click_callback
        self.right_click_callback = right_click_callback

        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(32, 32))
        self.setToolTip(tooltip)

        self.setAutoRaise(True)
        self.setCheckable(False)
        self.setFocusPolicy(Qt.NoFocus)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:
            if self.click_callback:
                self.click_callback()

        elif event.button() == Qt.RightButton:
            if self.right_click_callback:
                self.right_click_callback()

        event.accept()