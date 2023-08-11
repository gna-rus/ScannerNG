import model
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 573)
        MainWindow.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(610, 470, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(610, 30, 181, 401))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.pushButtonMenu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMenu.setGeometry(QtCore.QRect(10, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonMenu.setFont(font)
        self.pushButtonMenu.setObjectName("pushButtonMenu")
        self.pushButtonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpen.setGeometry(QtCore.QRect(610, 440, 61, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonOpen.setFont(font)
        self.pushButtonOpen.setStyleSheet("background-color: rgb(199, 199, 0);")
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(14, 30, 591, 531))
        self.mainLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.mainLabel.setText("")
        self.mainLabel.setObjectName("mainLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonStart.clicked.connect(model.add)  # алгоритм подключения нажатия кнопки
        pixmap = QtGui.QPixmap('cat1.png')
        self.mainLabel.setPixmap(pixmap)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScanerNG"))
        self.pushButtonStart.setText(_translate("MainWindow", "Start"))
        self.pushButtonMenu.setText(_translate("MainWindow", "Menu"))
        self.pushButtonOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
