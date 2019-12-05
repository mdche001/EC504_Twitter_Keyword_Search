from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def read(self):
        file_name, ok = QFileDialog.getOpenFileName(self, 'Read', '/home')
        if ok:
            _f = open(file_name, 'r')
            with _f:
                data = _f.read()
                self.textBrowser.append(data)
            self.textBrowser.append("reading success...")

    def save(self):
        file_name, ok = QFileDialog.getSaveFileName(self, 'Save', '/home')
        if ok:
            _f = open(file_name, 'w')
            _f.write(str(self.plainTextEdit.toPlainText()))
            self.textBrowser.append("Save success...")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())