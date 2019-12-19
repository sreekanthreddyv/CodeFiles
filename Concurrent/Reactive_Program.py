from rx.core import Observer
from rx import Observable, create


def push_five_strings(observer):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()


class PrintObserver(Observer):

    def on_next(selfself, value):
        print(f"Received {value}")

    def on_completed(self) -> None:
        print("Done!")

    def on_error(self, error: Exception) -> None:
        print(f"Error {error} Occurred")


source = create(push_five_strings())

source.subscribe(PrintObserver())

