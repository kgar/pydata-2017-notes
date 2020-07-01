# gen.py
import time

def compute():
    for i in range(10):
        time.sleep(.5)
        yield i

for i in compute():
    print(i)