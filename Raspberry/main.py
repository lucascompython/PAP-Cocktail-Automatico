import sys
import threading

import RPi.GPIO as GPIO
import uvicorn
from api import app
import pins

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
        
Pos Rasp:
    3 -> "impulso" para fazer o eixo mexer
"""



if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BCM)
        # Enviar percentagens para o Autómato
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

        # Receber percentagens do Autómato
        GPIO.setup(26, GPIO.IN)
        GPIO.setup(28, GPIO.IN)
        GPIO.setup(32, GPIO.IN)
        GPIO.setup(36, GPIO.IN)
        #GPIO.setup(38, GPIO.IN)
        GPIO.setup(40, GPIO.IN)

        # Para drivers do motor (LN298)
        # Motor 1
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)

        # Motor 2
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)

        # Motor 3
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(29, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)

        # Bits extra
        GPIO.setup(35, GPIO.IN)
        GPIO.setup(37, GPIO.IN)

        # Posição Raspberry PI (para o eixo)
        GPIO.setup(3, GPIO.OUT)


        server_thread = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"host": "0.0.0.0", "port": 5000}, daemon=True)
        server_thread.start()


        pins.enviar_armazenamento_para_o_automato()

        pins.wait_for_start() 

    except KeyboardInterrupt:
        print("\nInterrunpido pelo utilizador")
        sys.exit(0)
    finally: # garantir que os pinos são libertados
        GPIO.cleanup() 