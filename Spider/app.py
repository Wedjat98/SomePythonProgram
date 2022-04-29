from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget
from ui_headlineAPP import Ui_APP as Ui_MainWindow
import sqlite3
import wbSpider


def getHeadLineFromDB():
    tableList = []
    wbSpider.main()
    conn = sqlite3.connect("wbTopRank.db")
    cur = conn.cursor()
    executeResult = cur.execute("select name from sqlite_master where type = 'table' order by name").fetchall()
    for i, tab in enumerate(executeResult, start=0):
        tableList.append(tab[0])
    sql4 = f'select * from {tableList[-2]}'
    queryResult = cur.execute(sql4)
    return queryResult
    # for row in queryResult:
    #     print(row[1])


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(getHeadLineFromDB)
        # self.ui.listWidget.addItem('demo')
        for row in getHeadLineFromDB():
            self.ui.listWidget.addItem(row[1])


app = QApplication([])
mainWindow = MainWindow()
mainWindow.show()
app.exec_()
