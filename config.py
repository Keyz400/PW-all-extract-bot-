#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6780649862:AAFiQf2KDjfYDJgGV0PA-wtculRmZwWrLUw")
    API_ID = int(os.environ.get("API_ID", "27188447"))
    API_HASH = os.environ.get("API_HASH", "42a7205daefacde8e9ba22232deab028")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5985461381")
    

