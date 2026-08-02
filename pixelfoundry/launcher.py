from pixelfoundry.window import PixelFoundryWindow

window = None


def run():
    global window

    if window:
        window.close()

    window = PixelFoundryWindow()
    window.show()