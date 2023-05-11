import sys
import threading

import RPi.GPIO as GPIO
import uvicorn
from api import app

"""
Raspbarry PI PINS

Enviar percentagens para o Autómato:
    8 -> ENTR_1
    10 -> ENTR_2
    12 -> ENTR_3
    16 -> ENTR_4
    18 -> ENTR_5
    22 -> ENTR_6
    24 -> ENTR_7

Receber percentagens do Autómato:
    26 -> 33%
    28 -> 50%
    32 -> 66%
    36 -> 100%
    #38
    40 -> BIT_EXTRA1_OUT no Autómato usado para indicar qual o líquido que está a ser enviado para o Raspberry e quando começar o programa
    7 -> BIT_EXTRA2_OUT no Autómato usado para indicar qual o líquido que está a ser enviado para o Raspberry e quando começar o programa

Para drivers do motor (LN298):
    Motor 1:
        5
        7
        11
        13
    Motor 2:
        15
        19
        21
        23
    Motor 3:
        27
        29
        31
        33

Bits extra:
    35 -> BIT_EXTRA1_IN no Autómato usado para indicar qual o líquido que está a ser enviado para o autómato e quando começar o programa
    37 -> BIT_EXTRA2_IN no Autómato usado para indicar qual o líquido que está a ser enviado para o autómato e quando começar o programa
        
"""


def main():
    print("main")

if __name__ == "__main__":
    try:
        server_thread = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"host": "0.0.0.0", "port": 5000}, daemon=True)

        server_thread.start()

        main()
    except KeyboardInterrupt:
        print("\nInterrunpido pelo utilizador")
        sys.exit(0)
    finally: # garantir que os pinos são libertados
        GPIO.cleanup() 