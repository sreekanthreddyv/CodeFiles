from pycsp.parallel import *
from time import sleep


@process
def proess_1(n):
    print("Executng process-1")
    sleep(n)
    print("Execution finished proc_1")


@process
def process_2(n):
    print("Executing process-2")
    sleep(n)
    print("Execution finished proc_2")


Parallel(proess_1(3), process_2(2))
print("Finished")