import threading

class ThreadInstance(threading.Thread):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        while True:
            print(self.getName() + "thread is running")
            pass
        pass
    pass

thread1 = ThreadInstance()
thread1.start()

thread2 = ThreadInstance()
thread2.start()

thread3 = ThreadInstance()
thread3.start()
