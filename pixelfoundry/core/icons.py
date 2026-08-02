# ==========================================================
# Pixel Foundry
# Icon Manager
# ==========================================================

import os


PIXELFOUNDRY_ROOT = os.path.dirname(
    os.path.dirname(__file__)
)


def get_icon(relative_path):

    return os.path.join(
        PIXELFOUNDRY_ROOT,
        "icons",
        relative_path
    )