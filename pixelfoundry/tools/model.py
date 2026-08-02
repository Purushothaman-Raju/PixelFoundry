# ==========================================================
# Pixel Foundry
# Modeling Tools
# ==========================================================

import maya.cmds as cmds
import maya.mel as mel


# ----------------------------------------------------------
# Create Primitives
# ----------------------------------------------------------

def create_cube():
    cmds.polyCube()


def create_cube_options():
    mel.eval("CreatePolygonCubeOptions;")


def create_sphere():
    cmds.polySphere()


def create_sphere_options():
    mel.eval("CreatePolygonSphereOptions;")


def create_cylinder():
    cmds.polyCylinder()


def create_cylinder_options():
    mel.eval("CreatePolygonCylinderOptions;")


def create_plane():
    cmds.polyPlane()


def create_plane_options():
    mel.eval("CreatePolygonPlaneOptions;")


def create_cone():
    cmds.polyCone()


def create_cone_options():
    mel.eval("CreatePolygonConeOptions;")


def create_torus():
    cmds.polyTorus()


def create_torus_options():
    mel.eval("CreatePolygonTorusOptions;")


def create_disc():
    cmds.polyDisc()


def create_disc_options():
    mel.eval("CreatePolygonDiscOptions;")

def move_tool():
    cmds.setToolTo("moveSuperContext")


def rotate_tool():
    cmds.setToolTo("RotateSuperContext")


def scale_tool():
    cmds.setToolTo("scaleSuperContext")

def move_tool_options():
    mel.eval("MoveToolOptions")


def rotate_tool_options():
    mel.eval("RotateToolOptions")


def scale_tool_options():
    mel.eval("ScaleToolOptions")

def edit_pivot():
    cmds.ToggleRotatePivotMode()


def center_pivot():
    cmds.xform(cp=True)


def object_space():
    cmds.manipMoveContext(
        "Move",
        edit=True,
        mode=0
    )

    cmds.manipRotateContext(
        "RotateSuperContext",
        edit=True,
        mode=0
    )

    cmds.manipScaleContext(
        "scaleSuperContext",
        edit=True,
        mode=0
    )


def world_space():
    cmds.manipMoveContext(
        "Move",
        edit=True,
        mode=2
    )

    cmds.manipRotateContext(
        "RotateSuperContext",
        edit=True,
        mode=2
    )

    cmds.manipScaleContext(
        "scaleSuperContext",
        edit=True,
        mode=2
    )