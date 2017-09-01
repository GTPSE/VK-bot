# coding: utf-8

import vk_api
import random
import time
from path import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


login_={'me-bot1@yandex.ru':'226640411QWE', '+79126482524':'226640411', '+79506482524':'226640411','+79623240505':'18082017GTPSE'}


def read_stok():
    puti = os.path.abspath('stok.txt')
    with open(puti, 'r') as f:
        line = f.read()
    return  line.split()

def read_flud():
    puti = os.path.abspath('flud.txt')
    with open(puti, 'r') as f:
        line = f.read()
    return  line.split('.')

def vk_session(user, password):
    vk_session = vk_api.VkApi(user, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
    return vk_session.get_api()


def parser(new_mass, new_mass_id, col, vk):
    print('вызов парсера')

    # !!!мугут быть ошибки вызванные тем что пиршли сразу несколько сообщений от одного человека

    try:
        if str(new_mass['items'][col]['body']).lower()[0:6] == 'ответ ':
            print('перенаправляем сообщение')
            otvet = str(new_mass['items'][col]['body']).split(
                ';')  # парсим строку по точке запятой на две части, вторая с текстом
            response = vk.messages.send(user_id=otvet[0].split()[1], message=otvet[1])
            vk.messages.markAsRead(message_ids=new_mass_id)  # помечаем сообщение как прочитанное
            time.sleep(10)

        else:
            print('рассылаем уведомление о входящем сообщении')
            kon_otc = ['7257819', '47775818', '113536512']
            user_first_name = vk.users.get(user_ids=new_mass['items'][col]['user_id'])
            for n in kon_otc:
                time.sleep(10)
                response = vk.messages.send(user_id=n,
                                            message='https://vk.com/id{} пользователь {} с номером № {}, пишет: {}'.format(
                                                new_mass['items'][col]['user_id'],
                                                user_first_name[col]['first_name'],
                                                new_mass['items'][col]['user_id'],
                                                new_mass['items'][col]['body']))
            vk.messages.markAsRead(message_ids=new_mass_id)  # помечаем сообщение как прочитанное

    except:
        kon_otc = ['7257819', '47775818', '113536512']
        for n in kon_otc:
            time.sleep(10)
            response = vk.messages.send(user_id=n, message='Команда введена не верно')






def raed_messages(vk):
    while True:
    # проверяем есть ли новые сообщения у бота
        new_Dialogs = vk.messages.getDialogs(unread=1)  # получаем чаты с новыми сообщениятми
        if int(new_Dialogs['count']) > 0: # если количество новых сообщений > 0 читаем это сообщение
            for i in range(len(new_Dialogs['items'])):
                    new_mass_id = new_Dialogs['items'][i]['message']['id']
                    new_mass = vk.messages.getById(message_ids=new_mass_id)
                    for col in range(len(new_mass['items'])):
                        parser(new_mass, new_mass_id, col, vk)







def mane(user):
    print ('user =', user)
    password = login_[user]
    print ('password =', password)


    vk = vk_session(user, password)
    raed_messages(vk)


if __name__ == '__main__':
    stok = read_stok() # читаем спам базу
    flud = read_flud() # читаем войну и мир для для флуда между ботами
    pool = ThreadPool(len(login_)) # создаем пул из воркеров,  количество воркеров равно колличеству ботов
    pool.map(mane, login_)




