import os
from instagrapi import Client
#import config
import configparser # Library for reading from a configuration file, # pip install configparser

#config = configparser.ConfigParser() # Define the method to read the configuration file
#config.read('../config.ini') # read config.ini file


USERNAME = 'catsdodo_'
PASSWORD = 'aster226'

cl = Client()
before_ip = cl._send_public_request("https://api.ipify.org/")
print(f"Before: {before_ip}")
cl.login(USERNAME,PASSWORD)
cl.dump_settings('../login_sessions/session_' + USERNAME + ".json")
