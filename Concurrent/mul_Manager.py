import multiprocessing as mp
import queue


def myProcess(ns):
    # Update values with inout namespace
    print(ns.x)
    ns.x = 2


def mySharedQueue(qu):
    value = qu.get()
    print(f"{mp.current_process()} is poped out {value} from the shared queue")
    qu.task_done()


def main():
    manager = mp.Manager()
    ns = manager.Namespace()
    ns.x = 1
    print(ns)
    process = mp.Process(target=myProcess, args=(ns,))
    process.start()
    process.join()
    print(ns)


def main():
    m = mp.Manager()
    sharedque = m.Queue()
    sharedque.put(2)
    sharedque.put(3)
    sharedque.put(4)
    p = []
    for val in range(1, 4):
        p1 = mp.Process(target=mySharedQueue, args=(sharedque, ))
        p1.start()
        p.append(p1)

    for v in p:
        v.join()




if __name__ == "__main__":
    main()
