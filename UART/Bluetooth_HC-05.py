# importamos o módulo UART para usar o Bluetooth
from machine import Pin, UART
from time import sleep 

# Vamos controlar o LED da placa
LED = Pin(25, Pin.OUT)

# Iniciamos o UART do Bluetooth 
uart = UART( 0, baudrate = 9600, tx = Pin(0), rx = Pin(1) ) 

# Vamos conferir as configurações 
print(uart)
 
 
## LOOP 
while True:
    # Vamos ver quantos bytes o bluetooth recebeu 
    bytes_to_read = uart.any()
    
    # Se ele recebeu algum byte, vamos lê-los
    if bytes_to_read > 0 : 
        # Aqui fazemos a leitura de N bytes 
        command= uart.read( bytes_to_read )
        # Vamos printar esse valor na sua forma pura
        print(command)
        
        # Vamos decodificar os bytes em caracteres  
        command= command.decode()
        print(command)
        
        # Se o caracter recebido corresponder
        if command =='L':  
            LED.value(1)
            uart.write( "LED LIGADO (L)".encode() ) 
            
        elif command =='D':
            LED.value(0)
            uart.write( "LED DESLIGADO (D)".encode() )
            
    sleep( 1 )
    
    
    
    
