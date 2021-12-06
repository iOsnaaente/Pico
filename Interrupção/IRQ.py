from machine import Pin 

led_builtin = Pin(25, Pin.OUT )

def blink_led_builtin():
    led_builtin.toggle() 
    
    if led_builtin.value() == 0: 
        print( "O LED esta deligado" )
    else: 
        print( "O LED esta deligado" )
    
    print( led_builtin.irq().flags() )


button = Pin( 2, Pin.IN, Pin.PULL_UP )
button.irq( blink_led_builtin, Pin.IRQ_FALLING ) 