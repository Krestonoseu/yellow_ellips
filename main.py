import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic
import random


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')

        self.pushButton.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag is True:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            for i in range(5):
                radius = random.randint(1, 50)
                painter.drawEllipse(random.randint(1, 512), random.randint(1, 506), radius, radius)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
