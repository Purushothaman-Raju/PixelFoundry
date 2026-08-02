import sys

PROJECT_PATH = r"Z:\Tool_Development\PixelFoundry"

if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

import pixelfoundry.launcher
pixelfoundry.launcher.run()