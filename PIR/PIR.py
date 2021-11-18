from machine import Pin
from utime import ticks_ms, sleep 

RED_PIN   = 21
GREEN_PIN = 20
BLUE_PIN  = 19 

PIR_PIN   = 15 

TEMPO_MAXIMO = 2000
offset       = 0

RED   = Pin( RED_PIN  , Pin.OUT )
GREEN = Pin( GREEN_PIN, Pin.OUT )
BLUE  = Pin( BLUE_PIN , Pin.OUT )

PIR   = Pin(PIR_PIN   , Pin.IN  )

while True: 
  if PIR.value() == 1 : 
    BLUE.high()  
    GREEN.low() 
    RED.low()
    
    print( "PIR == 1" )
    offset = ticks_ms()
  
  else:
    if ( ticks_ms() - offset) > TEMPO_MAXIMO:
      BLUE.low()  
      GREEN.low() 
      RED.high()
      print( "PIR == 0 e tempo excedido" )

    else:
      BLUE.low()  
      GREEN.high() 
      RED.low()
      print( "PIR == 0 e tempo contando" )

  sleep(0.01)