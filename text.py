import sqlite3
from datetime import datetime, timedelta, date
current_date = datetime.now().date()
def convert_date_to_text(date_str):
    try:
        months = {
            1: "января",
            2: "февраля",
            3: "марта",
            4: "апреля",
            5: "мая",
            6: "июня",
            7: "июля",
            8: "августа",
            9: "сентября",
            10: "октября",
            11: "ноября",
            12: "декабря"
        }

        date = datetime.strptime(str(date_str), "%Y-%m-%d").date()
        day = date.day
        month = months[date.month]

        return f"{day} {month}"
    except ValueError:
        return "Некорректный формат даты"

def convert_into_iso(date_str):
    day, month = date_str.split('-')


    day = int(day)
    month = int(month)


    year = datetime.now().year

    # Возвращаем дату в формате ГГГГ-ММ-ДД
    return f"{year}-{day:02d}-{month:02d}"
def converter_day_month(date_sqlite_format):

    # Разделяем строку на день и месяц
    day, month = map(int, date_sqlite_format.split('-'))


    day, month = month, day


    months = ['Января','Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
              'Июля', 'Августа', 'Сентябя', 'Октября', 'Ноября', 'Декабря']


    if 1 <= month <= 12:
        return f'{day} {months[month - 1]}'


    else:
        return f"Неверный формат даты: {date_sqlite_format}"
listfor_neardate = []
with sqlite3.connect("Banya_birthday_database.db") as db:
    allbirthday = ["start"]
    cur = db.cursor()
    cur.execute("""SELECT * FROM banya """)
    allinfonow_iso = ""

    allbirthday_sqlite = cur.fetchall()
    for i in allbirthday_sqlite:

        for n in i:
            allbirthday.append(n)
            iso_birthday = allbirthday.copy()

for _ in iso_birthday:
    if iso_birthday.index(_) % 3 == 0 and iso_birthday.index(_) != 0:
        indexation = iso_birthday.index(_)

        surname_indexation = indexation - 1
        name_indexation = indexation - 2
        isoconverted = str(convert_into_iso(_))
        iso_birthday[indexation] = isoconverted

        iso_birthday[indexation] = isoconverted

        listfor_neardate.append(isoconverted)

        future_dates = []


        current_date = datetime.now().date()
        future_dates = []

for date_str in listfor_neardate:
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    if date > current_date:
        future_dates.append(date)

if future_dates:

    nearest_date = min(future_dates)
    print("Ближайшая дата в будущем:", convert_date_to_text(nearest_date) ,iso_birthday[iso_birthday.index((nearest_date).isoformat()  )-1] ,iso_birthday[iso_birthday.index((nearest_date).isoformat())-2] )







