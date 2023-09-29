import schedule
import os
from instagrapi import Client
import datetime # Library that we will need to get the day and time, # pip install datetime
import time 
from BotIG import BotIG

USERNAME = 'design.boi_'
PASSWORD = '195@asem777'

def doUnfoll():
    Bot = BotIG(USERNAME, PASSWORD)
    #user_fol = Bot.userFollowing()
    data = Bot.test()
    print(data)

doUnfoll()
Bot = BotIG(USERNAME, PASSWORD)
#user_fol = Bot.userFollowing()
data = Bot.test()
print(data)

data2 = Bot.test2()
print(data2)

data3 = Bot.userInfo()
print(data3)


