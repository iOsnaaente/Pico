import dearpygui.dearpygui as dpg 
import numpy as np
import struct
import serial 
import time 

COMPORT = 'COM12'
BAUDRATE = 19200


print( "Versão do DearPyGui: ", dpg.get_dearpygui_version() )
print( "Author: Bruno Gabriel F. Sampaio ")


comp = serial.Serial( COMPORT, baudrate = BAUDRATE )
Z = [ 0 for _ in range(100) ]

def make_data_run( phase ):
    global Z
    t = np.linspace(0,2*np.pi, 100)
    Z = np.cos(t + np.radians(phase) )
    dpg.configure_item("Z_value", x = t, y = Z )

def att_data_run( z_val ):
    global Z
    t = [ i for i in range(100) ]
    Z.append(z_val)
    Z.pop(0)
    dpg.configure_item("Z_value", x = t, y = Z )


with dpg.window() as main_window:
    pass

with dpg.window(id='Ploter', label="simple plot", no_resize=True, no_title_bar=True, no_move=True):
    with dpg.plot(id='Graph', label="Plot AS5600", height=300, width=400, anti_aliased=True):
        dpg.add_plot_legend()

        dpg.add_plot_axis(dpg.mvXAxis, label="Tempo", id='x_axis')
        dpg.set_axis_limits("x_axis", 0, 100 )
        dpg.add_plot_axis(dpg.mvYAxis, label="Valores XYZ", id="y_axis")
        dpg.set_axis_limits('y_axis', -5, 375)
        
        dpg.add_line_series([], [], label="Z_value", id="Z_value", parent="y_axis")


def resize_group( sender, data, user ):
    dpg.configure_item('Ploter', height = data[1], width = data[0] ) 
    dpg.configure_item('Graph', height = data[1]*0.9, width = data[0]*0.9, pos=[ data[0]*0.05, data[1]*0.05] ) 


dpg.setup_viewport()

dpg.set_primary_window     ( main_window, True              )
dpg.set_viewport_min_height( height = 700                   ) 
dpg.set_viewport_min_width ( width  = 800                   ) 
dpg.set_viewport_title     ( title  = 'Ploter AS5600'       )

dpg.maximize_viewport() 

dpg.add_resize_handler(main_window, callback=resize_group)


z_data = 0.0

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame() 
    count = dpg.get_frame_count() 
    pBytes = b''
    while comp.inWaiting() > 0:
        nBytes = comp.in_waiting
        if nBytes == 4:  
            pBytes += comp.read(nBytes)
            print( f'[{count} / {len(pBytes)}]: {pBytes}' ) 
            z_data = struct.unpack('f', pBytes )[0]
            print( z_data)
            att_data_run(z_data)
        else: 
            comp.read(nBytes)
    time.sleep(0.01)    

