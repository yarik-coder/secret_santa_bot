import telebot
from telebot import types
import os

wait = False
wait1 = False
wait_for_start = False

token = ""
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
    f = open('saves.txt', 'a', encoding='utf-8')
    if not (a in db):
        f.write(a)
        f.close()

    spisok = []
    komnaty = os.listdir()
    komnaty_new = []
    for i in komnaty:
        if i.split()[0] == "komnata":
            komnaty_new.append(i)
    for i in komnaty_new:
        komnaty_admina = open(i, "r", encoding="UTF-8")
        if message.from_user.id == int(komnaty_admina.readline().split()[1]):
            spisok.append(i)
            komnaty_admina.close()
        else:
            komnaty_admina.close()
    if not spisok:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("создать комнату")
        btn1 = types.KeyboardButton("присоединиться к комнате")
        markup.add(btn, btn1)
        bot.send_message(message.from_user.id, "выберите кнопку", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("создать комнату")
        btn1 = types.KeyboardButton("присоединиться к комнате")
        btn2 = types.KeyboardButton("админ панель")
        markup.add(btn, btn1, btn2)
        bot.send_message(message.from_user.id, "выберите кнопку", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def komnata(message):
    global wait, wait1, n, name, wait2, wait_for_start, proverkaa, wait_comment, a, cont, wait_comment_admin, comment, result_comment, wait_admin_panel, show_people, delete_people, delete_people2, komnata_for_de, switch_name, switch_name2, komnata_switch_name
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
                wait_admin_panel = False
                wait = False
                wait1 = False
        bot.send_message(message.from_user.id, "если хочешь ты можешь добавить комментарий к подарку")
        bot.send_message(message.from_user.id, "если ты не хочешь добавлять комментарий просто поставь '.'")

    elif message.text == "присоединиться к комнате":
        bot.send_message(message.from_user.id, "введите название комнаты")
        wait = False
        wait1 = True
        komnaty = os.listdir()
        n = []
        for i in komnaty:
            n.append(i)
        print(n)
        wait_comment_admin = False
        wait_admin_panel = False

    elif message.text == "админ панель":
        wait_admin_panel = True
        bot.send_message(message.from_user.id, "введи название комнаты")
        wait_comment_admin = False
        wait_comment = False
        show_people = False
        delete_people = False
        delete_people2 = False
        switch_name = False
        switch_name2 = False

    elif message.text == "показать участников":
        show_people = True
        switch_name = False
        wait_comment_admin = False
        wait_comment = False
        wait_for_start = False
        wait_admin_panel = False
        delete_people = False
        delete_people2 = False
        spisok = []
        komnaty = os.listdir()
        komnaty_new = []
        for i in komnaty:
            if i.split()[0] == "komnata":
                komnaty_new.append(i)
        print(komnaty_new)
        for i in komnaty_new:
            komnaty_admina = open(i, "r", encoding="UTF-8")
            if message.from_user.id == int(komnaty_admina.readline().split()[1]):
                spisok.append(i)
                komnaty_admina.close()
            else:
                komnaty_admina.close()

        bot.send_message(message.from_user.id, "ваши комнаты")
        for i in spisok:
            bot.send_message(message.from_user.id, str(i))
        bot.send_message(message.from_user.id, "введите комнату у который хотите узнать пользователей")

    elif message.text == "выйти из панели админа":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("создать комнату")
        btn1 = types.KeyboardButton("присоединиться к комнате")
        btn2 = types.KeyboardButton("админ панель")
        markup.add(btn, btn1, btn2)
        bot.send_message(message.from_user.id, "админ панель закрыта", reply_markup=markup)

    elif message.text == "переименовать комнату":
        switch_name = True
        delete_people = False
        delete_people2 = False
        show_people = False
        wait_comment_admin = False
        wait_comment = False
        wait_for_start = False
        wait_admin_panel = False
        spisok = []
        komnaty = os.listdir()
        komnaty_new = []
        for i in komnaty:
            if i.split()[0] == "komnata":
                komnaty_new.append(i)
        print(komnaty_new)
        for i in komnaty_new:
            komnaty_admina = open(i, "r", encoding="UTF-8")
            if message.from_user.id == int(komnaty_admina.readline().split()[1]):
                spisok.append(i)
                komnaty_admina.close()
            else:
                komnaty_admina.close()

        bot.send_message(message.from_user.id, "ваши комнаты")
        for i in spisok:
            bot.send_message(message.from_user.id, str(i))
        bot.send_message(message.from_user.id, "введите название комнаты которую хотите переименовать")

    elif message.text == "удалить участника":
        delete_people = True
        delete_people2 = False
        switch_name = False
        show_people = False
        wait_comment_admin = False
        wait_comment = False
        wait_for_start = False
        wait_admin_panel = False
        spisok = []
        komnaty = os.listdir()
        komnaty_new = []
        for i in komnaty:
            if i.split()[0] == "komnata":
                komnaty_new.append(i)
        for i in komnaty_new:
            komnaty_admina = open(i, "r", encoding="UTF-8")
            if message.from_user.id == int(komnaty_admina.readline().split()[1]):
                spisok.append(i)
                komnaty_admina.close()
            else:
                komnaty_admina.close()

        bot.send_message(message.from_user.id, "ваши комнаты")
        for i in spisok:
            bot.send_message(message.from_user.id, str(i))
        bot.send_message(message.from_user.id, "введите название комнаты где хотите удалить участника")

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
            btn1 = types.KeyboardButton("создать комнату")
            btn2 = types.KeyboardButton("присоединиться к комнате")
            btn3 = types.KeyboardButton("админ панель")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, "комната успешно создана", reply_markup=markup)
            wait = False
            wait1 = False
            contunie = False
        elif contunie == False:
            bot.send_message(message.from_user.id, "комната с таким именим уже есть")
            contunie = False

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
                        wait_comment = False
            wait1 = False
            wait = False
            wait2 = False
            for i in komnaty:
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

    elif show_people:
        if message.text.split()[0] == "komnata":
            komnata = message.text
        else:
            komnata = "komnata " + message.text + ".txt"
        people = open(komnata, "r", encoding="UTF-8")
        lines = people.readlines()
        id_users = []
        us_users = []
        for line in lines:
            id_users.append(line.split()[1])
            us_users.append(line.split()[0])
        receivers = us_users[1:] + [us_users[0]]
        for i in range(len(us_users)):
            bot.send_message(message.from_user.id, receivers[i])
        show_people = False

    elif delete_people:
        if message.text.split()[0] == "komnata":
            komnata_for_de = message.text
        else:
            komnata_for_de = "komnata " + message.text + ".txt"
        people = open(komnata_for_de, "r", encoding="UTF-8")
        lines = people.readlines()
        id_users = []
        us_users = []
        for line in lines:
            id_users.append(line.split()[1])
            us_users.append(line.split()[0])
        receivers = us_users[1:] + [us_users[0]]
        for i in range(len(us_users)):
            bot.send_message(message.from_user.id, receivers[i])
        bot.send_message(message.from_user.id, "введите юзернейм участника которого хотите удалить")
        delete_people2 = True
        delete_people = False

    elif delete_people2:
        spisok = []
        people = message.text
        f = open(komnata_for_de, "r", encoding="UTF-8")
        for i in f:
            if i.split()[0] != people:
                spisok.append(i)
        f1 = open(komnata_for_de, "w", encoding="UTF-8")
        print(spisok)
        for e in spisok:
            f1.write(e)
        bot.send_message(message.from_user.id, "человек успешно удалён")
        delete_people2 = False

    elif switch_name:
        if message.text.split()[0] == "komnata":
            komnata_switch_name = message.text
        else:
            komnata_switch_name = "komnata " + message.text + ".txt"
        komnaty_to_switch_name = os.listdir()
        bot.send_message(message.from_user.id, "введи новое имя для комнаты")
        switch_name2 = True
        switch_name = False

    elif switch_name2:
        if message.text.split()[0] == "komnata":
            new_name = message.text
        else:
            new_name = "komnata " + message.text + ".txt"
        os.rename(komnata_switch_name, new_name)
        bot.send_message(message.from_user.id, f"комната {komnata_switch_name} была переименована в {new_name}")
        switch_name2 = False

    elif wait_admin_panel:
        komnaty_p_n_a_p = os.listdir()
        proverka_prav = "komnata " + message.text + ".txt"
        for i in komnaty_p_n_a_p:
            if i == proverka_prav:
                proverka_p_n_a_p = open(proverka_prav, "r", encoding="UTF-8")
                if message.from_user.id == int(proverka_p_n_a_p.readline().split()[1]):
                    proverka_p_n_a_p.close()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton("показать участников")
                    btn2 = types.KeyboardButton("удалить участника")
                    btn3 = types.KeyboardButton("запустить тайного санту")
                    btn4 = types.KeyboardButton("переименовать комнату")
                    btn5 = types.KeyboardButton("выйти из панели админа")
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.from_user.id, "права подтверждены", reply_markup=markup)

    elif message.text == "запустить тайного санту":
        bot.send_message(message.from_user.id, "введи название комнаты которую ты хочешь запустить")
        wait_for_start = True
        wait_admin_panel = False

    elif wait_for_start:
        komnaty = os.listdir()
        name_proverki = "komnata " + message.text + ".txt"
        for i in komnaty:
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
        wait_for_start = False

    else:
        bot.send_message(message.from_user.id, "не понял вашей комнады")

bot.polling(none_stop=True)