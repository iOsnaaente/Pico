
from machine import Pin 
import utime 

Trig = Pin( 15, Pin.OUT )
Echo = Pin( 14, Pin.IN )

def get_distance():
  Trig.high() 
  utime.sleep_us(2)
  Trig.low()

  while Echo.value() == 0: 
    time1 = utime.ticks_us() 
  
  
  while Echo.value() == 1:
    time2 = utime.ticks_us() 
  
  d_time = time2 - time1 

  # Velocidade do som 343.2 m/s ou 0.0343cm/ms
  # Pegamos o tempo de eco, que vale o tempo de ida e tempo de volta 
  time = (d_time * 0.0343) / 2

  return time 


while True: 
  print( get_distance() ) 
  utime.sleep_us(1000)