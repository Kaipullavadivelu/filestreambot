import logging
import os
import time
import random
import string
import subprocess
import requests

from dotenv import load_dotenv

load_dotenv('config.env')

def getConfig(name: str):
    return os.environ[name]

StartTime = time.time()

try:
    SHORTENER = getConfig('SHORTENER')
    SHORTENER_API = getConfig('SHORTENER_API')
    if len(SHORTENER) == 0 or len(SHORTENER_API) == 0:
        raise KeyError
except KeyError:
    SHORTENER = None
    SHORTENER_API = None
