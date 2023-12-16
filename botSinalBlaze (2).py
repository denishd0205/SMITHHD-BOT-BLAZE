import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from time import sleep
import requests



driver = uc.Chrome()
driver.get('https://blaze-4.com/pt ')
sleep(5)

    


#Mensagens Padrao
analise = ''
win = '🔰𝗚𝗥𝗘𝗘𝗡 𝗦𝗘𝗠 𝗚𝗔𝗟𝗘🔰 '
win_branco = '🔰⚪️𝗕𝗥𝗔𝗡𝗖𝗢 𝟭𝟰𝗫⚪️🔰'
loss = '❌ 𝘽𝙊𝙍𝘼𝙍 𝙍𝙀𝘾𝙐𝙋𝙀𝙍𝘼𝙍 '
nao_confirmacao = ''
##############################

def esperar():
    while True:
        try:
            driver.find_element(By.CLASS_NAME,'time-left').find_element(By.TAG_NAME,'span').text
            break
        except:
            pass
    
    while True:
        try:
            driver.find_element(By.CLASS_NAME,'time-left').find_element(By.TAG_NAME,'span').text
        except:
            break
        
def retornar_historico():
    return [i['color'] for i in requests.get('https://blaze-4.com/api/roulette_games/recent').json()][::-1]

            
def retornar_ultimo():
    return requests.get('https://blaze-4.com/api/roulette_games/current').json()['color']

def martin_gale(gale,ultimo):
    enviar_mensagem(gale)
    esperar()
    sleep(1.5)
    ultimo_ = retornar_ultimo()
    if ultimo_ != ultimo and ultimo_ != 0:
        enviar_mensagem(win)
        return True
    elif ultimo_ == 0: 
        enviar_mensagem(win_branco)
        return True
            
def enviar_mensagem(mensagem):
    bot_token = '6634308277:AAGV20f6ZwJe7N81vkD631yAHwDaWZ-XLRg'
    chat_id = '-4085097999'
    url_blaze = ''
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={mensagem}\n{url_blaze}&parse_mode=Markdown'
    requests.get(url)


cor = ['⚪','⚫','🔴']
simbolo = ['⚪','⚫','🔴']


print('ATENTOS ...')
enviar_mensagem('⚪𝗕𝗢𝗧 𝗟𝗜𝗚𝗔𝗗𝗢 𝗔𝗧𝗘𝗡𝗖𝗔𝗢⚪ ...')
while True:
    try:
        print('ok')
        esperar()
        sleep(1.5)
        historico = retornar_historico()
        ultimo = retornar_ultimo()
        historico.append(ultimo)
        padrao = historico[-3:]
        print(padrao)
        confirmacao = f'{simbolo[padrao[0]]} 𝗘𝗡𝗧𝗥𝗔 𝗡𝗢 {cor[padrao[0]]}\n{simbolo[0]} 𝙋𝙍𝙊𝙏𝙀𝘾𝘼𝙊 𝙉𝙊 𝘽𝙍𝘼𝙉𝘾𝙊'
        gale1 = f' \n{simbolo[padrao[0]]} {cor[padrao[0]]}\n{simbolo[0]} 𝙋𝙍𝙊𝙏𝙀𝘾𝘼𝙊 𝙉𝙊 𝘽𝙍𝘼𝙉𝘾𝙊'
        gale2 = f' \n{simbolo[padrao[0]]} {cor[padrao[0]]}\n{simbolo[0]} 𝙋𝙍𝙊𝙏𝙀𝘾𝘼𝙊 𝙉𝙊 𝘽𝙍𝘼𝙉𝘾𝙊'

        
        
        #Como as estratégias sempre jogam na cor contraria, resolvi colocar as cores
        #Vermelha e Preta em indices diferentes para aproveirar a logica
        if padrao ==[1,2,2] or padrao == [2,1,1] or padrao == [2,1,1] or padrao == [0,2,1] or padrao == [1,1,2]:       
            enviar_mensagem(analise)
            esperar()
            sleep(1.5)
            ultimo = retornar_ultimo()
            while True:
                if ultimo == padrao[0]:
                    enviar_mensagem(confirmacao)
                    esperar()
                    sleep(1.5)
                    ultimo_ = retornar_ultimo()
                    if ultimo_ != ultimo and ultimo_ != 0:
                        enviar_mensagem(win)
                        break
                    elif ultimo_ == 0:
                        enviar_mensagem(win_branco)
                        break
                
                    enviar_mensagem(loss)
                                      
                else:
                    enviar_mensagem(nao_confirmacao)
                    break
    except Exception as e:
        print(e)
        driver.get(' https://blaze-3.com/pt/games/double ')
        sleep(10)
        pass
        