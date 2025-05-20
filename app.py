# app.py

def run():
    from machine import Pin
    import time

    led = Pin(2, Pin.OUT)

    print("🚀 Aplicación v1.0.0 iniciada")
    while True:
        print("✅ Ejecutando Otra actualizacion...")
        time.sleep(1)
