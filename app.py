# app.py

def run():
    from machine import Pin
    import time

    led = Pin(2, Pin.OUT)  # Ajusta el GPIO si usas otro pin

    while True:
       # led.on()
       # time.sleep(1)
       # led.off()
        time.sleep(1)