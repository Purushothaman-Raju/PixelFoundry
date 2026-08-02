# ==========================================================
# Pixel Foundry
# Main Application Window
# Autodesk Maya 2027
# ==========================================================

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTabWidget
)

from pixelfoundry.tabs.model import ModelTab


class PixelFoundryWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # --------------------------------------------------
        # Window
        # --------------------------------------------------
        self.setWindowTitle("Pixel Foundry")
        self.resize(700, 800)

        # --------------------------------------------------
        # Central Widget
        # --------------------------------------------------
        central = QWidget()
        self.setCentralWidget(central)

        # --------------------------------------------------
        # Main Layout
        # --------------------------------------------------
        layout = QVBoxLayout(central)

        # --------------------------------------------------
        # Tabs
        # --------------------------------------------------
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # --------------------------------------------------
        # Production Tabs
        # --------------------------------------------------
        self.tabs.addTab(ModelTab(), "Model")
        self.tabs.addTab(QWidget(), "UV")
        self.tabs.addTab(QWidget(), "Shading")
        self.tabs.addTab(QWidget(), "Rigging")
        self.tabs.addTab(QWidget(), "Animation")
        self.tabs.addTab(QWidget(), "FX")
        self.tabs.addTab(QWidget(), "Lighting")
        self.tabs.addTab(QWidget(), "Rendering")

        # --------------------------------------------------
        # Status Bar
        # --------------------------------------------------
        self.statusBar().showMessage("Ready")