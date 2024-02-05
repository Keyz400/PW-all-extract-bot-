#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6780649862:AAFiQf2KDjfYDJgGV0PA-wtculRmZwWrLUw")
    API_ID = int(os.environ.get("API_ID", "27344176"))
    API_HASH = os.environ.get("API_HASH", "d1712cc190dc99572be1a96d8b0f4f9e")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5985461381")
    

