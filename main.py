import telebot
from telebot import types
import os
import random

wait = False
wait1 = False
wait_for_start = False

token = "8041543227:AAE36P70e5fBsfX14YOCsSfRZ3oxw12OkpA"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    a1 = str(message.from_user.id)
    if message.from_user.username == None:
        bot.send_message(message.from_user.id, "заведите себе 'юзернэйм'")
        a2 = message.from_user.first_name
    else:
        a2 = message.from_user.username
    a = "@" + a2 + " " + a1 + "\n"
    f = open('saves.txt', 'r')
    db = f.read()
    f.close()
    f = open('saves.txt', 'a')
    if not (a in db):
        f.write(a)
        f.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("создать комнату")
    btn1 = types.KeyboardButton("присоедениться к комнате")
    markup.add(btn, btn1)
    bot.send_message(message.from_user.id, "выберите кнопку", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def komnata(message):
    global wait, wait1, n, name, wait2, wait_for_start, proverkaa
    if message.text == "создать комнату":
        bot.send_message(message.from_user.id, "придумай название комнате")
        wait = True
        wait1 = False
    elif wait and not wait1:
        name = "komnata " + message.text + ".txt"
        komnaty = os.listdir()
        contunie = True
        for i in komnaty:
            print(i)
            if i == name:
                wait = False
                wait1 = False
                contunie = False
            else:
                continue
        if contunie == True:
            name_komnaty = open(name, "a")
            a1 = message.from_user.username
            a2 = message.from_user.id
            a = "@" + a1 + " " + str(a2) + "\n"
            name_komnaty.write(a)
            name_komnaty.close()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton("запустить тайного санту")
            markup.add(btn)
            bot.send_message(message.from_user.id, "комната успешно создана", reply_markup=markup)
            wait = False
            wait1 = False
        elif contunie == False:
            bot.send_message(message.from_user.id, "комната с таким именим уже есть")



    elif message.text == "присоедениться к комнате":
        bot.send_message(message.from_user.id, "введите название комнаты")
        wait = False
        wait1 = True
        komnaty = os.listdir()
        n = []
        for i in komnaty:
            n.append(i)
        print(n)

    elif wait1 and not wait:
        komnaty = os.listdir()
        join_in_room = "komnata " + message.text + ".txt"
        name = "komnata " + message.text + ".txt"
        a1 = message.from_user.username
        a2 = message.from_user.id
        cont = True
        a = "@" + a1 + " " + str(a2) + "\n"
        for i in n:
            if i == join_in_room:
                lines = open(join_in_room, "r")
                for line in lines:
                    #print(line)
                    if line == a:
                        wait1 = False
                        wait = False
                        cont = False
            wait1 = False
            wait = False
            wait2 = False
            for i in komnaty:
                #print(i)
                if i == join_in_room:
                    wait2 = True
        if cont and wait2:
            name_komnaty = open(name, "a")
            name_komnaty.write(a)
            name_komnaty.close()
            bot.send_message(message.from_user.id, "вы успешно присоеденились к комнате")
            wait1 = False
            wait = False
        elif not cont and wait2:
            bot.send_message(message.from_user.id, "вы уже есть в комнате")
            wait1 = False
            wait = False

    elif message.text == "запустить тайного санту":
        bot.send_message(message.from_user.id, "введи название комнаты которую ты хочешь запустить")
        wait_for_start = True

    elif wait_for_start:
        komnaty = os.listdir()
        name_proverki = "komnata " + message.text + ".txt"
        for i in komnaty:
            #print(i)
            if i == name_proverki:
                proverka = open(name_proverki, "r")
                if message.from_user.id == int(proverka.readline().split()[1]):
                    bot.send_message(message.from_user.id, "начинаю")
                    peremeshanie = random.randint(1, 10)
                    b = 0
                    while b < peremeshanie:
                        b += 1
                        bot.send_message(message.from_user.id, b)
        wait_for_start = False


bot.polling(none_stop=True)