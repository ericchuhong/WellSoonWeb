#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chuhong Ma'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from config import configs
from coroweb import get, post

from models import User, Comment, Blog, next_id

COOKIE_NAME = 'awesession'
__COOKIE_KEY = configs.session.secret

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'user': users
    }