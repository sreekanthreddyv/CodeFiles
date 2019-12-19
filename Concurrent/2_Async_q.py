import asyncio
import random
import time


@asyncio.coroutine
def newProducer(myque):
    while True:
        yield from myque.put(random.randint(2, 10))
        yield from asyncio.sleep(1)


@asyncio.coroutine
def newConsumer(myque):
    while True:
        articleId = yield from myque.get()
        print(f"New reader consumed the article {articleId}")


myQueue = asyncio.Queue()

loop = asyncio.get_event_loop()

loop.create_task(newProducer(myQueue))
loop.create_task(newConsumer(myQueue))
try:
    loop.run_forever()
finally:
    loop.close()




