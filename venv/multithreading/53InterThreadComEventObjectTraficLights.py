from threading import *
import time


def trafficpolice():
    while True:
        time.sleep(10)
        print("Traffic Police Giving GREEN Signal")
        event.set()
        print("Traffic Police sleeping")
        time.sleep(20)
        print("Traffic Police Giving RED Signal")
        event.clear()


def driver():
    num = 0
    while True:
        print("Drivers waiting for GREEN Signal -> Event is set:", event.isSet())
        event.wait()
        print("Traffic Signal is GREEN...Vehicles can move -> Event is set:", event.isSet())
        while event.isSet():
            num = num + 1
            print("Vehicle No:", num, "Crossing the Signal")
            time.sleep(2)
        print("Traffic Signal is RED...Drivers have to wait")


event = Event()
t1 = Thread(target=trafficpolice)
t2 = Thread(target=driver)
t1.start()
t2.start()

# Drivers waiting for GREEN Signal -> Event is set: False
# Traffic Police Giving GREEN Signal
# Traffic Police sleeping
# Traffic Signal is GREEN...Vehicles can move -> Event is set: True
# Vehicle No: 1 Crossing the Signal
# Vehicle No: 2 Crossing the Signal
# Vehicle No: 3 Crossing the Signal
# Vehicle No: 4 Crossing the Signal
# Vehicle No: 5 Crossing the Signal
# Vehicle No: 6 Crossing the Signal
# Vehicle No: 7 Crossing the Signal
# Vehicle No: 8 Crossing the Signal
# Vehicle No: 9 Crossing the Signal
# Vehicle No: 10 Crossing the Signal
# Traffic Police Giving RED Signal
# Traffic Signal is RED...Drivers have to wait
# Drivers waiting for GREEN Signal -> Event is set: False
# .
# .
# .
