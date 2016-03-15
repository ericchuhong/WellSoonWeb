#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chuhong Ma'

' url handlers '

import re, json, logging, hashlib, base64, asyncio
import time


from config import configs
from coroweb import get, post

from models import User, Comment, Blog, next_id

COOKIE_NAME = 'awesession'
__COOKIE_KEY = configs.session.secret

@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary,created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]


    # users = await User.findAll()
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }