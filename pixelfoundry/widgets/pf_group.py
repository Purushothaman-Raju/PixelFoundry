# ==========================================================
# Pixel Foundry
# Group Widget
# ==========================================================

from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout
)


class PFGroup(QGroupBox):

    def __init__(self, title):
        super().__init__(title)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(8, 8, 8, 8)
        self.layout.setSpacing(4)

        self.setLayout(self.layout)

    def add(self, widget):
        self.layout.addWidget(widget)

    def stretch(self):
        self.layout.addStretch()