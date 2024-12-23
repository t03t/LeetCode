from threading import Lock
class Foo:
    def __init__(self):
        self.firstJob = Lock()
        self.secondJob = Lock()
        self.firstJob.acquire()
        self.secondJob.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJob.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstJob:
            printSecond()
            self.secondJob.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondJob:
            printThird()
        