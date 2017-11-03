# coding: utf-8

import vk_api
import random
import time
from path import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


login_={'me-bot1@yandex.ru':'226640411QW3', '+79126482524':'226640411@', '+79506482524':'226640411@@'}
login_2={'me-bot1@yandex.ru':'226640411QWE', '+79126482524':'226640411@', '+79506482524':'226640411@','+79623240505':'18082017GTPSE2'}
bot_ID = ['442125906', '442123798', '432166514', '436034900']

def read_stok():
    with open(r'D:\\VK-bot\\stok.txt', 'r') as f:
        line = f.read()
    return  line.split()

def read_flud():
    with open(r'D:\\VK-bot\\flud.txt', 'r') as f:
        line = f.read()
    return  line.split('.')

def error(ex):
    print ('Возникла следующая ошибка:', ex)
    try:
        with open(r'D:\\VK-bot\\error.txt', 'a') as f:
            f.write(str(ex) + '/n')
    except:
        with open(r'D:\\VK-bot\\error.txt', 'w') as f:
            f.write(str(ex) + '/n')


def vk_session(user, password):
    vk_session = vk_api.VkApi(user, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
    return vk_session.get_api()


def message(imia):
    first = ['{} здравствуйте, ', '{} добрый день, ', '{} день добрый, ', 'Приветствую {}, ', '{} приветсвую ']
    second = [
        'меня зовут Светлана, я  мастер ногтевого сервиса и хотела бы предложить Вам свои услуги. ',
        'меня зовут Светлана, я начинающий мастер ногтевого сервиса. В первую очередь я заинтересована в постоянных клиентах, поэтому за демократичную цену я предлагаю качественные услуги и не экономлю на материалах. ',
        'меня зовут Светлана, я делаю маникюр на дому в районе Щорса - Московская. ',
        'меня зовут Светлана, я делаю маникюр на дому и хотела бы предложить Вам свои услуги. '
        'Я начинающий мастер ногтевого сервиса и хотела бы предложить Вам свои услуги. '
        'Я мастер ногтевого сервиса, в первую очередь я заинтересована в постоянных клиентах, поэтому за демократичную цену я делаю качественный маникюр. '
    ]
    third = ['Маникюр + покрытие всего 400 рублей👍, подробности в моей группе: https://vk.com/svetipermyakova',
             'Маникюр + покрытие всего 400 рублей👍, с прайсом, а также с моими работами вы можете ознакомиться в группе: https://vk.com/svetipermyakova',
             'С моими работами вы можете ознакомиться в группе: https://vk.com/svetipermyakova, маникюр + покрытие всего 400 рублей👍',
             'Большинство своих работ я выкладываю в своей группе: https://vk.com/svetipermyakova, там же вы можете ознакомиться со стоимостью моих услуг. Маникюр + покрытие всего 400 рублей👍.'
             ]

    fourth = [' Если вам не интересно мое предложение пожалуйста не отправляйте его в спам']

    message_ = first[random.randrange(len(first))].format(imia[0]['first_name']) + second[
        random.randrange(len(second))] + third[random.randrange(len(third))] + fourth[0]

    return message_

def write_():
    global notpr
    with open(r'D:\\VK-bot\\stok.txt', 'w') as f:
        for i in stok:
            f.write(
                str(i) + '\n'
            )
    with open(r'D:\\VK-bot\\otpr.txt', 'a') as f:
        for o in otpr:
            f.write(
                str(o)
            )
    with open(r'D:\\VK-bot\\notpr.txt', 'a') as f:
        for p in notpr:
            f.write(
                    str(p)
                    )

def main(vk, user):
    global stok
    global otpr
    global notpr
    global otpr_otc
    global notpr_otc
    global message_
    t = 0
    while t < 15:
        #        for t in range(15):
        try:
            time.sleep(random.randrange(20, 100))
            id_ = stok.pop(
                random.randrange(len(stok) - 1))  # случайным образом выбираем человека для отправки сообщения
            imia = vk.users.get(user_id=id_, name_case='nom')
            vk.messages.send(user_id=id_, message=message(imia))
            otpr += ['https://vk.com/id' + str(id_) + '\n']
            otpr_otc += 1
            t += 1
        except Exception as ex:
            error(ex)
            notpr += ['https://vk.com/id' + str(id_) + '\n']
            notpr_otc += 1
            print('сообщение не отправлено', id_)
            kon_otc = ['7257819', '47775818', '13662095'] 
            mess_err= 'Возникла следующая ошибка =' + str(ex)
            for n in kon_otc:
                time.sleep(random.randrange(10, 20))
                vk.messages.send(user_id=n, message=mess_err)


    # необходимо отправить отчет от имени робота
    mess = 'Добрый день, меня зовут {}, сегодня я отправил {} рекламных сообщений, у {} пользователей личка закрыта :((. В спам базе осталось {} контактов'.format(
        str(user), str(otpr_otc), str(notpr_otc), str(len(stok)))
    kon_otc = ['7257819', '47775818', '13662095']
    for n in kon_otc:
        time.sleep(random.randrange(10, 20))
        vk.messages.send(user_id=n, message=mess)
    print('Сообщения оправлены')

def send(vk, new_mass_id, user):
    global stok
    print ('запускаем спам')
    kon_otc = ['7257819', '47775818']
    for n in kon_otc:
        time.sleep(random.randrange(10, 20))
        vk.messages.send(user_id=n, message='Запущена рассылка спама')
    main(vk, user)
    write_()
    vk.messages.markAsRead(message_ids=new_mass_id)
    print('Ok')



def parser(new_mass, new_mass_id, vk, user, mass_user):
    print('вызов парсера')

    # !!!мугут быть ошибки вызванные тем что пиршли сразу несколько сообщений от одного человека

    try:
        if str(new_mass.lower()[0:6]) == 'ответ ':
            print('перенаправляем сообщение')
            otvet = new_mass.split(';')  # парсим строку по точке запятой на две части, вторая с текстом
            vk.messages.send(user_id=otvet[0].split()[1], message=otvet[1])
            time.sleep(random.randrange(1, 2))


        elif str(new_mass).lower() == 'старт':
                send(vk, new_mass_id, user)

        else:
            print('рассылаем уведомление о входящем сообщении')
            kon_otc = ['7257819', '47775818', '113536512']
            user_first_name = vk.users.get(user_ids=mass_user)
            for n in kon_otc:
                time.sleep(random.randrange(1, 3))
                vk.messages.send(user_id=n,
                                            message='https://vk.com/id{} пользователь {} с номером № {}, пишет: {}'.format(
                                                mass_user,
                                                user_first_name[0]['first_name'],
                                                mass_user,
                                                new_mass))


    except Exception as ex:
        error(ex)
        kon_otc = ['7257819', '47775818', '113536512']
        ms_err = 'Возникла следующая ошибка: ' + str(ex)
        for n in kon_otc:
            time.sleep(10)
            response = vk.messages.send(user_id=n, message=ms_err)






def raed_messages(vk, user):
    # проверяем есть ли новые сообщения у бота
    new_Dialogs = vk.messages.get(count=100)  # получам последние 100 сообщений
    for t in reversed(new_Dialogs['items']):
        if t['read_state'] == 0:
            new_mass_id = t['id']
            new_mass = t['body']
            mass_user = t['user_id']
            if bot_ID.count(str(mass_user)) != 0: # проверяем от кого сообщение
                                                     # если от ота то не реагируем
                vk.messages.markAsRead(message_ids=new_mass_id)  # помечаем сообщение как прочитанное
            else:
                parser(new_mass, new_mass_id, vk, user, mass_user)
                vk.messages.markAsRead(message_ids=new_mass_id)  # помечаем сообщение как прочитанное


# рассылаем флуд между ботами
def flud(vk):
    time.sleep(random.randrange(7, 10))
    try:
        global fluds
        global bot_ID
        bots_id = vk.users.get()
        bot_ID_flud = []
        for e in bot_ID:
            if str(e) != str(bots_id[0]['id']): bot_ID_flud.append(e)
        message_flud = str(fluds[random.randrange(len(fluds))])
        messege_in_bot_ID = str(bot_ID_flud[random.randrange(len(bot_ID_flud))])
        vk.messages.send(user_id=messege_in_bot_ID, message=message_flud)
    except:
        print ('messege_in_bot_ID =', messege_in_bot_ID)
        print ('message_flud =', message_flud)






# запускаем тело функции в бесконечном цикле
def mane(user):
    password = login_[user]
    vk = vk_session(user, password)
    while True:
       time.sleep(random.randrange(7, 10))
       raed_messages(vk, user) # роверяем новые сообщения
       time.sleep(random.randrange(7, 10))
       flud(vk) # рассылаем флуд между ботами


if __name__ == '__main__':
    print ('Поехали!!!')
    otpr = []
    notpr = []
    notpr_otc = 0
    otpr_otc = 0
    stok = read_stok() # читаем спам базу
    fluds = read_flud() # читаем войну и мир для для флуда между ботами
    pool = ThreadPool(len(login_)) # создаем пул из воркеров,  количество воркеров равно колличеству ботов
    pool.map(mane, login_)
# просто так



