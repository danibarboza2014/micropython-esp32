from machine import Pin
import time

led = Pin(2, Pin.OUT)

print("🚀 Aplicación iniciada")

def run():
    while True:
        print("Ejecutando  Cambio 1111...")  
        time.sleep(1)
