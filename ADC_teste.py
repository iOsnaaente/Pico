from machine import Pin, ADC
from time import sleep 

led    = Pin( 25, Pin.OUT )
rele_1 = Pin( 17, Pin.OUT )
rele_2 = Pin( 16, Pin.OUT )

pot_gir = ADC(1) 
pot_ele = ADC(0)

factor = 3.3/ 2**16

while True:
    # Medido em tensão de 0 - 3.3V 
    print("Pot_1: ", pot_gir.read_u16()*factor, "\nPot_2: ", pot_ele.read_u16()*factor, end='\n' )
    
    if pot_gir.read_u16()*factor < 1.5 :
        rele_1.high()
    else:
        rele_1.low()
    
    if pot_ele.read_u16()*factor < 1.5 :
        rele_2.high()
    else:
        rele_2.low()

    led.toggle()
    sleep(1)