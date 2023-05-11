import RPi.GPIO as GPIO
from time import sleep
import argparse

out1 = 3
out2 = 5
out3 = 7
out4 = 13


enable1 = 15
enable2 = 19





VEL = 0.0005 # quanto maix baixo, mais rapido
PROGRAM_ENABLE = 37
VOLTAS = 1


i=0
positive=0
negative=0
y=0


def check_pin_enable() -> bool:
    return bool(GPIO.input(PROGRAM_ENABLE))

def arg_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="GRANDE",
        description="Controla o motor",
    )
    parser.add_argument("-c", "--completo", action="store_true")

    return parser.parse_args()

def run(completo: bool):
    global VEL

    if not completo: 
        for _ in range(round((VOLTAS * 400) / 8)):
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            sleep(VEL)
            #sleep(1)
        #if i == 0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            sleep(VEL)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            sleep(VEL)
    else:
        VEL *= 2
        for _ in range(round((VOLTAS * 200) / 4)):

            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            sleep(VEL)
            #sleep(1)
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            sleep(VEL)
def main():

    args = arg_parse()
    completo = args.completo
    

    while not check_pin_enable():
        sleep(0.001)
    
    run(completo)


if __name__ == "__main__":


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PROGRAM_ENABLE, GPIO.OUT)
    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(out3,GPIO.OUT)
    GPIO.setup(out4,GPIO.OUT)

    GPIO.setup(enable1,GPIO.OUT)
    GPIO.setup(enable2,GPIO.OUT)

    try:
        main()
    finally:
        GPIO.cleanup()