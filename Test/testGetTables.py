import sqlite3

'''

sqlite3存在系统表sqlite_master,结构如下：

sqlite_master(

    type TEXT,      #类型:table-表,index-索引,view-视图

    name TEXT,      #名称:表名,索引名,视图名

    tbl_name TEXT,

    rootpage INTEGER,

    sql TEXT

    )

'''

# 查看某数据库中所有表
result = []


def GetTables(db_file='../Spider/wbTopRank.db'):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        executeResult = cur.execute("select name from sqlite_master where type = 'table' order by name").fetchall()
        for i, tab in enumerate(executeResult, start=0):
            result.append(tab[0])
        sql4 = f'select * from {result[-2]}'
        queryResult = cur.execute(sql4)
        for row in queryResult:
            print(row[1])
    except sqlite3.Error as e:
        print(e)


'''

#查看表结构

cur.execute("PRAGMA table_info(T_Person)")

print cur.fetchall()

'''
GetTables()
