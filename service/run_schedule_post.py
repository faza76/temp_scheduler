# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:29:43 2023

@author: Kakak
"""

import schedule
import os
import pathlib
from instagrapi import Client
import pandas as pd
import datetime # Library that we will need to get the day and time, # pip install datetime
import time 
from BotIG import BotIG

USERNAME = 'catsdodo_'
PASSWORD = 'aster226'

SHEET_ID = "16VQ9rnyTLZXVdrZI8wau1pZDtJz2F9joRzD6TOolkuU"
SHEET_NAME = "post_material"

def doPostPhoto(path):
    try:
        Bot = BotIG(USERNAME, PASSWORD)
        print("login succeed")
        #user_fol = Bot.userFollowing()
        Bot.post_photo(path)
        print("Success Post")
        os.remove(path)
        print("file removed")
    except:
        print("error")
        
def doPostVideo(path):
    try:
        Bot = BotIG(USERNAME, PASSWORD)
        print("login succeed")
        #user_fol = Bot.userFollowing()
        capt = getPostConfig()
        Bot.post_video(path,capt)
        print("Success Post")
        os.remove(path)
        print("file removed")
    except:
        print("error")
        
        
def getPostConfig():
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
    df = pd.read_csv(url)
    conf = df[df['account'] == "catsdodo_"]
    capt = conf["captions"].item()
    return capt
    
        
def checking_material_post():
    files = [f for f in pathlib.Path().glob("../media/design.boi_/*.jpg")]
    
    if len(files) > 0:
        doPostPhoto(files[0])
    else:
        print("none post material")
        
def checking_material_video():
    files = [f for f in pathlib.Path().glob("../media/catsdodo_/*.mp4")]

    if len(files) > 0:
        doPostVideo(files[0])
    else:
        print("none post material")


#Bot = BotIG(USERNAME, PASSWORD)
#schedule.every().minutes.do(checking_material_post)
schedule.every().minutes.do(checking_material_video)

while True:
    schedule.run_pending()
    time.sleep(1)


