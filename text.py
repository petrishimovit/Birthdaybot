import sqlite3
db_birthday = []
allinfo_db = ""
def convert_into_iso(date_str):
    day, month = date_str.split('-')


    day = int(day)
    month = int(month)


    year = 2024

    # Возвращаем дату в формате ГГГГ-ММ-ДД
    return f"{year}-{day:02d}-{month:02d}"

with sqlite3.connect("Banya_birthday_database.db") as db:
    allbirthday = ["start"]
    cur = db.cursor()
    cur.execute("""SELECT * FROM banya """)
    allbirthday_sqlite = cur.fetchall()
    for i in allbirthday_sqlite:
        for n in i:
            allbirthday.append(n)
            iso_birthday = allbirthday.copy()
for _ in iso_birthday:


    if iso_birthday.index(_) % 3 == 0 and iso_birthday.index(_) != 0:


        iso_birthday[iso_birthday.index(_)] = str(convert_into_iso(_))


        input_for_tele_name = iso_birthday.index(str(convert_into_iso(_))) - 1


        input_for_tele_surname = iso_birthday.index(str(convert_into_iso(_))) - 2



        allinfonow = iso_birthday[input_for_tele_name] + " " + iso_birthday[input_for_tele_surname] + " " + str(
                convert_into_iso(_))

        allinfo_db += f"{allinfonow}\n"
print()
print(allinfo_db)