'''
дальномер
'''
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time


def len():
    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D5)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pin 0
    chan = AnalogIn(mcp, MCP.P0)

    print('Raw ADC Value: ', chan.value)
    print('ADC Voltage: ' + str(chan.voltage) + 'V')

    active = False
    try:
        for _ in range(5):
            input_Pir = round(10* pow( (chan.value * 0.0048828125),int(-1))  *100, 1)
            print(input_Pir)
            time.sleep(0.6)
            if not input_Pir > 4:
                active = False
                break
            else:
                active = True
    except:
        return False
    return active

# if len():
#     print("дальнометр работает")
# else:
#     print("дальнометр не работает")