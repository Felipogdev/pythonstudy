import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont #Font
from PyQt5.QtCore import Qt #Allingment


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(700,300,500,500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: blue;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop) #VERTICALLY TOP
        #label.setAlignment(Qt.AlignBottom) #VERTICALLY BOTTOM
        #label.setAlignment(Qt.AlignVCenter) #VERTICALLY CENTER

        #label.setAlignment(Qt.AlignRight) #HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignLeft) #HORIZONTALLY LEFT
        #label.setAlignment(Qt.AlignHCenter) #HORIZONTALLY CENTER

        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()