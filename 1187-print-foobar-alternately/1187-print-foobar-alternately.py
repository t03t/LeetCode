from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.barLock = Lock()
        self.fooLock.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.barLock.acquire()
            printFoo()
            self.fooLock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.fooLock.acquire()
            printBar()
            self.barLock.release()
