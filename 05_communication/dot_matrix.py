# import matrix module
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import  show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

# create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=0,
                    rotate=0, blocks_arranged_in_reverse_order=False)
print("Created device")

# slow
msg = "Korea Digital Media High School"
print(msg)
show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.1)
    
# demo(1, 0, 0, False)
