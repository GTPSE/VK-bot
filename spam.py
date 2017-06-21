# -*- coding: utf8 -*-

import vk_api
import random
import time

otpr_otc = 0
notpr_otc = 0 
stok =[]
otpr = []
notpr = []
login_={'me-bot1@yandex.ru':'6607062017','me-bot2@yandex.ru':'6607062017'} 

def read_():
    f = open(r'C:\\2\\1\\stok.txt')
    line = f.read()
    return line.split()
    
def main():
    global stok
    global otpr
    global notpr
    global otpr_otc
    global notpr_otc
    for w in login_:
        otpr_otc = 0
        notpr_otc = 0
        vk_session = vk_api.VkApi(w, login_[w])
        try:
            vk_session.auth()
        except vk_api.AuthError as error_msg:
            print(error_msg)
        vk = vk_session.get_api()
        
        for t in range(15):
            try:
                time.sleep(random.randrange(1, 100))
                id_ = stok.pop(random.randrange(len(stok)-1)) 
                response = vk.messages.send(user_id=id_, message='Добрый день, предлагаю свои услуги, маникюр + покрытие всего 400 рублей??, подробности в моей группе: https://vk.com/svetipermyakova') 
                otpr += ['https://vk.com/id' + str(id_) + '\n']
                otpr_otc += 1
            except:
                notpr += ['https://vk.com/id' + str(id_) + '\n']
                notpr_otc +=1
                print ('сообщение не отправлено', id_)
                t -= 1
        
        mess = 'Добрый день, меня зовут {}, сегодня я отправил {} рекламных сообщений, у {} пользователей личка закрыта :((. В спам базе осталось {} контактов'.format (str(w), str(otpr_otc), str(notpr_otc), str(len(stok)))
        kon_otc = ['7257819', '47775818', '13662095']
        for n in kon_otc:
            response = vk.messages.send(user_id=n, message=mess)
        print ('Сообщения оправлены')

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


        
if __name__ == '__main__':
    stok = read_()
    main()
    write_()

    print ('Ok')