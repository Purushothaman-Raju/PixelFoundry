# ==========================================================
# Pixel Foundry
# Main Application Window
# Autodesk Maya 2027
# ==========================================================

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QGroupBox,
    QToolButton
)


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
        main_layout = QVBoxLayout(central)

        # --------------------------------------------------
        # Tabs
        # --------------------------------------------------
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # ==================================================
        # MODEL TAB
        # ==================================================
        model_tab = QWidget()
        model_layout = QVBoxLayout(model_tab)

        # --------------------------------------------------
        # Create Group
        # --------------------------------------------------
        create_group = QGroupBox("Create")
        create_layout = QHBoxLayout()

        # Cube
        cube_btn = QToolButton()
        cube_btn.setIcon(QIcon(":polyCube.png"))      
        cube_btn.setIconSize(QSize(32, 32))
        cube_btn.setToolTip("Create Polygon Cube")

        # Sphere
        sphere_btn = QToolButton()
        sphere_btn.setIcon(QIcon(":polySphere.png"))
        sphere_btn.setIconSize(QSize(32, 32))
        sphere_btn.setToolTip("Create Polygon Sphere")

        # Cylinder
        cylinder_btn = QToolButton()
        cylinder_btn.setIcon(QIcon(":polyCylinder.png"))
        cylinder_btn.setIconSize(QSize(32, 32))
        cylinder_btn.setToolTip("Create Polygon Cylinder")

        # Plane
        plane_btn = QToolButton()
        plane_btn.setIcon(QIcon(":polyPlane.png"))
        plane_btn.setIconSize(QSize(32, 32))
        plane_btn.setToolTip("Create Polygon Plane")

        # Cone
        cone_btn = QToolButton()
        cone_btn.setIcon(QIcon(":polyCone.png"))
        cone_btn.setIconSize(QSize(32, 32))
        cone_btn.setToolTip("Create Polygon Cone")

        # Torus
        torus_btn = QToolButton()
        torus_btn.setIcon(QIcon(":polyTorus.png"))
        torus_btn.setIconSize(QSize(32, 32))
        torus_btn.setToolTip("Create Polygon Torus")

         # Disc
        disc_btn = QToolButton()
        disc_btn.setIcon(QIcon(":polyDisc.png"))
        disc_btn.setIconSize(QSize(32, 32))
        disc_btn.setToolTip("Create Polygon Disc")

        # Add buttons
        create_layout.addWidget(cube_btn)
        create_layout.addWidget(sphere_btn)
        create_layout.addWidget(cylinder_btn)
        create_layout.addWidget(plane_btn)
        create_layout.addWidget(cone_btn)
        create_layout.addWidget(torus_btn)
        create_layout.addWidget(disc_btn)
        create_layout.addStretch()

        create_group.setLayout(create_layout)

        model_layout.addWidget(create_group)
        model_layout.addStretch()

        self.tabs.addTab(model_tab, "Model")

        # ==================================================
        # OTHER TABS
        # ==================================================
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