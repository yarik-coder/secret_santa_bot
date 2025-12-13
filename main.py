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
    if message.from_user.username == "Soundof_water":
        bot.send_message(message.from_user.id, "привет катя)")
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
    global wait, wait1, n, name, wait2, wait_for_start, proverkaa, wait_comment, a, cont, wait_comment_admin, comment, result_comment
    result_comment = ""
    if message.text == "создать комнату":
        bot.send_message(message.from_user.id, "придумай название комнате")
        wait = True
        wait1 = False
        wait_comment = False
    elif wait and not wait1:
        name = "komnata " + message.text + ".txt"
        komnaty = os.listdir()
        contunie = False
        for i in komnaty:
            print(i)
            if i == name:
                wait = False
                wait1 = False
                contunie = False
            else:
                wait_comment_admin = True
                wait = False
                wait1 = False
        bot.send_message(message.from_user.id, "если хочешь ты можешь добавить комментарий к подарку")
        bot.send_message(message.from_user.id, "если ты не хочешь добавлять комментарий просто поставь '.'")

    elif wait_comment_admin:
        if message.text == ".":
            comment = "у пользователя нет комментариев"
            wait2 = True
            contunie = True
            wait_comment_admin = False
        else:
            comment = message.text
            wait2 = True
            contunie = True
            wait_comment_admin = False

        if contunie == True:
            name_komnaty = open(name, "a", encoding="UTF-8")
            a1 = message.from_user.username
            a2 = message.from_user.id
            a = "@" + a1 + " " + str(a2) + " " + comment + "\n"
            name_komnaty.write(a)
            name_komnaty.close()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton("запустить тайного санту")
            markup.add(btn)
            bot.send_message(message.from_user.id, "комната успешно создана", reply_markup=markup)
            wait = False
            wait1 = False
            contunie = False
        elif contunie == False:
            bot.send_message(message.from_user.id, "комната с таким именим уже есть")
            contunie = False



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
        a = "@" + a1 + " " + str(a2) + " "
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
                    wait_comment = True
        bot.send_message(message.from_user.id, "если хочешь ты можешь добавить комментарий к подарку")
        bot.send_message(message.from_user.id, "если ты не хочешь добавлять комментарий просто поставь '.'")

    elif wait_comment:
        if message.text == ".":
            a = a + "у пользователя нет комментариев" + "\n"
            wait2 = True
            wait_comment = False
        else:
            a = a + message.text + "\n"
            print("пошло")
            wait2 = True
            wait_comment = False


        if cont and wait2:
            name_komnaty = open(name, "a", encoding="utf-8")
            name_komnaty.write(a)
            name_komnaty.close()
            bot.send_message(message.from_user.id, "вы успешно присоеденились к комнате")
            wait1 = False
            wait = False
            cont = False
            wait2 = False
        elif not cont and wait2:
            bot.send_message(message.from_user.id, "вы уже есть в комнате")
            wait1 = False
            wait = False
            cont = False
            wait2 = False

    elif message.text == "запустить тайного санту":
        bot.send_message(message.from_user.id, "введи название комнаты которую ты хочешь запустить")
        wait_for_start = True


    elif wait_for_start:
        pon = 0
        komnaty = os.listdir()
        name_proverki = "komnata " + message.text + ".txt"
        for i in komnaty:
            #print(i)
            if i == name_proverki:
                proverka = open(name_proverki, "r",  encoding="UTF-8")
                if message.from_user.id == int(proverka.readline().split()[1]):
                    proverka.close()
                    proverka = open(name_proverki, "r",  encoding="UTF-8")
                    bot.send_message(message.from_user.id, "начинаю")
                    lines = proverka.readlines()
                    liness = 0
                    for line in lines:
                        liness += 1
                    liness -= 1
                    peremeshanie = random.randint(1, liness)
                    proverka.close()
                    proverka = open(name_proverki, "r",  encoding="UTF-8")
                    lines1 = proverka.readlines()
                    id_users = []
                    us_users = []
                    comment_users = []
                    for line in lines1:
                        parts = line.strip().split()
                        id_users.append(parts[1])
                        us_users.append(parts[0])
                        comment_users.append(parts[2::])
                        print(parts[2:])
                    print(us_users, id_users, comment_users)
                    receivers = us_users[1:] + [us_users[0]]
                    receivers_comment = comment_users[1:] + [comment_users[0]]
                    for i in range(len(us_users)):
                        bot.send_message(id_users[i], f"🎅 ты даришь {receivers[i]}")
                        for e in receivers_comment[i]:
                            result_comment = result_comment + e + " "
                        bot.send_message(id_users[i], f"комментарий пользователя: {result_comment}")
                        result_comment = ""
                        print(id_users[i], f"🎅 ты даришь {receivers[i]}")

                        print(id_users[i], f"комментарий пользователя {receivers_comment[i]}")


                    '''
                    for n in lines:
                        idd = linessss.split()[pon]
                        bot.send_message(idd, "ты даришь подарок " + linesss.split()[peremeshanie - pon])
                        print(linessss.split()[pon] + " ты даришь подарок " + linesss.split()[peremeshanie - pon])
                        pon += 1'''







        wait_for_start = False




bot.polling(none_stop=True)