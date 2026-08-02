# ==========================================================
# Pixel Foundry
# Model Tab
# ==========================================================
import maya.cmds as cmds


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QButtonGroup
)

from pixelfoundry.widgets.pf_group import PFGroup
from pixelfoundry.widgets.pf_toolbutton import PFToolButton
from pixelfoundry.widgets.pf_togglebutton import PFToggleButton

from pixelfoundry.tools import model
from pixelfoundry.core.icons import get_icon


class ModelTab(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # ==================================================
        # Create
        # ==================================================
        create_group = PFGroup("Create")

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

        create_group.add(cube_btn)
        create_group.add(sphere_btn)
        create_group.add(cylinder_btn)
        create_group.add(plane_btn)
        create_group.add(cone_btn)
        create_group.add(torus_btn)
        create_group.add(disc_btn)

        create_group.stretch()

        layout.addWidget(create_group)


        # ==================================================
        # Transform
        # ==================================================
        transform_group = PFGroup("Transform")


        move_btn = PFToolButton(
            icon=":move_M.png",
            tooltip="Move Tool",
            click_callback=model.move_tool,
            right_click_callback=model.move_tool_options
        )

        rotate_btn = PFToolButton(
            icon=":rotate_M.png",
            tooltip="Rotate Tool",
            click_callback=model.rotate_tool,
            right_click_callback=model.rotate_tool_options
        )

        scale_btn = PFToolButton(
            icon=":scale_M.png",
            tooltip="Scale Tool",
            click_callback=model.scale_tool,
            right_click_callback=model.scale_tool_options
        )


        edit_pivot_btn = PFToolButton(
            icon=get_icon("modeling/edit_pivot.svg"),
            tooltip="Edit Pivot",
            click_callback=model.edit_pivot
        )


        center_pivot_btn = PFToolButton(
            icon=":CenterPivot.png",
            tooltip="Center Pivot",
            click_callback=model.center_pivot
        )


        # --------------------------------------------------
        # Transform Space
        # --------------------------------------------------

        object_btn = PFToggleButton(
            text="Object",
            callback=model.object_space
        )

        world_btn = PFToggleButton(
            text="World",
            callback=model.world_space
)


        self.space_group = QButtonGroup()

        self.space_group.addButton(object_btn)
        self.space_group.addButton(world_btn)

        self.space_group.setExclusive(True)

        object_btn.setChecked(True)


        # --------------------------------------------------
        # Add Transform Items
        # --------------------------------------------------

        transform_group.add(move_btn)
        transform_group.add(rotate_btn)
        transform_group.add(scale_btn)
        transform_group.add(edit_pivot_btn)
        transform_group.add(center_pivot_btn)

        transform_group.layout.addSpacing(20)

        transform_group.add(object_btn)
        transform_group.add(world_btn)

        transform_group.stretch()

        layout.addWidget(transform_group)


        # ==================================================
        # Modify
        # ==================================================
        modify_group = PFGroup("Modify")
        layout.addWidget(modify_group)


        # ==================================================
        # Normals
        # ==================================================
        normals_group = PFGroup("Normals")
        layout.addWidget(normals_group)


        # ==================================================
        # Utilities
        # ==================================================
        utilities_group = PFGroup("Utilities")
        layout.addWidget(utilities_group)


        # ==================================================
        # Selection
        # ==================================================
        selection_group = PFGroup("Selection")
        layout.addWidget(selection_group)


        # ==================================================
        # Display
        # ==================================================
        display_group = PFGroup("Display")
        layout.addWidget(display_group)


        layout.addStretch()