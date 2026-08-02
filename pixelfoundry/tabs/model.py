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
            icon=get_icon("modeling/editpivot.svg"),
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
        # Component Selection
        # ==================================================

        component_group = PFGroup("Component Selection")


        object_mode_btn = PFToggleButton(
            text="Object",
            callback=model.select_object_mode
        )

        vertex_btn = PFToggleButton(
            text="Vertex",
            callback=model.select_vertex_mode
        )

        edge_btn = PFToggleButton(
            text="Edge",
            callback=model.select_edge_mode
        )

        face_btn = PFToggleButton(
            text="Face",
            callback=model.select_face_mode
        )


        self.component_group = QButtonGroup()

        self.component_group.addButton(object_mode_btn)
        self.component_group.addButton(vertex_btn)
        self.component_group.addButton(edge_btn)
        self.component_group.addButton(face_btn)

        self.component_group.setExclusive(True)

        object_mode_btn.setChecked(True)


        component_group.add(object_mode_btn)
        component_group.add(vertex_btn)
        component_group.add(edge_btn)
        component_group.add(face_btn)

        component_group.stretch()

        layout.addWidget(component_group)
        
        



        # ==================================================
        # Modify
        # ==================================================

        modify_group = PFGroup(
            "Modify",
            vertical=True
        )


        # ==================================================
        # Object Operations
        # ==================================================

        object_ops_group = PFGroup("Object Operations")


        combine_btn = PFToolButton(
            icon=":polyUnite.png",
            tooltip="Combine",
            click_callback=model.combine,
            right_click_callback=model.combine_options
        )

        separate_btn = PFToolButton(
            icon=":polySeparate.png",
            tooltip="Separate",
            click_callback=model.separate,
            right_click_callback=model.separate_options
        )

        extract_btn = PFToolButton(
            icon=":polyChipOff.png",
            tooltip="Extract",
            click_callback=model.extract,
            right_click_callback=model.extract_options
        )

        detach_btn = PFToolButton(
            icon=":detach.png",
            tooltip="Detach",
            click_callback=model.detach,
            right_click_callback=model.detach_options
        )

        mirror_btn = PFToolButton(
            icon=":polyMirrorGeometry.png",
            tooltip="Mirror",
            click_callback=model.mirror,
            right_click_callback=model.mirror_options
        )


        object_ops_group.add(combine_btn)
        object_ops_group.add(separate_btn)
        object_ops_group.add(extract_btn)
        object_ops_group.add(detach_btn)
        object_ops_group.add(mirror_btn)

        object_ops_group.stretch()



        # ==================================================
        # Modeling
        # ==================================================

        modeling_group = PFGroup("Modeling")


        weld_btn = PFToolButton(
            icon=":weld_NEX32.png",
            tooltip="Weld",
            click_callback=model.weld,
            right_click_callback=model.weld_options
        )

        extrude_btn = PFToolButton(
            icon=":extrude.png",
            tooltip="Extrude",
            click_callback=model.extrude,
            right_click_callback=model.extrude_options
        )

        bevel_btn = PFToolButton(
            icon=":polyBevel.png",
            tooltip="Bevel",
            click_callback=model.bevel,
            right_click_callback=model.bevel_options
        )

        bridge_btn = PFToolButton(
            icon=":polyBridge.png",
            tooltip="Bridge",
            click_callback=model.bridge,
            right_click_callback=model.bridge_options
        )

        multi_cut_btn = PFToolButton(
            icon=":multiCut_NEX32.png",
            tooltip="Multi Cut",
            click_callback=model.multi_cut,
            right_click_callback=model.multi_cut_options
        )

        connect_btn = PFToolButton(
            icon=":connect_NEX32.png",
            tooltip="Connect",
            click_callback=model.connect,
            right_click_callback=model.connect_options
        )


        modeling_group.add(weld_btn)
        modeling_group.add(extrude_btn)
        modeling_group.add(bevel_btn)
        modeling_group.add(bridge_btn)
        modeling_group.add(multi_cut_btn)
        modeling_group.add(connect_btn)

        modeling_group.stretch()



        # ==================================================
        # Refine
        # ==================================================

        refine_group = PFGroup("Refine")


        smooth_btn = PFToolButton(
            icon=":polySmooth.png",
            tooltip="Smooth",
            click_callback=model.smooth,
            right_click_callback=model.smooth_options
        )


        adddivison_btn = PFToolButton(
            icon=":addDivision24.png",
            tooltip="Add Division",
            click_callback=model.adddivision,
            right_click_callback=model.adddivision_options
        )



    


        refine_group.add(smooth_btn)
        refine_group.add(adddivison_btn)
      

        refine_group.stretch()



        # ==================================================
        # Boolean
        # ==================================================

        boolean_group = PFGroup("Boolean")


        union_btn = PFToolButton(
             icon=":Bool_Union.png",
            tooltip="Boolean Union",
            click_callback=model.boolean_union,
            right_click_callback=model.boolean_union_options
        )

        difference_ab_btn = PFToolButton(
             icon=":Bool_dif.png",
            tooltip="Boolean Difference (A - B)",
            click_callback=model.boolean_difference_ab,
            right_click_callback=model.boolean_difference_ab_options
        )

        difference_ba_btn = PFToolButton(
             icon=":Bool_BMinusA.png",
            tooltip="Boolean Difference (B - A)",
            click_callback=model.boolean_difference_ba,
            right_click_callback=model.boolean_difference_ba_options
        )

        intersection_btn = PFToolButton(
             icon=":Bool_inter.png",
            tooltip="Boolean Intersection",
            click_callback=model.boolean_intersection,
            right_click_callback=model.boolean_intersection_options
        )


        boolean_group.add(union_btn)
        boolean_group.add(difference_ab_btn)
        boolean_group.add(difference_ba_btn)
        boolean_group.add(intersection_btn)

        boolean_group.stretch()



        # ==================================================
        # Add Modify Sections
        # ==================================================

        modify_group.add(object_ops_group)
        modify_group.add(modeling_group)
        modify_group.add(refine_group)
        modify_group.add(boolean_group)

        modify_group.stretch()

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
        # Display
        # ==================================================
        display_group = PFGroup("Display")
        layout.addWidget(display_group)


        layout.addStretch()