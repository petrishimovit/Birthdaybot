import telebot
import webbrowser
import sqlite3
from telebot import types
import datetime
from datetime import datetime, timedelta, date

day_now = str(datetime.now().day)
month_now=str(datetime.now().month)
datenow = (f"{month_now}-{day_now}")
logdatenow = str(date.today())
datetoseconds = datetime.now()




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


    year = 2024

    # Возвращаем дату в формате ГГГГ-ММ-ДД
    return f"{year}-{day:02d}-{month:02d}"



db_birthday = []

allinfo_db = ""
allinfo = ""


bot = telebot.TeleBot('7027598404:AAGkSY5MIScCcBXI8YUQxZRJ-_5SU-Bqs34')#токенбота
current_chat = "-1002004314793"



"""ОБРАБОТКА КОМАНДЫ START"""
@bot.message_handler(commands=["start","начать","стартуй","стартануть","new"])
def description(message):
    with open("description.txt","r" , encoding="utf-8") as description_file:
        bot.send_message(message.chat.id, description_file.read() )



"""ОБРАБОТКА КОМАНДЫ INFO"""
@bot.message_handler(commands=["info","information","i"])
def info(message):
    with open("info.txt","r" , encoding="utf-8") as info_file:
        bot.send_message(message.chat.id, info_file.read() )




"""ОБРАБОТКА КОМАНДЫ DATA"""
@bot.message_handler(commands=["date","data","d"])
def info(message):
    bot.send_message(message.chat.id, f"Сегодня {logdatenow}" )





"""ФУНКЦИЯ ЧТОБЫ В ДЕНЬ РОЖДЕНИЯ ПРИСЫЛАТЬ АЛЕРТ"""
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



with sqlite3.connect("Banya_birthday_database.db") as db:
    allbirthday = ["start"]
    cur = db.cursor()
    cur.execute("""SELECT * FROM banya """)
    allbirthday_sqlite = cur.fetchall()
    for i in allbirthday_sqlite:
        for n in i:
            allbirthday.append(n)
for _ in allbirthday:


    if allbirthday.index(_) % 3 == 0 and allbirthday.index(_) != 0:


        allbirthday[allbirthday.index(_)] = str(converter_day_month(_))


        input_for_tele_name = allbirthday.index(str(converter_day_month(_))) - 1


        input_for_tele_surname = allbirthday.index(str(converter_day_month(_))) - 2



        allinfonow = allbirthday[input_for_tele_name] + " " + allbirthday[input_for_tele_surname] + " " + str(
                converter_day_month(_))

        allinfo += f"{allinfonow}\n"



"""ОБРАБОТКА КОМАНДЫ GETBIRTHDAY"""
@bot.message_handler(commands=["get","getbirthdays"])
def getbirthday_checker(message):
    bot.send_message(chat_id=current_chat, text=allinfo)








# allbirthday[input_for_tele_name],allbirthday[input_for_tele_surname],str(converter_day_month(_)





db_birthday = []
allinfo_db = ""
def convert_into_iso(date_str):
    day, month = date_str.split('-')


    day = int(day)
    month = int(month)


    year = 2024

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

        indexation = iso_birthday.index(_)
        surname_indexation = indexation - 1
        name_indexation = indexation - 2
        isoconverted = str(convert_into_iso(_))


        iso_birthday[indexation] = convert_into_iso(_)
        three_days_earlier_for_alert = datetime.strptime(isoconverted, '%Y-%m-%d') - timedelta(days=3)
        if datetoseconds == three_days_earlier_for_alert:
            bot.send_message(chat_id=current_chat,text=f"НАПОМИНАНИЕ ! через 3 дня день рождения у {name_indexation} {surname_indexation } ")



        # date_early_alert = date_for_early - timedelta(days=3)

        # print(iso_birthday.index(_))+6

        # input_for_tele_name = iso_birthday.index(indexation)


        input_for_tele_name = iso_birthday[name_indexation]
        #
        input_for_tele_surname = iso_birthday[surname_indexation]
        #
        allinfonow_iso = str(input_for_tele_name + " " + input_for_tele_surname+ " " + isoconverted)

         #
         #
         # if str(convert_into_iso(_)) == (logdatenow - timedelta(days=3)):
         #    bot.send_message(chat_id=current_chat,text=f'Напоминаем у {input_for_tele_name} {input_for_tele_surname} через 3 дня день рождения!')
         #
         #
         #
         #













bot.polling(none_stop=True)


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