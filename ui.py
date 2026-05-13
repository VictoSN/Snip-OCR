from PyQt6.QtWidgets import (
    QMainWindow, QSystemTrayIcon, QStyle, QWidget, QVBoxLayout, QPushButton
)

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
        
        self.bottom_row = QVBoxLayout()
        main_layout.addLayout(self.bottom_row)
        
        self.snip_button = QPushButton("+")
        self.bottom_row.addWidget(self.snip_button)
    
    def setup_connections(self):
        self.snip_button.clicked.connect(self.snip_screen)
    
    def snip_screen(self):
        self.snip.screenshot()