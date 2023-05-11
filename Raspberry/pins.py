import os
from time import sleep

import orjson
import RPi.GPIO as GPIO


informacao_enviada = False

def obter_percentagem_do_autómato() -> int:
    if GPIO.input(26):
        return 33
    elif GPIO.input(28):
        return 50
    elif GPIO.input(32):
        return 66
    elif GPIO.input(36):
        return 100
    elif GPIO.input(32) and GPIO.input(36):
        return 0


def check_bits_e_enviar_liquido():
    if GPIO.input(26): #33%
        pass

    elif GPIO.input(28): #50%
        pass

    elif GPIO.input(32): #66%
        pass

    elif GPIO.input(36): #100%
        pass

    elif GPIO.input(32) and GPIO.input(36): #0%
        pass


def enviar_armazenamento_para_o_automato():

    try:
        with open("armazenamento.json", "rb") as f:
            armazenamento = orjson.loads(f.read())

    except FileNotFoundError:
        print("Dados do armazenamento não encontrados\nCriando dados do armazenamento e assumindo que o armazenamento está cheio...")
        armazenamento = {
            "percentagens": [100, 100, 100]
        }

    bin_liquido1 = bin(armazenamento["percentagens"][0])[2:]
    bin_liquido2 = bin(armazenamento["percentagens"][1])[2:]
    bin_liquido3 = bin(armazenamento["percentagens"][2])[2:]

    # adicionar zeros à esquerda para ficar com 7 bits
    bin_liquido1 = "0" * (7 - len(bin_liquido1)) + bin_liquido1
    bin_liquido2 = "0" * (7 - len(bin_liquido2)) + bin_liquido2
    bin_liquido3 = "0" * (7 - len(bin_liquido3)) + bin_liquido3

    # enviar bits para o autómato

    #liquido1
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO)

    GPIO.output(8, int(bin_liquido1[0]))
    GPIO.output(10, int(bin_liquido1[1]))
    GPIO.output(12, int(bin_liquido1[2]))
    GPIO.output(16, int(bin_liquido1[3]))
    GPIO.output(18, int(bin_liquido1[4]))
    GPIO.output(22, int(bin_liquido1[5]))
    GPIO.output(24, int(bin_liquido1[6]))

    sleep(0.5)
    #liquido2
    GPIO.output(7, GPIO.HIGH) # para indicar que o liquido2 está a ser enviado

    GPIO.output(8, int(bin_liquido2[0]))
    GPIO.output(10, int(bin_liquido2[1]))
    GPIO.output(12, int(bin_liquido2[2]))
    GPIO.output(16, int(bin_liquido2[3]))
    GPIO.output(18, int(bin_liquido2[4]))
    GPIO.output(22, int(bin_liquido2[5]))
    GPIO.output(24, int(bin_liquido2[6]))

    sleep(0.5)

    #liquido3
    GPIO.output(7, GPIO.LOW) # para indicar que o liquido2 não está a ser enviado
    GPIO.output(40, GPIO.HIGH) # para indicar que o liquido3 está a ser enviado

    GPIO.output(8, int(bin_liquido3[0]))
    GPIO.output(10, int(bin_liquido3[1]))
    GPIO.output(12, int(bin_liquido3[2]))
    GPIO.output(16, int(bin_liquido3[3]))
    GPIO.output(18, int(bin_liquido3[4]))
    GPIO.output(22, int(bin_liquido3[5]))
    GPIO.output(24, int(bin_liquido3[6]))

    sleep(0.5)

    GPIO.output(40, GPIO.LOW) # para indicar que o liquido3 não está a ser enviado

    





def wait_for_start():
    while True:

        if GPIO.input(40) and GPIO.input(7):
            enviar_armazenamento_para_o_automato()
            sleep(21) # tempo que o robo demora a colocar a garrafa no eixo

            #liquido1
            if not GPIO.input(40) and not GPIO.input(7):
                check_bits_e_enviar_liquido()

            #liquido2
            if GPIO.input(40) and not GPIO.input(7):
                check_bits_e_enviar_liquido()

            #liquido3
            if not GPIO.input(40) and GPIO.input(7):
                check_bits_e_enviar_liquido()




        sleep(0.001)
