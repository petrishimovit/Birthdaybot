import sqlite3
with sqlite3.connect("Banya_birthday_database.db") as db:
    allbirthday = ["start"]
    cur = db.cursor()
    cur.execute("""SELECT * FROM banya """)
    allbirthday_sqlite = cur.fetchall()
    for i in allbirthday_sqlite:
        # print(i)
        for n in i:

            allbirthday.append(n)

print(allbirthday)
#     for i in allbirthday_sqlite:
#         for n in i:
#             allbirthday = []
#             allbirthday.append(n)
# print(allbirthday,allbirthday_sqlite)