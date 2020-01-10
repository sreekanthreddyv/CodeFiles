import asyncio


async def myCoroutine():
    print("Simple event loop example")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myCoroutine())
    loop.close()


# /* Run Forever */
@asyncio.coroutine
def hello_world():
    yield from asyncio.sleep(1)
    print("Hello World")
    asyncio.async(hello_world())


@asyncio.coroutine
def good_evening():
    yield from asyncio.sleep(1)
    print("Good Evening")
    asyncio.async(good_evening())


print("step: asyncio.get_event_loop()")


def forever():
    loop = asyncio.get_event_loop()
    try:
        print("step: loop.run_until_complete()")
        asyncio.async(hello_world())
        asyncio.async(good_evening())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Step: loop.close()")
        loop.close()


async def mycor():
    print("My Coroutine")


async def main():
    await asyncio.sleep(1)


loop = asyncio.get_event_loop()
try:
    loop.create_task(mycor())
    loop.create_task(mycor())
    loop.create_task(mycor())
    pending = asyncio.Task.all_tasks()
    print(pending)
    loop.run_until_complete(main())
finally:
    loop.close()

# if __name__ == "__main__":
#     main()
