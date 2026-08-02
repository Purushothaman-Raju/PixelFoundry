from pixelfoundry.window import PixelFoundryWindow

window = None


def run():
    global window

    try:
        if window:
            window.close()
            window.deleteLater()
    except Exception:
        pass

    window = PixelFoundryWindow()
    window.show()