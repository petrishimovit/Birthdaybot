import sqlite3
import datetime
while True:
    db = sqlite3.connect("../banya-helper/Banya_birthday_database.db")
    logdatenow = datetime.datetime.now()
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS banya (
        name text,
        surname text,
        birthday text
        )""")
    name = input("Введите Имя нового человека ")
    surname = input("Введите Фамилию нового человека ")
    birthday = input("Введите Дату рождения нового человека в формате ГГГГ-ММ-ЧЧ ")
    cur.execute(f"""INSERT INTO banya VALUES("{name}","{surname}","{birthday}")""")
    cur.execute("""SELECT * FROM banya""")
    db.commit()
    print("текущая таблица sqlite", cur.fetchall())
    with open("../banya-helper/Birthdaybot.log", "a") as logfile:
        logfile.write(
            f"\n{logdatenow}----в banya добавлен новый человек имя - {name} фамилия - {surname} дата рождения - {birthday}\n")
        logfile.write("\n")





