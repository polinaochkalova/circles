import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRectF
from random import randint


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(Qt.yellow)
            painter.drawEllipse(circle)

    def addCircle(self):
        diameter = randint(10, 100)
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)
        circle = QRectF(x, y, diameter, diameter)
        self.circles.append(circle)
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Generator")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.button = QPushButton("Generate Circle", self.central_widget)
        self.layout.addWidget(self.button)
        self.circle_widget = CircleWidget()
        self.layout.addWidget(self.circle_widget)
        self.button.clicked.connect(self.circle_widget.addCircle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
