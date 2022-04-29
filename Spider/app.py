from PySide2.QtWidgets import QAction, QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QStandardItemModel
import sqlite3


def getHeadLineFromDB():
    try:
        tableList = []
        conn = sqlite3.connect("wbTopRank.db")
        cur = conn.cursor()
        executeResult = cur.execute("select name from sqlite_master where type = 'table' order by name").fetchall()
        for i, tab in enumerate(executeResult, start=0):
            tableList.append(tab[0])
        sql4 = f'select * from {tableList[-2]}'
        queryResult = cur.execute(sql4)
        return queryResult
    except sqlite3.Error as e:
        print(e)


class App:
    def __init__(self):
        qfile_stats = QFile('headlineAPP.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.pushButton.clicked.connect(getHeadLineFromDB)
        self.model = QStandardItemModel(2, 10)
        self.ui.tableView.setTableView(self.model)


app = QApplication([])
stats = App()
stats.ui.show()
app.exec_()
