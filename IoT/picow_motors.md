# Picture of Fritzing 

```
# Raspberry Pi Pico Motor Test
# picow_motor.py
#
# Based on: DroneBot Workshop 2021
# https://dronebotworkshop.com
from machine import Pin, PWM
from utime import sleep


button = Pin(15, Pin.IN, Pin.PULL_UP)
mtr_AI1 = Pin(18, Pin.OUT)
mtr_AI2 = Pin(19, Pin.OUT)
mtr_PWMa = PWM(Pin(20))


mtr_PWMa.freq(50)
mtr_AI1.value(1)
mtr_AI2.value(0)

timer = 10
# while True:
for _ in range(timer):

    mtr_PWMa.duty_u16(32768)  # 50%
    
    if button.value() == 1:
        mtr_AI1.value(1)
        mtr_AI2.value(0)
    
    if button.value() == 0:
        mtr_AI1.value(0)
        mtr_AI2.value(0)
        
    sleep(0.25)
    print(button.value())

```
