# ==========================================================
# Pixel Foundry
# Group Widget
# ==========================================================

from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QVBoxLayout
)


class PFGroup(QGroupBox):

    def __init__(
        self,
        title,
        vertical=False
    ):
        super().__init__(title)

        # --------------------------------------------------
        # Layout Direction
        # --------------------------------------------------

        if vertical:
            self.layout = QVBoxLayout()
        else:
            self.layout = QHBoxLayout()

        # --------------------------------------------------
        # Spacing
        # --------------------------------------------------

        self.layout.setContentsMargins(
            8,
            8,
            8,
            8
        )

        self.layout.setSpacing(4)

        self.setLayout(self.layout)


    # ------------------------------------------------------
    # Add Widget
    # ------------------------------------------------------

    def add(self, widget):

        self.layout.addWidget(widget)


    # ------------------------------------------------------
    # Add Stretch
    # ------------------------------------------------------

    def stretch(self):

        self.layout.addStretch()