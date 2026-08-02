# ==========================================================
# Pixel Foundry
# Model Tab
# ==========================================================

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox
)

from pixelfoundry.widgets.pf_toolbutton import PFToolButton
from pixelfoundry.tools import model


class ModelTab(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # --------------------------------------------------
        # Create
        # --------------------------------------------------
        create_group = QGroupBox("Create")
        create_layout = QHBoxLayout()

        cube_btn = PFToolButton(
            icon=":polyCube.png",
            tooltip="Polygon Cube",
            click_callback=model.create_cube,
            right_click_callback=model.create_cube_options
        )

        sphere_btn = PFToolButton(
            icon=":polySphere.png",
            tooltip="Polygon Sphere",
            click_callback=model.create_sphere,
            right_click_callback=model.create_sphere_options
        )

        cylinder_btn = PFToolButton(
            icon=":polyCylinder.png",
            tooltip="Polygon Cylinder",
            click_callback=model.create_cylinder,
            right_click_callback=model.create_cylinder_options
        )

        plane_btn = PFToolButton(
            icon=":polyPlane.png",
            tooltip="Polygon Plane",
            click_callback=model.create_plane,
            right_click_callback=model.create_plane_options
        )

        cone_btn = PFToolButton(
            icon=":polyCone.png",
            tooltip="Polygon Cone",
            click_callback=model.create_cone,
            right_click_callback=model.create_cone_options
        )

        torus_btn = PFToolButton(
            icon=":polyTorus.png",
            tooltip="Polygon Torus",
            click_callback=model.create_torus,
            right_click_callback=model.create_torus_options
        )

        disc_btn = PFToolButton(
            icon=":polyDisc.png",
            tooltip="Polygon Disc",
            click_callback=model.create_disc,
            right_click_callback=model.create_disc_options
        )

        create_layout.addWidget(cube_btn)
        create_layout.addWidget(sphere_btn)
        create_layout.addWidget(cylinder_btn)
        create_layout.addWidget(plane_btn)
        create_layout.addWidget(cone_btn)
        create_layout.addWidget(torus_btn)
        create_layout.addWidget(disc_btn)
        create_layout.addStretch()

        create_group.setLayout(create_layout)

        layout.addWidget(create_group)
        layout.addStretch()