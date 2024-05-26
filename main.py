import telebot
import webbrowser
import sqlite3
from telebot import types
import datetime
from datetime import datetime, timedelta, date
import asyncio
import threading
from time import sleep



day_now = str(datetime.now().day)
month_now=str(datetime.now().month)
datenow = (f"{month_now}-{day_now}")
logdatenow = str(date.today())
datetoseconds = datetime.now().strftime("%Y-%m-%d")
current_date = datetime.now().date()



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

def convert_into_iso(date_str):
    day, month = date_str.split('-')


    day = int(day)
    month = int(month)


    year = datetime.now().year

    # Возвращаем дату в формате ГГГГ-ММ-ДД
    return f"{year}-{day:02d}-{month:02d}"
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

db_birthday = []

allinfo_db = ""
allinfo = ""


bot = telebot.TeleBot('7027598404:AAGkSY5MIScCcBXI8YUQxZRJ-_5SU-Bqs34')#токенбота
current_chat = "-1002004314793"

"""ОБРАБОТКА КОМАНДЫ GETBIRTHDAY"""
"""ПО КОМАНДЕ"""
@bot.message_handler(commands=["getbirthdays","geybirthdays","get"])
def description(message):
    with open("birthdays.txt","r" , encoding="utf-8") as birthdday_file:
        markup_inline = types.InlineKeyboardMarkup()
        button_for_getbirthday = types.InlineKeyboardButton(text = "У кого ближайший день рождения?" ,callback_data="/near")
        markup_inline.add(button_for_getbirthday)
        bot.send_message(chat_id=current_chat, text=birthdday_file.read() , reply_markup=markup_inline)
@bot.callback_query_handler(func = lambda call: True)
def answer(call):
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
        bot.send_message(chat_id=current_chat,
                         text=f"Ближайший день рождения у {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 1]} {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 2]} - {convert_date_to_text(nearest_date)}  ")
"""ПО КНОПКЕ"""
@bot.message_handler(func=lambda message: message.text == "Все дни рождения")
def description(message):
    with open("birthdays.txt","r" , encoding="utf-8") as birthdday_file:
        markup_inline = types.InlineKeyboardMarkup()
        button_for_getbirthday = types.InlineKeyboardButton(text = "У кого ближайший день рождения?" ,callback_data="/near")
        markup_inline.add(button_for_getbirthday)
        bot.send_message(chat_id=current_chat, text=birthdday_file.read() , reply_markup=markup_inline)
@bot.callback_query_handler(func = lambda call: True)
def answer(call):
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
        bot.send_message(chat_id=current_chat,
                         text=f"Ближайший день рождения у {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 1]} {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 2]} - {convert_date_to_text(nearest_date)}  ")



"""ОБРАБОТКА КОМАНДЫ START"""
"""ПО КОМАНДЕ"""
@bot.message_handler(commands=["start","начать","стартуй","стартануть","new"])
def description(message):
    with open("description.txt","r" , encoding="utf-8") as description_file:

        markupforallusers = types.ReplyKeyboardMarkup()
        button_near = types.KeyboardButton(text="У кого ближайший день рождения?",)
        button_info = types.KeyboardButton(text="Вывести информацию о боте")
        button_get = types.KeyboardButton(text="Все дни рождения")
        button_start = types.KeyboardButton(text="Перезапустить бота ")
        button_data = types.KeyboardButton(text="Вывести текущую дату")
        markupforallusers.row(button_near,button_info,button_data)
        markupforallusers.row(button_get,button_start )
        bot.send_message(message.chat.id, description_file.read(), reply_markup =markupforallusers)
"""ПО КНОПКЕ"""

@bot.message_handler(func=lambda message: message.text == "Перезапустить бота")
def description(message):
    with open("description.txt","r" , encoding="utf-8") as description_file:

        markupforallusers = types.ReplyKeyboardMarkup()
        button_near = types.KeyboardButton(text="У кого ближайший день рождения?",)
        button_info = types.KeyboardButton(text="Вывести информацию о боте")
        button_get = types.KeyboardButton(text="Все дни рождения")
        button_start = types.KeyboardButton(text="Перезапустить бота ")
        button_data = types.KeyboardButton(text="Вывести текущую дату")
        markupforallusers.row(button_near,button_info,button_data)
        markupforallusers.row(button_get,button_start )
        bot.send_message(message.chat.id, description_file.read(), reply_markup =markupforallusers)


"""ОБРАБОТКА КОМАНДЫ INFO"""

"""ПО КНОПКЕ"""
@bot.message_handler(func=lambda message: message.text == "Вывести информацию о боте")
def info(message):
    with open("info.txt","r" , encoding="utf-8") as info_file:
        bot.send_message(message.chat.id, info_file.read() )
"""ПО КОМАНДЕ"""
@bot.message_handler(commands=["info","information","i"])
def info(message):
    with open("info.txt","r" , encoding="utf-8") as info_file:
        bot.send_message(message.chat.id, info_file.read() )














"""ОБРАБОТКА КОМАНДЫ DATA"""
"""ПО КОМАНДЕ"""
@bot.message_handler(commands=["date","data","d"])
def info(message):
    bot.send_message(message.chat.id, f"Сегодня {logdatenow}" )
"""ПО КНОПКЕ"""


@bot.message_handler(func=lambda message: message.text == "Вывести текущую дату")
def info(message):
    bot.send_message(message.chat.id, f"Сегодня {logdatenow}")



"""ФУНКЦИЯ ДЛЯ БЛИЖАЙШЕГО ДНЯ РОЖДЕНИЯ"""

"""ПО КОМАНДЕ ИЛИ ПО ИНЛАЙН """
@bot.message_handler(commands=["ближайшийдр","nearbirthday","near"])
def nearbirthday(message):
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
        bot.send_message(chat_id=current_chat,
                         text = f"Ближайший день рождения у {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 1]} {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 2]} - {convert_date_to_text(nearest_date)}  ")
"""ПО КНОПКЕ"""
@bot.message_handler(func=lambda message: message.text == "У кого ближайший день рождения?")
def nearbirthday(message):
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
        bot.send_message(chat_id=current_chat,
                         text = f"Ближайший день рождения у {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 1]} {iso_birthday[iso_birthday.index((nearest_date).isoformat()) - 2]} - {convert_date_to_text(nearest_date)}  ")






"""ФУНКЦИЯ ЧТОБЫ В ДЕНЬ РОЖДЕНИЯ ПРИСЫЛАТЬ АЛЕРТ"""

def alert():
    with sqlite3.connect("Banya_birthday_database.db") as db:
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS banya (
            name text,
            surname text,
            birthday text
            )""")
        try:  # cur.execute(f"""INSERT INTO banya VALUES("Petr","Ishimov","2010-07-20")""")
            cur.execute(f"""SELECT * FROM banya WHERE birthday = "{datenow}" """)
            birthdayboystat = cur.fetchall()
            db.commit()

            birthday_boy_name = str(birthdayboystat[0][0])
            birthday_boy_surname = str(birthdayboystat[0][1])
            bot.send_message(chat_id=current_chat,
                             text=f"Сегодня день рождения у {birthday_boy_name} {birthday_boy_surname}")
            with open("Birthdaybot.log", "a") as logfile:
                logfile.write(f"{logdatenow}-бот был запущен\n")
                logfile.write(f"{datenow} - Сегодня день рождения у {birthday_boy_name} {birthday_boy_surname}\n")
        except:
            print(f"{datenow}-Сегодня событий нет")
            with open("Birthdaybot.log", "a") as logfile:
                logfile.write(f"{logdatenow}-бот был запущен\n")
                logfile.write(f"{logdatenow}----Сегодня событий нет\n")
allinfonow_iso = ""
"""АЛЕРТ ЗА 3 ДНЯ ДО ДР"""
def three_days_to_alert():
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

            input_for_tele_name = iso_birthday[name_indexation]

            input_for_tele_surname = iso_birthday[surname_indexation]

            allinfonow_iso += str(input_for_tele_name + " " + input_for_tele_surname + " " + converter_day_month(_) + "\n")






    if (datetime.strptime(isoconverted, '%Y-%m-%d') - timedelta(days=3)).strftime("%Y-%m-%d") == datetoseconds :
        bot.send_message(chat_id=current_chat,
                         text=f"НАПОМИНАНИЕ!!! у {input_for_tele_name} {input_for_tele_surname} через 3 дня день рождения")




    else:

        print(f"{datenow}-Сегодня событий нет")
        with open("Birthdaybot.log", "a") as logfile:

            logfile.write(f"{logdatenow}-бот был запущен\n")
            logfile.write(f"{logdatenow}----Сегодня событий нет\n")


    return allinfonow_iso

thread_alert = threading.Thread(target=alert)
thread_three_days_to_alert = threading.Thread(target=three_days_to_alert)
thread_alert.start()
thread_three_days_to_alert.start()








while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(1)


with open("Birthdaybot.log", "a") as logfile:
    logfile.write(f"{logdatenow}-бот отключился \n")

# allbirthday[input_for_tele_name],allbirthday[input_for_tele_surname],str(converter_day_month(_)









         #
         # if str(convert_into_iso(_)) == (logdatenow - timedelta(days=3)):
         #    bot.send_message(chat_id=current_chat,text=f'Напоминаем у {input_for_tele_name} {input_for_tele_surname} через 3 дня день рождения!')
         #
         #
         #
         #













# @bot.message_handler(commands=['dr'])
# def welcome(message):
#
#     namequestion = bot.send_message(message.chat.id,"Введите имя ")
#     bot.register_next_step_handler(namequestion,name_giver)
# def name_giver(message):
#
#     name = message.text
#     print(name)
#     print(message.text)
#     surnamequestion = bot.send_message(message.chat.id, "Введите фамилию")
#     bot.register_next_step_handler(surnamequestion, surname_giver)
#     return message.text
# def surname_giver(message):
#
#     surname = message.text
#     print(surname)
#     birthdayquestion = bot.send_message(message.chat.id, "Введите дату рождения в формате ГГГГ-ММ-ЧЧ")
#     bot.register_next_step_handler(birthdayquestion, birthday_giver)
# def birthday_giver(message):
#
#     birthday = message.text
#     print(birthday)
# name = None
# surname = None
# birthday = None