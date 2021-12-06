from machine import Pin
from time import sleep 

# definimos os pinos IN 
IN1 = Pin( 5, Pin.OUT )
IN2 = Pin( 4, Pin.OUT )
IN3 = Pin( 3, Pin.OUT )
IN4 = Pin( 2, Pin.OUT )

# Definimos os pinos Enable 
ENB1 = Pin( 6, Pin.OUT )
ENB2 = Pin( 7, Pin.OUT )

# Para podermos usar os motores
# devemos setar os pinos ENB como HIGH
# Para desativarmos os motores, LOW 
ENB1.value( 1 )
ENB2.value( 1 )
 
while True:
    # Para andar para a frente 
    IN1(1)
    IN2(0)

    IN3(1)
    IN4(0)
    sleep(1)

    # Para parar os motores 
    IN1(0)
    IN2(0)
    IN3(0)
    IN4(0)
    sleep(1)

    # Para andarem para trás 
    IN1(0)
    IN2(1)
    IN3(0)
    IN4(1)
    sleep(1)

    # Condição inválida
    IN1(1)
    IN2(1)
    IN3(1)
    IN4(1)
    sleep(1)
