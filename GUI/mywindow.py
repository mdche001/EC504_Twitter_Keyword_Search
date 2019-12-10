from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from hello import pt_hello
from project_504_3 import *
import os

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.former_file_name = ""
        self.file_reg = []
        self.keyword = ""
    def search(self):
        self.keyword = str(self.plainTextEdit.toPlainText())
        search_res = key_word_search(self.file_reg, self.keyword)
        self.textBrowser_3.clear()
        for i in range(10):
            self.textBrowser_3.append(str(search_res[i]))

    def read(self):
        # path D:\program\untitled
        file_name, ok = QFileDialog.getOpenFileName(self, 'Read', '/home')
        if ok:
            if (self.former_file_name != file_name):
                _f = open(file_name, 'r', encoding="utf8")
                if (os.path.splitext(file_name)[1] == '.txt'):
                    self.former_file_name = file_name
                    with _f:
                        res = _f.read()
                        self.textBrowser.append(res)
                    self.textBrowser.append("reading success...")

                    # print(file_name)
                    tweets = read_dataset(file_name)
                    # print("show partial tweets from dataset")
                    # print_tweets(tweets)
                    self.file_reg = tweets
                    # print(self.former_file_name)
                    # q = 'suffer'
                    # search_res = key_word_search(tweets, self.keyword)
                    # # print("search results")
                    # # print_tweets(search_res)
                    # for i in range(5):
                    #     self.textBrowser_3.append(str(search_res[i]))
                elif (os.path.splitext(file_name)[1] == '.csv'):
                    self.former_file_name = file_name
                    csv_file = read_csv_dataset(file_name)
                    self.file_reg = csv_file
                    for i in range(50):
                        self.textBrowser.append(csv_file[i])
                    self.textBrowser.append("reading success...")

                else:
                    self.textBrowser.append("error file type")
            else:
                # search_res = key_word_search(self.file_reg,self.keyword)
                # for i in range(5):
                #     self.textBrowser_3.append(str(search_res[i]))
                pass
    # def read(self):
    #     # path D:\program\untitled
    #     file_name, ok = QFileDialog.getOpenFileName(self, 'Read', '/home')
    #     if ok:
    #         _f = open(file_name, 'r', encoding="utf8")
    #         with _f:
    #             data = _f.read()
    #             # count = 0
    #             # for row in data:
    #             #     if (count <= 5):
    #             #         self.textBrowser.append(row)
    #             #         count += 1
    #             self.textBrowser.append(data)
    #             # self.textBrowser.append(pt_hello())
    #             self.textBrowser_3.append(pt_hello())
    #         self.textBrowser.append("reading success...")

    def save(self):
        file_name, ok = QFileDialog.getSaveFileName(self, 'Save', '/home')
        if ok:
            _f = open(file_name, 'w', encoding="utf8")
            _f.write(str(self.plainTextEdit.toPlainText()))
            self.textBrowser.append("Save success...")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())