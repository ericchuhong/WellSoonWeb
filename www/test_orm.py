
import asyncio

import aiomysql

loop = asyncio.get_event_loop()

@asyncio.coroutine
def go():
    # async with create_pool(host='127.0.0.1',port=3306,
    #                        user='www-data',password='www-data',
    #                        db='awesome',loop=loop) as pool:
        # async with pool.get() as conn:
        #     async with conn.cursor() as cur:
        #         await cur.execute("SELECT * FROM users;")
        #         value = await cur.fetchall()
        #         print(value)
    pool = yield from aiomysql.create_pool(host='127.0.0.1',port=3306,user='www-data',password='www-data',db='awesome',loop=loop)
    with (yield from pool) as conn:
        cur = yield from conn.cursor()
        yield from cur.execute("SELECT * FROM users")
        (r,) = yield from cur.fetchall()
        print(r)
    pool.close()
    yield from pool.wait_closed()

loop.run_until_complete(go())