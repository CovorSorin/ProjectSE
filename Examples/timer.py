import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print "Timer: " + name + " started\n"
    tLock.acquire()
    print "Name " + name + " has aquired the lock"
    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1
    print name + " is releasing the lock"
    tLock.release()
    print "Timer: " + name + " completed"

def main():
    t1 = threading.Thread(target = timer, args = ("Thread 1", 1, 5))
    t2 = threading.Thread(target = timer, args = ("Thread 2", 2, 5))
    t1.start()
    t2.start()

    print "Main Complete"

main()
