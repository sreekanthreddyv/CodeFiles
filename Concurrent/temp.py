from collections import deque


def countdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = deque()
tasks.extend([countdown(10), countdown(5), countdown(6)])
print(tasks)


def run():
    while tasks:
        task = tasks.popleft()
        try:
            x = next(task)
            print(x)
            tasks.append(task)
        except StopIteration:
            print("Task")


if __name__ == "__main__":
    run()
