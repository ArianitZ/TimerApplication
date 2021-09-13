import sys
from PyQt5.QtCore import QLine

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt


class TimerView(QMainWindow):
    def __init__(self, parent = None, window_title = "Arianit's Timer"):
        super().__init__(parent)
        self.setFixedSize(500,500)
        self.setWindowTitle(window_title)

        self._centralWidget = QWidget()
        self.setCentralWidget(self._centralWidget)
        self.initialize_window()

        
    def initialize_window(self):
        self.box_layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        self.display.setAlignment(Qt.AlignHCenter)
        self.display.setFixedHeight(250)

        self.startButton = QPushButton("Start")
        self.startButton.setFixedHeight(50)
        self.stopButton = QPushButton("Stop")
        self.stopButton.setFixedHeight(50)

        self._button_layout = QHBoxLayout()
        self._button_layout.addWidget(self.startButton)
        self._button_layout.addWidget(self.stopButton)

        self.box_layout.addWidget(self.display)
        self.box_layout.addItem(self._button_layout)

        self._centralWidget.setLayout(self.box_layout)

if __name__ == "__main__":
    timer_application = QApplication(sys.argv)

    view = TimerView()
    view.show()

    exit(timer_application.exec())