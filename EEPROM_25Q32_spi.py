import machine
import utime

# PROGRAMAÇÃO DO EEPROM 25Q32
WRITE_ENABLE      = 0x06        #Address Write Enable
WRITE_DISABLE     = 0x04        #Address Write Disable
CHIP_ERASE        = 0xc7        #Address Chip Erase
READ_STATUS       = 0x05        #Address Read Status
READ_DATA         = 0x03        #Address Read Data
PAGE_PROGRAM_STAT = 0x02        #Address Status Page Program
CHIP_COMMAND_ID   = 0x9f        #Address Status Read Id 

class EEPROM:
    
    buff_read   = bytearray(255)
    buff_write  = bytearray(255)
    
    command     = bytearray(2)
    address     = bytearray(2)

    id          = bytearray(1)
    memory_type = bytearray(1)
    capacity    = bytearray(1)
    
    def __init__(self, CSn, MOSI, MISO, SCK, baudrate = 1000000, bits = 8, phase = 0, polarity = 0 ):
        self._tx  = machine.Pin( MOSI, Pin.OUT )
        self._rx  = machine.Pin( MISO, Pin.IN  )
        self._sck = machine.Pin( SCK , Pin.OUT )
        self._cs  = machine.Pin( CSn , Pin.OUT )
        
        self.spi = SPI( 1, sck= SCK, mosi= MOSI, miso= Miso, baudrate= baudarate, polarity= polarity, phase= phase, bits= bits, firstbit = SPI.MSB )
        
        
    def not_busy(self) -> None :
        self._cs.high()
        self._cs.low()
        self.spi.write( READ_STATUS )
        while (self.spi.read( 1, write = 0 ) & 1 ):
            pass
        self._cs.high() 
    
    def chip_information( self ):
        self._cs.high()
        self._cs.low()
        self.spi.write( CHIP_COMMAND_ID )
        self.id          = self.spi.read( 1, write= 0 )
        self.memory_tipe = self.spi.read( 1, write= 0 )
        self.capacity    = self.spi.read( 1, write= 0 )
        self._cs.high()
        self.not_busy()
    
    def chip_erase(self):
        print("CHIP ERASE CALLED")
        self._cs.high()
        self._cs.low()
        self.spi.write( WRITE_ENABLE )
        self._cs.high()
        self._cs.low()
        self.spi.write( CHIP_ERASE )
        self._cs.high()
        self.not_busy()
    
    def print_page(self, page : list ) -> None :
        for i in range(16):
            for j in range(16):
                print(page[ i*j + j], end=' ' )
            print('\n')
    
    def readPage(self, page : int, page_buff : list) -> list:
        self._cs.high()
        self._cs.low()
        self.spi.write( READ_DATA )
        self.spi.write( page >> 8 )
        self.spi.write( page & 0xff )
        self.spi.write( 0 )
        page_buff = self.spi.read(256, write = 0)
        self._cs.high()
        self.not_busy()
    
    def writePage(self, page, data_buff):
        self._cs.high()
        self._cs.low()
        self.spi.write( WRITE_ENABLE )
        self._cs.high()
        self._cs.low()
        self.spi.write( PAGE_PROGRAM_STAT )
        self.spi.write( page >> 8 )
        self.spi.write( page & 0xff )
        self.spi.write( 0 )
        for i in range(256):
            self.spi.write( data_buff[i] )
        self._cs.high()
        self.not_busy()
    
    def write_one_byte(self, page, offset, data):
        buff = bytearray( 256 )
        self.read_page( buff )
        buff[offset] = data
        write_page( page, buff )
    
    def writeBytes( page, offset, data, len ):
        buff = bytearray(256)
        read_page( buff )
        for i in range( len ):
            buff[ offset + i] = data[i]
        write_page( page, buff )  
            
        
        
        
    
    