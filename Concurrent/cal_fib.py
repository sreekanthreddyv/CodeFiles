from time import sleep
from threading import Thread


def fib_num(n):
    if n <= 2:
        return 1
    else:
        return fib_num(n-1) + fib_num(n-2)


if __name__ == '__main__':
    n = 0

    def monitor():
        global n
        while True:
            sleep(1)
            print(f'{n} req/sec')
            n = 0


    Thread(target=monitor).start()
    while True:
        fib_num(1)
        n += 1

