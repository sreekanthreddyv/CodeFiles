import threading
import queue
from time import sleep


def mySubscriber(que):
    while not que.empty():
        item = que.get()
        if item is None:
            break
        print(f"{threading.current_thread()} removed {item} from the queue")
        que.task_done()
        sleep(1)


# myQueue = queue.LifoQueue()
myQueue = queue.Queue()
for val in range(1, 10):
    myQueue.put(val)

pq = queue.PriorityQueue()

for i, val in enumerate(['eat', 'code', 'sleep'], 1):
    pq.put((i, val))

for i, val in enumerate(['code', 'eat', 'sleep'], 1):
    pq.put((i, val))

print("Queue is Populated")

threads = []
for _ in range(4):
    thr = threading.Thread(target=mySubscriber, args=(pq,))
    threads.append(thr)
    threads[-1].start()

# for th in threads:
#     th.join()

pq.join()
print("Queue is Empty")
