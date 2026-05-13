from PyQt6.QtWidgets import (
    QMainWindow, QSystemTrayIcon, QStyle, QWidget, QVBoxLayout, QPushButton,
    QHBoxLayout, QLineEdit
)
from PyQt6.QtGui import QIntValidator

from snipping import Snipping
from storage import Storage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.snip = Snipping()
        self.storage = Storage()
        
        self.setup_notification()        
        self.setup_ui()
        self.setup_connections()
        
    def setup_notification(self):
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon))
        self.tray.show()

    def setup_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Snipping OCR")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        self.top_row = QVBoxLayout()
        main_layout.addLayout(self.top_row)

        self.bottom_row = QVBoxLayout()
        main_layout.addLayout(self.bottom_row)

        # Coords Layout
        self.coords_layout = QHBoxLayout()
        self.bottom_row.addLayout(self.coords_layout)
        coords_validator = QIntValidator()

        self.x_coords = QLineEdit()
        self.x_coords.setPlaceholderText("X")
        self.x_coords.setValidator(coords_validator)
        self.coords_layout.addWidget(self.x_coords)

        self.y_coords = QLineEdit()
        self.y_coords.setPlaceholderText("Y")
        self.y_coords.setValidator(coords_validator)
        self.coords_layout.addWidget(self.y_coords)

        self.width_coords = QLineEdit()
        self.width_coords.setPlaceholderText("W")
        self.width_coords.setValidator(coords_validator)
        self.coords_layout.addWidget(self.width_coords)

        self.height_coords = QLineEdit()
        self.height_coords.setPlaceholderText("H")
        self.height_coords.setValidator(coords_validator)
        self.coords_layout.addWidget(self.height_coords)

        self.snip_button = QPushButton("+")
        self.bottom_row.addWidget(self.snip_button)
    
    def setup_connections(self):
        self.snip_button.clicked.connect(self.snip_screen)
    
    def show_notifications(self, title, message=''):
        self.tray.showMessage(
            title,
            message,
            QSystemTrayIcon.MessageIcon.Information,
            5000
        )

    def snip_screen(self):
        self.show_notifications("Screenshot Taken...")
        x = int(self.x_coords.text())
        y = int(self.y_coords.text())
        w = int(self.width_coords.text())
        h = int(self.height_coords.text())
        self.snip.screenshot(x, y, w, h)
