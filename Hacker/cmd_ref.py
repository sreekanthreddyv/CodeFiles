import queue
import timeit
from collections import deque
from time import sleep
from concurrent.futures import ThreadPoolExecutor


FIFO = queue.Queue()
LIFO = queue.LifoQueue()

# FIFO.task_done()

PQ = queue.PriorityQueue()
PQ.put((1, 'eat'))
# PQ.join()
PQ.get()
PQ.task_done()

g = deque()
g.append(2)
g.appendleft(3)
g.pop()
g.popleft()
g.insert(2, 5)
g.extend(range(1, 5))
print(g)
g.rotate(2)  # right
print(g)
g.rotate(-3)  # left
print(g)

t = timeit.default_timer()


def func_1():
    print("func_1 executing")
    sleep(2)
    print("func_1 Completed")


t1 = timeit.Timer("func_1()", setup="from __main__ import func_1")
print(t1)
times = t1.repeat(repeat=2, number=1)
# "repeat" to determine how many times we want to time our code
# "number" to determine how many times we want to run these tests.
print(times)


class Timer:

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = timeit.default_timer

    def __enter__(self):
        self.start = self.timer()
        return self

    def __exit__(self, *args):
        end = self.timer()
        self.elapsed_sec = end - self.start
        self.elapsed = self.elapsed_sec * 1000  # milliseconds
        if self.verbose:
            print(f"elapsed time {self.elapsed_sec}")


with Timer(verbose=True):
    func_1()

executor = ThreadPoolExecutor(max_workers=2)
task1 = executor.submit(Timer)
