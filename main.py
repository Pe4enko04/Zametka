import sys
from PyQt5 import QtWidgets
import zametka as design
class ExamleApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)




app=QtWidgets.QApplication(sys.argv)
window=ExamleApp()
window.show()
app.exec_()