#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Liga 3 LEDs                                              #
#  Quando o botão do pino 18 é pressionado                  #
#  Os LEDs são ligados, um por um                           #
#  Conforme descrição no comando if                         #
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
#Definindo a utilização da biblioteca GPIO e time 
#	em um mesmo import
import RPi.GPIO as GPIO, time
#Iniciando contador
contador = 0
#Aqui definimos que vamos usar o numero de ordem do pino, e
#	não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição 
#	"GPIO.BOARD (12)" para "GPIO.BCM (18)" 
#Definindo a pinagem real
GPIO.setmode(GPIO.BOARD)
#Definindo os pinos onde serão conectados o leds, como saída
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
#Definindo o pino do botao como entrada
GPIO.setup(18, GPIO.IN)
#Apagando todos os leds
GPIO.output(11,0)
GPIO.output(12,0)
GPIO.output(13,0)
try:
    while(1):
        #Verificando se o botao foi pressionado
        if GPIO.input(18) == True:
            #Incrementando contador
            contador = contador+1
            time.sleep(0.5)
        #Caso contador = 1, acende o led vermelho
        if contador == 1:
            GPIO.output(11, 1)       
        #Caso contador = 2, acende o led azul
        if contador == 2:
            GPIO.output(12, 1)
        #Caso contador = 3, acende o led verde
        if contador == 3:
            GPIO.output(13, 1)
        #Caso contador = 4, apaga todos os leds e zera o contador
        if contador == 4:
            GPIO.output(11, 0)
            GPIO.output(12, 0)
            GPIO.output(13, 0)
            contador = 0
except KeyboardInterrupt:
    print ("Fim")
    pass
finally:
    GPIO.cleanup()

#Fonte: FILIPEFLOP
