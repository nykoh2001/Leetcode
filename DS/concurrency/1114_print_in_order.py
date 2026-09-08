from threading import Lock, Condition


class Foo:
    def __init__(self):
        self.second_gate = Condition()
        self.third_gate = Condition()
        self.first_called = False
        self.second_called = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        with self.second_gate:
            self.second_gate.notify()
        self.first_called = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.second_gate:
            self.second_gate.wait_for(lambda: self.first_called)
        printSecond()
        self.second_called = True
        with self.third_gate:
            self.third_gate.notify()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.third_gate:
            self.third_gate.wait_for(lambda: self.second_called)
        printThird()
