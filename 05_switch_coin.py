#05_switch_coin.py
#This program uses a switch and both LEDS to simulate Heads/Tails on a coin

from rrb2 import *
import time

rr = RRB2()

while True:
    if rr.sw1_closed() == False:
        rr.set_led1(0)
        rr.set_led2(1)
    time.sleep(0.03)
    if rr.sw1_closed() == False:
        rr.set_led1(1)
        rr.set_led2(0)
    time.sleep(0.03)