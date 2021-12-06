from machine import Pin, PWM
from time import sleep 

# Criamos o objeto PWM do servo 
servo = PWM( Pin(0) )

# O servo opera com frequência fixa de 50 Hz 
servo.freq( 50 )

while True:
  # PWM.duty_u16 leva valores de 0 até 65535 
  # Esses valores correspondem ao duty cycle do pwm 
  # Ou melhor dizendo, ao comprimento de pulso 

  # O servo SG90 tem 2% do duty cycle para 0º 
  # Isso equivale a 1350 de 65535 

  # Move o servo até 0º ( 2% do duty cycle )
  servo.duty_u16(1350)
  sleep(1)
  
  # E tem 12% do duty cycle para atingir os 180º 
  # Isso equivale a 8200 de 65535 

  # Move o servo até 180º (12% do duty cycle )
  servo.duty_u16(8200)
  sleep(1)
  
  
  
  
  
