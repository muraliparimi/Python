import threading

rlock = threading.RLock()
rlock.acquire()
rlock.acquire()
print(threading.current_thread())
print(rlock)