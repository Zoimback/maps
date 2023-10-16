import RPi.GPIO as GPIO
import time

# Inicializa el objeto PWM
def start():
    # Configura los pines de control
    IN1 = 18
    IN2 = 17

    # Configura la numeración de pines de la Raspberry Pi
    GPIO.setmode(GPIO.BCM)

    # Configura los pines de control como salida
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)

    # Crea un objeto PWM para controlar la velocidad del motor
    pwm = GPIO.PWM(IN1, 100)

    # Inicializa el objeto PWM
    pwm.start(0)
    
    return("Start done")

def stop():
#Detiene y limpia los pines
    pwm.stop()
    GPIO.cleanup()

def rigth(int:seconds,intensidad):
#Giro a la derecha, paramentros --> segundos(giro), intensidad()    
    try:
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        pwm.ChangeDutyCycle(intensidad)
        time.sleep(seconds)
        return(print("Right"))
    except Exception as e:
        return(print("ERROR RIGHT --> " + str(e)))
    pwm.ChangeDutyCycle(0)

def left(int:seconds):

    try:
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        pwm.ChangeDutyCycle(10)
        time.sleep(seconds)
        return(print("Left"))
    except Exception as e:
        return(print("ERROR LEFT --> " + str(e)))
    pwm.ChangeDutyCycle(0)


