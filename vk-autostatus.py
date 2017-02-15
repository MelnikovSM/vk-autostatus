# UTF-8 Issue Fix
# -*- coding: utf-8 -*-
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')

# Config
token='' # VK Access Token
# https://oauth.vk.com/authorize?client_id=3697615&scope=status,account,messages,offline&response_type=token
delay=300 # delay in seconds
status_strings = [
'Unable initialize reconnection - internal issue: This service activity disabled by internal functioning policy.', # internal thought en_US
'Невозможно инициализировать переподключение - внутренняя ошибка: Активность этой службы отключена внутренней политикой функционирования.', # internal thought en_US
'root@MSMHSF:~ $ rm -rf /*', # internal thought POSIX
'Stop, turn, take a look around..  At all of the Lights And Sounds.. Let them bring you in.', # Yellowcard - Lights And Sounds
'I\'ve got a way to work this out, I got a way and you know how', # Yellowcard - Lights And Sounds
'Me Against The World!', # Simple Plan - Me Against The World
'You`re my Playmate Of The Year (но это неточно!).', # # Zebrahead - Playmate Of The Year + Disclaimer
'I am where I am\nI\'m only here cause I want to be.', # Zebrahead - I Am
'Но это неточно.', # Big Russian Boss famous quote
'Busy writing thoughts tonight. A message sent with no reply.', # Yellowcard - Hide
'Yellowcard, Zebrahead, Blink-182, Simple Plan are best music bands!', # my opinion about best music bands
'2017: Rest in peace, Yellowcard :(', # Rest in pleace, Yellowcard :(
'Invinsible, earthquake, powerful', # Skillet - Feel Invinsible
'Another reckless holiday.. Another brain cell floats away.. I\'ve had enough, please wake me up ...if I\'m dreaming', # Zebrahead - Dissatisfied
'Don\'t worry everything\'s gonna be alright, alright, alright.. Dissatisfied', # Zebrahead - Dissatisfied
'Под оболочкой идут процессы, сутками, идут рассчёты. Я понимаю, что с этой системой врят ли свести мне счеты.', # Yellow Socks - Тонкая грань
'Rise! Rise! Rise in revolution! Rise! Rise in revolution! Rise!', # Skillet - Rise
'Hell Yeah!', # Zebrahead - Hell Yeah & I Am
'I\'m a nightmare, a disaster. That\'s what they always said. I\'m a lost cause, not a hero..But I\'ll make it on my own.. Me against the world!', # Simple Plan - Me Against The World
'TLS://Where_Tangents_Meet', # WTM Enforce
'TLS://Siren`s_Lament', # SL Enforce
'True_Love_Story://Where_Tangents_Meet', # For dumb
'True_Love_Story://Siren`s_Lament', # Again, for dumb
'Fell in love with <Person name hidden> (Но это не точно!)' # Bila ne bila
] # Populate this array with your own status strings

# Code

import vk
from time import sleep
from random import randint
vkapi=vk.API(vk.Session(access_token=token), v='5.53', lang='ru', timeout=20)

oldStatusString=vkapi.status.get()['text']
print('Total '+str(len(status_strings))+' status strings defined.\nStarting status update with delay '+str(delay)+' seconds..')
try:
	while True:
		print('Updating status..')
		try: vkapi.status.set(text=status_strings[randint(0, (len(status_strings)-1))])
		except vk.exceptions.VkAPIError:
			print('VK Issue, status not updated')
			vkapi.messages.send(user_id=vkapi.users.get()[0]['id'],message='Status updater issue')
			pass
		sleep(delay)
except KeyboardInterrupt: 
	print('Shutdown initiated, restoring original status..')
	vkapi.status.set(text=oldStatusString)
