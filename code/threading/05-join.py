import time
import threading


def myfunc(name):
    print(f"myfunc started with {name}")
    time.sleep(10)
    print("myfunc ended")

if __name__ == '__main__':
    print('main started')
    #myfunc('realpython')
    t=threading.Thread(target=myfunc, args=['realpython'])
    t.start()
    t.join()
    print('main ended')