# ==========================================================
# Pixel Foundry
# Modeling Tools
# ==========================================================

import maya.cmds as cmds
import maya.mel as mel


# ==========================================================
# Create Primitives
# ==========================================================

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



# ==========================================================
# Transform Tools
# ==========================================================

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



# ==========================================================
# Transform Space
# ==========================================================

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



# ==========================================================
# Component Selection
# ==========================================================

def select_object_mode():
    cmds.selectMode(object=True)


def select_vertex_mode():
    cmds.selectMode(component=True)
    cmds.selectType(vertex=True)


def select_edge_mode():
    cmds.selectMode(component=True)
    cmds.selectType(edge=True)


def select_face_mode():
    cmds.selectMode(component=True)
    cmds.selectType(polymeshFace=True)



# ==========================================================
# Modify
# ==========================================================


# ----------------------------------------------------------
# Object Operations
# ----------------------------------------------------------

def combine():
    pass


def combine_options():
    pass


def separate():
    pass


def separate_options():
    pass


def extract():
    pass


def extract_options():
    pass


def detach():
    pass


def detach_options():
    pass


def mirror():
    pass


def mirror_options():
    pass



# ----------------------------------------------------------
# Modeling
# ----------------------------------------------------------

def weld():
    pass


def weld_options():
    pass


def extrude():
    pass


def extrude_options():
    pass


def bevel():
    pass


def bevel_options():
    pass


def bridge():
    pass


def bridge_options():
    pass


def multi_cut():
    pass


def multi_cut_options():
    pass


def connect():
    pass


def connect_options():
    pass



# ----------------------------------------------------------
# Refine
# ----------------------------------------------------------

def smooth():
    pass


def smooth_options():
    pass


def subdivide():
    pass


def subdivide_options():
    pass



# ----------------------------------------------------------
# Boolean
# ----------------------------------------------------------

def boolean_union():
    pass


def boolean_union_options():
    pass


def boolean_difference_ab():
    pass


def boolean_difference_ab_options():
    pass


def boolean_difference_ba():
    pass


def boolean_difference_ba_options():
    pass


def boolean_intersection():
    pass


def boolean_intersection_options():
    pass

def adddivision():
    pass


def adddivision_options():
    pass

