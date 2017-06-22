
# coding: utf-8

# In[ ]:

import vk_api
import random
import time

otpr_otc = 0 # счетчик колличесва отправленных сообщений
notpr_otc = 0 # счетчик не отправленных сообщений
stok =[]
otpr = []
notpr = []
login_={'me-bot1@yandex.ru':'6607062017bot','me-bot2@yandex.ru':'6607062017'}
bot_id = {'me-bot1@yandex.ru':432166514, 'me-bot2@yandex.ru':432445894}
vk = []

def send(vk):
    print ('запускаем спам')

def parser(new_mass, new_mass_id, w):
    print ('вызов парсера')
    print (new_mass['items'][0]['body'])

    
    try:
        if str(new_mass['items'][0]['body']).lower()[0:6] == 'ответ ':
            print ('перенаправляем сообщение')
            otvet = str(new_mass['items'][0]['body']).split(';') # парсим строку по точке запятой на две части, вторая с текстом
            response = vk.messages.send(user_id = otvet[0].split()[1], message = otvet[1])
            vk.messages.markAsRead(message_ids = new_mass_id) # помечаем сообщение как прочитанное 
            time.sleep(10) 
        
        else:
            print ('рассылаем уведомление о входящем сообщении')
            kon_otc = ['7257819', '47775818', '13662095', '113536512']
            for n in kon_otc:
                time.sleep(10)
                response = vk.messages.send(user_id=n, message='Пользователь {}, пишет: {}'.format (new_mass['items'][0]['user_id'], new_mass['items'][0]['body']))
            vk.messages.markAsRead(message_ids = new_mass_id) # помечаем сообщение как прочитанное 

    except:
        kon_otc = ['7257819', '47775818', '13662095', '113536512']
        for n in kon_otc:
            time.sleep(10)
            response = vk.messages.send(user_id=n, message='Команда введена не верно')                
                
                
if __name__ == '__main__':                                     
    while True:
        time.sleep(60)                      
        # создаем сессию (подключение)
        for w in login_:
            otpr_otc = 0
            notpr_otc = 0
            vk_session = vk_api.VkApi(w, login_[w])
            try:
                vk_session.auth()
            except vk_api.AuthError as error_msg:
                print(error_msg)
            vk = vk_session.get_api()

            # проверяем есть ли новые сообщения у ботов
        #    ts_ = vk.messages.getLongPollServer(need_pts = 1)
            new_Dialogs = vk.messages.getDialogs(unread = 1) # получаем чаты с новыми сообщениятми 
            if int(new_Dialogs['count'])>0:
                for i in range(len(new_Dialogs['items'])):
                    new_mass_id = new_Dialogs['items'][i]['message']['id']
                    new_mass = vk.messages.getById (message_ids = new_mass_id)
                    if str(new_mass['items'][0]['body']) == 'start' : send(w)
                    elif int(new_mass['items'][0]['out']) == 0:
                        parser(new_mass, new_mass_id, w)



        


# In[ ]:



