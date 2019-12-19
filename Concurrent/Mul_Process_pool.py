import multiprocessing
from time import sleep
from concurrent.futures import ProcessPoolExecutor


def normal(n):
    print("Hello")
    sleep(n)
    print("process Finished")


def daemonProcess():
    print("Daemon process started")
    while True:
        pass


def task(n):
    print(f"start Process: {n}")
    sleep(n)
    # print(f"Finish Process: {n}")
    return n


def main():
    m1 = multiprocessing.Process(target=normal, args=(3,))
    m2 = multiprocessing.Process(target=daemonProcess)
    m2.daemon = True
    m1.start()
    m2.start()
    m1.join()
    # m2.join()


def main_1():
    with multiprocessing.Pool(4) as p:
        p.apply(task, (4,))
        p.apply(task, (3,))
        p.apply(task, (2,))
        p.apply(task, (1,))


def main_1_async():
    with multiprocessing.Pool(4) as p:
        tasks = []
        for i in range(1, 5)[::-1]:
            ap = p.apply_async(func=task, args=(i,))
            tasks.append(ap)

        for gt in tasks:
            gt.wait()
            print(f"Result: {gt.get()}")


def map_aysc():
    lst = [4, 3, 2, 1]
    with multiprocessing.Pool(4) as p:
    #     res = p.map(task, lst)
    #     for it in p.imap(task, lst):
        for it in p.imap_unordered(task, lst):
            print(it)

    # with multiprocessing.Pool(4) as p:
    #     res = p.map_async(task, lst).get()
    # print(res)


def task2(x, y):
    print(f"start: ({x}, {y})")
    sleep(y)
    return x*y


def proc_starmap():
    with multiprocessing.Pool(4) as p:
        # p.map(task2, [2, 3])  # We can't pass two parameters
        res = p.starmap(task2, [(2, 3), (4, 2)])
    print(res)


def process_pool():
    with ProcessPoolExecutor(max_workers=4) as p:
        p.submit(task, (4))
        p.submit(task, (3))
        p.submit(task, (2))
        p.submit(task, (1))


if __name__ == "__main__":
    # main()
    # main_1()
    # process_pool()
    # main_1_async()
    # map_aysc()
    proc_starmap()
    print("All Finished")
