# Importação dos modulos do RP2040
from machine import Pin 

# Importação do sleep 
from time import sleep 

# Definimos o número do pino
# Igual fazíamos com o #define 
PIN_LED = 13 

# Instanciamos LED usando a função Pin
LED = Pin( PIN_LED, Pin.OUT )

# Iniciamos manualmente um Loop infinito
while True: 
    
    # Trocamos o estado do Pino com o comando toggle 
    # podemos usar também LED.high() ou LED.low() 
    LED.toggle() 

    # Sleep de 1s igual o delay(1000)
    sleep(1)