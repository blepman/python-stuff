#!/usr/bin/env python3
from time import strftime, sleep
def clock_24h(interval: int=5):
    def _time():
        while True:
            try:
                if int(strftime("%S")) % interval == 0:
                    print("\r", strftime("%H:%M:%S"), end="")
                    sleep(interval)
                else:
                    print("\r", f"{interval} sec update.", end="")
                    sleep(0.1)
            except:
                print("\r", strftime("%H:%M:%S"), end="")
                sleep(5)
    return str(_time())
