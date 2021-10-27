import time
import concurrent.futures as cf


def myfunc(name):
    print(f"myfunc started with {name}")
    time.sleep(10)
    print(f"myfunc ended with {name}")

if __name__ == '__main__':
    print('main started')
    with cf.ThreadPoolExecutor(max_workers=3) as tp:
        tp.map(myfunc,['foo','bar','baz'])
    print('main ended')