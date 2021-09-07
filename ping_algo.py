import time
import sys
import os

def ping_every_x(lst,gap):
    try:
        while True:
            print('tick')
            time.sleep(gap)
    except KeyboardInterrupt:
        sys.exit(0)

ping_every_x([1,2,3],10)