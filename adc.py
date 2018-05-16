import requests
import time
from bs4 import BeautifulSoup as bs
import random
from random import getrandbits

session = requests.session()

print ("[" + (time.strftime("%H:%M:%S")) + "]" + " ############################################")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " #               ADC ACC GEN                #")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " #          Developed by @mxnnxt            #")
print ("[" + (time.strftime("%H:%M:%S")) + "]" + " ############################################\n")


times = int(input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the number of accounts you would like: ")))
domain = input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter your domain (ex: domain.com): "))
password = input("[" + (time.strftime("%H:%M:%S") + "]" + " - Enter the password you would like: "))

text_file = open("Accounts.txt", "w")

headers = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, br",
	"Accept-Language":"en-US,en;q=0.9",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Content-Type":"application/x-www-form-urlencoded",
	"Host":"www.adidas.com",
	"Origin":"https://www.adidas.com",
	"Referer":"https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def create():
	global session
	global email

	url1 = "https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MiAccount-Register/"

	r1 = session.get(url1, headers=headers)

	soup1 = bs(r1.text,"html.parser")
	inputs1 = soup1.find_all("input",{"name":"dwfrm_mipersonalinfo_securekey"})
	sec1 = inputs1[0]["value"]
	#print(sec1)

	end1 = soup1.find_all("form",{"id":"dwfrm_mipersonalinfo"})
	p1 = end1[0]["action"]
	url_end1 = p1.split("Register/")[1]
	#print(url_end1)

	url2 = url1+url_end1

	names = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]

	firstName = names[random.randint(0, 99)]
	lastName = names[random.randint(0, 99)]


	payload1 = {
		'dwfrm_mipersonalinfo_firstname': firstName, 
		'dwfrm_mipersonalinfo_lastname': lastName,
		'dwfrm_mipersonalinfo_customer_birthday_dayofmonth': "7",
		'dwfrm_mipersonalinfo_customer_birthday_month': "10",
		'dwfrm_mipersonalinfo_customer_birthday_year': "1995",
		'dwfrm_mipersonalinfo_step1': 'Next', 
		'dwfrm_mipersonalinfo_securekey': sec1

	}

	r2 = session.post(url2,headers=headers,data=payload1)
	time.sleep(1/2)

	soup2 = bs(r2.text,"html.parser")
	inputs2 = soup2.find_all("input",{"name":"dwfrm_milogininfo_securekey"})
	sec2 = inputs2[0]["value"]
	#print(sec2)

	end2 = soup2.find_all("form",{"id":"dwfrm_milogininfo"})
	p2 = end2[0]["action"]
	url_end2 = p2.split("Register/")[1]
	#print(url_end2)

	url3 = url1+url_end2

	headers2 = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	'Upgrade-Insecure-Requests': '1',
	'Host': 'www.adidas.com',
	'Origin': 'https://www.adidas.com',
	'Referer': url2

	}
    

	email = (names[random.randint(0, 99)] + "{}" + "@"+domain).format(getrandbits(40)) 

	payload2 = {
   	'dwfrm_milogininfo_email': email,
   	'dwfrm_milogininfo_password': password,
   	'dwfrm_milogininfo_newpasswordconfirm': password,
   	'dwfrm_milogininfo_step2': 'Next',
   	'dwfrm_milogininfo_securekey': sec2
   	}

	r3 = session.post(url3, headers=headers2, data=payload2)
	time.sleep(1/2)
	print("[" + (time.strftime("%H:%M:%S")) + "]" + " - CREATING ACCOUNT . . . ")


	soup3 = bs(r3.text,"html.parser")
	inputs3 = soup3.find_all("input",{"name":"dwfrm_micommunicinfo_securekey"})
	sec3 = inputs3[0]["value"]

	end3 = soup3.find_all("form",{"id":"dwfrm_micommunicinfo"})
	p3 = end3[0]["action"]
	url_end3 = p3.split("Register/")[1]

	url4 = url1 + url_end3

	headers2 = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	'Upgrade-Insecure-Requests': '1',
	'Host': 'www.adidas.com',
	'Origin': 'https://www.adidas.com',
	'Referer': url2

	}

	payload3 = {
	'dwfrm_micommunicinfo_agreeterms': 'true',
	'dwfrm_micommunicinfo_step3': 'Register',
	'dwfrm_micommunicinfo_securekey': sec3
	}

	r4 = session.post(url4, headers=headers2, data=payload3)
	time.sleep(1/2)

	if 'justRegistered=true' in r4.text:
		print("[" + (time.strftime("%H:%M:%S")) + "]" + " - SUCCESSFULLY CREATED ACCOUNT: "+email+":"+password)
		write()
		return email , password
	else:
		print("[" + (time.strftime("%H:%M:%S")) + "]" + " - FAILED TO CREATE ACCOUNT ")
	
def write():

    text_file.write(email + ":" + password + "\n")

for i in range (times):
    create()

