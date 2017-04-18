import threading
from threading import Thread
import time

class AsyncWrite(Thread):
    def __init__(self, text, out):
        Thread.__init__(self)
        self.text = text;
        self.out = out;
        
    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print "Finished background file writing " + self.out

def main():
    message = raw_input ("Enter a string to store:")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print "The program can continue to run while it writes in another thread"
    print 100 + 200

    background.join()
    print "Waited until thread was complete"

main()
                
