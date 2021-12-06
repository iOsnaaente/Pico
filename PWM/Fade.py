# Importamos o módulos Pin e PWM 
from machine import Pin, PWM

# Importamos o módulo Time 
from time import sleep

# Definimos o pino ao qual iremos usar o Fade 
LED_BUILTIN = Pin( 25, Pin.OUT )

# Definimos o PWM sobre o Pino 
FADE = PWM( LED_BUILTIN )

# Definimos a frequência de operação do PWM 
FADE.freq( 1000 )        

## LOOP 
while True:
    
    # Criamos uma repetição ciclica      
    for i in range( 0, 2**16, 100 ):
        
        # Mudamos o valor do Duty cicle 
        FADE.duty_u16( i )
        
        # Damos um Delay para recomeçar 
        sleep( 0.005 ) 

