import threading
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, URLError, urljoin, urlopen


def task():
    print("Executing task")
    result = 0
    for i in range(10):
        result += i
    print(f"res: {result}")
    print(f"Task Executed: {threading.current_thread()}")


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    _ = executor.submit(task)
    _ = executor.submit(task)


def hacker(n):
    from functools import reduce
    res = reduce(lambda x, y: x * y, range(1, n + 1))
    print(f'Factorial: {res}')
    return res


lst = [5, 6, 8, 3, 4, 9]
with ThreadPoolExecutor(max_workers=4) as executor:
    op = executor.map(hacker, lst)
print(op)

if __name__ == "__main__":
    main()

with ThreadPoolExecutor(max_workers=4) as executor:
    task1 = executor.submit(task)
    # executor.shutdown(wait=True) cannot schedule new futures after shutdown
    task2 = executor.submit(task)


def one(n):
    print(f"Executing task {n}")
    time.sleep(n)
    print(f"Finished task {n}")


with ThreadPoolExecutor(max_workers=2) as executor:
    tst = executor.submit(one, (1)).result(timeout=2)
    print(tst)
    # t1 = executor.submit(one, (1))  # .add_done_callback(hacker)
    # t2 = executor.submit(one, (2))
    # t3 = executor.submit(one, (3))
    # t4 = executor.submit(one, (4))

    # t3.cancel()  # t3 will not run


URLS = [
    'http://www.google.com',
    'http://www.pymotw.com',
    # 'http://camunxbld27.europe.root.pri/',
    'http://py-tips.herokuapp.com/'
]


def checkStatus(url):
    print(f"attempting to crawl {url}")
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)
    return response.getcode(), url


def printStatus(status):
    print(f"URL Crawled with status code: {status}")


def main():
    tasks = []
    with ThreadPoolExecutor(max_workers=4) as exe:
        for url in URLS:
            task = exe.submit(checkStatus, (url))
            tasks.append(task)

    for res in as_completed(tasks):
        printStatus(res.result(timeout=None))


def taskDone(fn):
    if fn.cancelled():
        print(f"our {fn.arg} Future has been cancelled")
    else:
        print("our task has been completed")


def main():
    print("Starting ThreadPool")
    with ThreadPoolExecutor(max_workers=3) as ece:
        task1 = ece.submit(one, (1))
        task2 = ece.submit(one, (5))
        task1.add_done_callback(taskDone)
        task2.add_done_callback(taskDone)
        task2.cancel()

    print("All task completed")


if __name__ == "__main__":
    main()
