import telebot
import webbrowser
import sqlite3
from telebot import types
import datetime

months = {
"января": 1,
"февраля": 2,
"марта": 3,
"апреля": 4,
"мая": 5,
"июня": 6,
"июля": 7,
"августа": 8,
"сентября": 9,
"октября": 10,
"ноября": 11,
"декабря": 12
}





bot = telebot.TeleBot('7027598404:AAFiF8XYzjvgceMrg_MvMG9W0Lpp_9OSyd0')#токенбота
current_chat = "-1002004314793"

@bot.message_handler(commands=["start","начать","стартуй","стартануть","new"])#будем обрабытывать команды "start","начать","стартуй","стартануть","new" и отвечать на них описанием чо мы умеем как бы говоря
def description(message):
    with open("description.txt","r" , encoding="utf-8") as description_file:
        bot.send_message(message.chat.id, description_file.read() )


day_now = str(datetime.datetime.now().day)
month_now=str(datetime.datetime.now().month)
datenow = (f"{month_now}-{day_now}")
logdatenow = datetime.datetime.now()

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
    if allbirthday.index(_) % 3 == 0 and allbirthday.index(_) != 0 :
        print(_)












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