# coding: utf-8

import vk_api
import random
import time
from path import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


login_={'me-bot1@yandex.ru':'226640411QWE', '+79126482524':'226640411', '+79623240505':'18082017GTPSE'}
login_2={'me-bot1@yandex.ru':'226640411QWE', '+79126482524':'226640411', '+79506482524':'226640411','+79623240505':'18082017GTPSE'}
bot_ID = ['4421259060', '442123798', '432166514', '436034900']

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
             'Большинство своих работ я выкладываю в своей группе: https://vk.com/svetipermyakova, там же вы можете ознакомиться со стоимостью моих услуг. Маникюр + покрытие всего 400 рублей👍.']

    message_ = first[random.randrange(len(first))].format(imia[0]['first_name']) + second[
        random.randrange(len(second))] + third[random.randrange(len(third))]

    return message_

def write_():
    global notpr
    with open(r'C:\\2\\1\\stok.txt', 'w') as f:
        for i in stok:
            f.write(
                str(i) + '\n'
            )
    with open(r'C:\\2\\1\\otpr.txt', 'a') as f:
        for o in otpr:
            f.write(
                str(o)
            )
    with open(r'C:\\2\\1\\notpr.txt', 'a') as f:
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
        except:
            notpr += ['https://vk.com/id' + str(id_) + '\n']
            notpr_otc += 1
            print('сообщение не отправлено', id_)

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
    main(vk)
    write_()
    vk.messages.markAsRead(message_ids=new_mass_id)
    print('Ok')



def parser(new_mass, new_mass_id, col, vk, user):
    print('вызов парсера')

    # !!!мугут быть ошибки вызванные тем что пиршли сразу несколько сообщений от одного человека

    try:
        if str(new_mass['items'][col]['body']).lower()[0:6] == 'ответ ':
            print('перенаправляем сообщение')
            otvet = str(new_mass['items'][col]['body']).split(
                ';')  # парсим строку по точке запятой на две части, вторая с текстом
            response = vk.messages.send(user_id=otvet[0].split()[1], message=otvet[1])

            time.sleep(random.randrange(10, 20))

        elif str(new_mass['items'][col]['body']).lower() == 'старт':
            send(vk, new_mass_id, user)

        else:
            print('рассылаем уведомление о входящем сообщении')
            kon_otc = ['7257819', '47775818', '113536512']
            user_first_name = vk.users.get(user_ids=new_mass['items'][col]['user_id'])
            for n in kon_otc:
                time.sleep(random.randrange(10, 20))
                response = vk.messages.send(user_id=n,
                                            message='https://vk.com/id{} пользователь {} с номером № {}, пишет: {}'.format(
                                                new_mass['items'][col]['user_id'],
                                                user_first_name[col]['first_name'],
                                                new_mass['items'][col]['user_id'],
                                                new_mass['items'][col]['body']))


    except:
        kon_otc = ['7257819', '47775818', '113536512']
        for n in kon_otc:
            time.sleep(10)
            response = vk.messages.send(user_id=n, message='Команда введена не верно')






def raed_messages(vk, user):
    # проверяем есть ли новые сообщения у бота
    new_Dialogs = vk.messages.getDialogs(unread=1)  # получаем чаты с новыми сообщениятми
    if int(new_Dialogs['count']) > 0: # если количество новых сообщений > 0 читаем это сообщение
        for i in range(len(new_Dialogs['items'])):
                new_mass_id = new_Dialogs['items'][i]['message']['id']
                new_mass = vk.messages.getById(message_ids=new_mass_id)
                print (new_mass)
                print (new_mass_id)
                for col in range(len(new_mass['items'])):
                    parser(new_mass, new_mass_id, col, vk, user)
        vk.messages.markAsRead(message_ids=new_mass_id)  # помечаем сообщение как прочитанное


# рассылаем флуд между ботами
def flud(vk):
    global fluds
    message_flud = str(fluds[random.randrange(len(fluds))])
    messege_in_bot_ID = str(bot_ID[random.randrange(len(bot_ID))])
    vk.messages.send(user_id=messege_in_bot_ID, message=message_flud)







# запускаем тело функции в бесконечном цикле
def mane(user):
    password = login_[user]
    vk = vk_session(user, password)
    while True:
        raed_messages(vk, user) # роверяем новые сообщения
 #       flud(vk) # рассылаем флуд между ботами


if __name__ == '__main__':
    print ('Поехали!!!')
    stok = read_stok() # читаем спам базу
    fluds = read_flud() # читаем войну и мир для для флуда между ботами
    pool = ThreadPool(len(login_)) # создаем пул из воркеров,  количество воркеров равно колличеству ботов
    pool.map(mane, login_)




