from time    import sleep_ms
from machine import Pin

BACKWARD = False
FORWARD  = True

DISABLE = 1 
ENABLE  = 0

class Motor: 
    
    direction = FORWARD
    torque    = ENABLE

    position  = 0.0 
    ratio     = 1.0 
    step      = 1.8
    u_step    = 16 
    nano_step = 0.0 

    # Para ter 30rpm durante 1 segundo
    rpm       = 0 
    pps       = 800  

    def __init__(self, STEP_PIN : int, DIRECTION_PIN : int, ENABLE_PIN : int, TORQUE : bool = False ) -> None:
        self.STEP_PIN       = Pin( STEP_PIN, Pin.OUT ) 
        self.DIRECTION_PIN  = Pin( DIRECTION_PIN, Pin.OUT )
        self.ENABLE_PIN     = Pin( ENABLE_PIN, Pin.OUT )

        self.direction      = FORWARD
        self.torque         = ENABLE if TORQUE else DISABLE 
        self.ENABLE_PIN.value( self.torque )
        
        self.step   = 1.8
        self.u_step = 16 
        self.ratio  = 1

    def configure(self, step : float = 1.8, u_step : int = 16, ratio : float = 1) -> None: 
        self.step   = step
        self.u_step = u_step 
        self.ratio  = ratio 

    def set_torque( self, torque : bool = ENABLE ) -> None:
        self.torque = ENABLE if torque else DISABLE 
        self.ENABLE_PIN.value( self.torque )
        
    def set_velocity( self, rpm : int = 1 ) -> None:
        self.pps = int( ( rpm * 360 * ( self.u_step // self.step ) )/( 60 * self.step ))
        self.rpm = rpm 
    
    def set_direction( self, direction : bool ) -> None:
        self.direction = FORWARD if direction else BACKWARD
        self.DIRECTION_PIN.value( 1 if self.direction == FORWARD else 0 ) 
    
    def _pulse(self, time_spend : int = 2 ) -> None :
        self.STEP_PIN.high()
        sleep_ms ( time_spend//2 )
        self.STEP_PIN.low()
        sleep_ms ( time_spend//2 )
        
    def move( self, angle : int, time_stemp : int = 10 ) -> None:  
        n_pulso = (angle*self.u_step)/self.step
        self.nano_step = n_pulso % 1
        n_pulso = int( n_pulso // 1 )
        if self.nano_step > 1.0 :
            self.nano_step -= 1  
            n_pulso += 1
            
        print( n_pulso ) 
        if self.torque == DISABLE: 
            self.ENABLE_PIN.low() 
            for _ in range( n_pulso ):
                self._pulse( time_stemp )
            self.ENABLE_PIN.high() 
        else:
            for i in range( n_pulso ):
                self._pulse( time_stemp )
        
        if self.direction: self.position += self.step / (self.u_step * self.ratio)  
        else:              self.position -= self.step / (self.u_step * self.ratio)

        if   self.position > 360.0: self.position -= 360.0
        elif self.position < 0:     self.position = 360 - self.position 