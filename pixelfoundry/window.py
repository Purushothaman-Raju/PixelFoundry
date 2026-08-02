from PySide6.QtWidgets import QMainWindow, QWidget


class PixelFoundryWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pixel Foundry")
        self.resize(500, 700)

        central = QWidget()
        self.setCentralWidget(central)