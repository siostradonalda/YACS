from threading import Timer
from threading import Thread

DELAY_SECONDS = 5.0

def hello():
    print('Timer Thread')
    Timer(DELAY_SECONDS, hello).start()


class MyThread(Thread):
    def run(self):
        print('hello')


t1 = MyThread()
t1.start()

t = Timer(DELAY_SECONDS, hello)
t.start()

print('Main Thread')
