from machine import Pin, PWM, ADC
from time import sleep 

# Iniciamos o Servo 
servo = PWM( Pin(  0 ) ) 
servo.freq( 50 )

# Criamos o objeto do ADC 
pot = ADC( Pin( 26 ) ) 


while True:
  # PWM.duty_u16 leva valores de 0 até 65535 
  # A leitura ADC também 

  # O servo SG90 tem 2% do duty cycle para -90º 
  # Isso equivale a 1350 de 65535 
  # E tem 12% do duty cycle para atingir os +90º 
  # Isso equivale a 8200 de 65535
  
  # Fazemos uma conversão para normalizar os valores
  # norm = ( leitura - val_min ) / ( val_max - val_min )
  
  leitura_pot = pot.read_u16()
   
  norm = ( leitura_pot - 1350 ) / (8200 - 1350)   
  
  # Move o servo para a posição do potenciometro
  servo.duty_u16( norm )
  sleep(0.1)
  
  
  
  

