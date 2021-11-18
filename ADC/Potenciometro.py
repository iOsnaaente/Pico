from machine import Pin, ADC
from time import sleep 

LED_BUILTIN = Pin( 25, Pin.OUT )

RELE_1 = Pin( 17, Pin.OUT ) # Red Led
RELE_2 = Pin( 16, Pin.OUT ) # Blue Led 

POTENCIOMETRO_1 = ADC(1) # Yellow wire 
POTENCIOMETRO_2 = ADC(0) # Blue wire 

FACTOR = 3.3/ 2**16

while True:
    # Medido em tensão de 0 - 3.3V 
    print("Pot_1: ", POTENCIOMETRO_1.read_u16()*FACTOR, end='\n')
    print("Pot_2: ", POTENCIOMETRO_2.read_u16()*FACTOR, end='\n' )
    
    # Podemos passar valores para os pinos de saída usando o .value() 
    RELE_1.value( True if POTENCIOMETRO_1.read_u16()*FACTOR < 1.5 else False )
    
    # Ou podemos passar os valores utilizando .high() e .low() 
    if POTENCIOMETRO_1.read_u16()*FACTOR < 1.5 :    RELE_2.high()
    else:                                           RELE_2.low()

    # Outro modo de alterar os valores dos pinos é utilizando o .toggle() 
    # Desse modo, o valor passa a ser ivnertido 1 -> 0  e 0 -> 1 
    LED_BUILTIN.toggle()

    sleep(1)
    