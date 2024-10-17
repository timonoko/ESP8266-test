from machine import WDT
import time
def hui():
    c=1
    wdt=WDT()
    while True:
        print(c)
        wdt.feed()
        time.sleep(c)
        c=c+0.1
 
