
# coding: utf-8

import vk_api
import random
import time

otpr_otc = 0 # счетчик колличесва отправленных сообщений
notpr_otc = 0 # счетчик не отправленных сообщений
stok =[]
otpr = []
notpr = []
login_=login_={'+79126482524':'226640411@9', '+79623240505':'159987@'}
'''
'me-bot1@yandex.ru':'226640411QW4'
'''
bot_id = {'me-bot1@yandex.ru':'34244GTPSE', 'me-bot2@yandex.ru':432445894}
vk = []
def read_():
    f = open(r'C:\\2\\1\\stok.txt')
    line = f.read()
    return line.split()

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

def send(vk, new_mass_id):
    global stok
    print ('запускаем спам')
    kon_otc = ['7257819', '47775818']
    for n in kon_otc:
        time.sleep(random.randrange(10, 20))
        vk.messages.send(user_id=n, message='Запущена рассылка спама')
    stok = read_()
    main(vk)
    write_()
    vk.messages.markAsRead(message_ids=new_mass_id)
    print('Ok')




def main(vk):
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

def write_():
    global otpr
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



def parser(new_mass, new_mass_id, user):
    print ('вызов парсера')

# !!!мугут быть ошибки вызванные тем что пиршли сразу несколько сообщений от одного человека
    
    try:
        if str(new_mass['items'][0]['body']).lower()[0:6] == 'ответ ':
            print ('перенаправляем сообщение')
            otvet = str(new_mass['items'][0]['body']).split(';') # парсим строку по точке запятой на две части, вторая с текстом
            response = vk.messages.send(user_id = otvet[0].split()[1], message = otvet[1])
            vk.messages.markAsRead(message_ids = new_mass_id) # помечаем сообщение как прочитанное 
            time.sleep(10) 
        
        else:
            print ('рассылаем уведомление о входящем сообщении')
            kon_otc = ['7257819', '47775818', '113536512']
            user_first_name = vk.users.get(user_ids = new_mass['items'][0]['user_id'])
            for n in kon_otc:
                time.sleep(10)
                response = vk.messages.send(user_id=n, message='https://vk.com/id{} пользователь {} с номером № {}, пишет: {}'.format (new_mass['items'][0]['user_id'],
                                                                                                                                       user_first_name[0]['first_name'],
                                                                                                                                       new_mass['items'][0]['user_id'],
                                                                                                                                       new_mass['items'][0]['body']))
            vk.messages.markAsRead(message_ids = new_mass_id) # помечаем сообщение как прочитанное 

    except:
        kon_otc = ['7257819', '47775818', '113536512']
        for n in kon_otc:
            time.sleep(10)
            response = vk.messages.send(user_id=n, message='Команда введена не верно')                
                
                
if __name__ == '__main__':
    print ('Поехали!!!')
	# создаем сессию (подключение)

    while True:
        for user in login_:
            otpr_otc = 0
            notpr_otc = 0
            vk_session = vk_api.VkApi(user, login_[user])
            try:
                vk_session.auth()
            except vk_api.AuthError as error_msg:
                print(error_msg)
            vk = vk_session.get_api()
            time.sleep(random.randrange(40, 60))
        # проверяем есть ли новые сообщения у ботов
        #    ts_ = vk.messages.getLongPollServer(need_pts = 1)
            new_Dialogs = vk.messages.getDialogs(unread = 1) # получаем чаты с новыми сообщениятми
            if int(new_Dialogs['count'])>0:
                for i in range(len(new_Dialogs['items'])):
                    new_mass_id = new_Dialogs['items'][i]['message']['id']
                    new_mass = vk.messages.getById (message_ids = new_mass_id)
                    if str(new_mass['items'][0]['body']).lower() == 'старт' : send(vk, new_mass_id)
                    elif int(new_mass['items'][0]['out']) == 0:
                        parser(new_mass, new_mass_id, user)




