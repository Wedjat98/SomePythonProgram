import sqlite3

conn = sqlite3.connect("test.db")
print("Opened database success")

c = conn.cursor()

# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int nut null,
#         address varchar(50),
#         salary real);
# '''
sql1 = '''
    insert into company (id,name,age,address,salary)
        values (1,'alex',22,'US',8000);
'''
sql2 = '''
    insert into company (id,name,age,address,salary)
        values (2,'xiaozhuzhu',29,'JP',3000);
'''
sql3 = '''
    update company set salary=3000 where id =2;
'''
sql4 = '''
    select * from company;
'''

cursor = c.execute(sql4)

for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3], "\n")

# c.execute(sql1)
# c.execute(sql2)
# c.execute(sql3)

conn.commit()
conn.close()

print("set up")
