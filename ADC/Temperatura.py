from machine import Pin, ADC
from time import sleep 

# LED DA PLACA PICO 
LED_BUILTIN = Pin( 25, Pin.OUT )

# SIMBOLICAMENTE, AQUECEMOS OU ESFRIAMOS O PICO 
LAMP_QUENTE = Pin( 17, Pin.OUT )
LAMP_FRIA   = Pin( 16, Pin.OUT )

# O SENSOR DE TEMPERATURA DO RASP PICO ESTA NO ADC 4 
TEMPERATURA_IN = ADC(4)

# FAZ A CONVERSÃO DA LEITURA ANALOGICA PARA GRAUS CELSIUS 
# PARA LIMITAR A MEDIÇÃO DE 16BITS ENTRE 0 E 3.3V USAMOS A EQ. TEMP*( 3.3V / 2<<16 = 3.3 / 65535 )
# EM 27ºC O SENSOR MEDE 0.706V E CADA GRAU ADICIONAL A TEMPERATURA CAI 1,721mV 
# JUNTANDO TUDO TEMOS A EQUAÇÃO ABAIXO 
DEG_FACTOR = lambda TEMP : 27 - ( TEMP*(3.3/ 2**16) - 0.706 )/0.001721


# 30º como o limite entre frio e calor  
TEMPERATURA_CORTE = 30 


while True:
    # Medido em tensão de 0 - 3.3V 
    TEMPERATURA_CONV = DEG_FACTOR( TEMPERATURA_IN.read_u16() )

    print("Temperatura interna do Pico: ", TEMPERATURA_CONV, end='\n')
    
    # Mudamos o estado das lâmpadas de acordo com a temperatura medida 
    if TEMPERATURA_CONV  >  30: 
        LAMP_QUENTE.low() 
        LAMP_FRIA.high() 

    elif TEMPERATURA_CONV == 30: 
        LAMP_QUENTE.low()
        LAMP_FRIA.low() 

    else:
        LAMP_QUENTE.high()
        LAMP_FRIA.low() 


    LED_BUILTIN.toggle()

    sleep(1)