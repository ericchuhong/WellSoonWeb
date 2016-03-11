#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chuhong Ma'

import orm,asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test5@example.com', passwd='1234567890',image='about:blank')
    # rs = await User.findAll(email='test1@example.com')
    # for i in range(len(rs)):
    #     print(rs[i])

    # await u.findAll()
    # print(u)
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))

__pool = orm.__pool
__pool.close()

loop.run_until_complete(__pool.wait_closed())

loop.close()
