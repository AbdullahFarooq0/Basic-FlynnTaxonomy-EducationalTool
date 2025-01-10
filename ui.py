from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel, QWidget
from sisd import visualize_sisd
from simd import visualize_simd
from misd import visualize_misd
from mimd import visualize_mimd

class FlynnGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flynn's Taxonomy Visualization")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Select an Architecture:")
        layout.addWidget(self.label)

        self.sisd_button = QPushButton("SISD")
        self.sisd_button.clicked.connect(self.run_sisd)
        layout.addWidget(self.sisd_button)

        self.simd_button = QPushButton("SIMD")
        self.simd_button.clicked.connect(self.run_simd)
        layout.addWidget(self.simd_button)

        self.misd_button = QPushButton("MISD")
        self.misd_button.clicked.connect(self.run_misd)
        layout.addWidget(self.misd_button)

        self.mimd_button = QPushButton("MIMD")
        self.mimd_button.clicked.connect(self.run_mimd)
        layout.addWidget(self.mimd_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_sisd(self):
        visualize_sisd(3, 5)

    def run_simd(self):
        visualize_simd([1, 2, 3, 4])

    def run_misd(self):
        visualize_misd(5)

    def run_mimd(self):
        visualize_mimd([5, 2, 9], [1, 2, 3])

def launch_gui():
    app = QApplication([])
    window = FlynnGUI()
    window.show()
    app.exec_()
