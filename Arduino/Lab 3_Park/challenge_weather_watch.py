from pyowm import OWM
import serial
import time
from datetime import datetime



def setup(serial_name, baud_rate):
    ser = serial.Serial(serial_name, baudrate=baud_rate)
    return ser

def close(ser):
    ser.close()


def send_message(ser, msg):
   if(msg[-1] != '\n'):
       msg = msg + '\n'
   ser.write(msg.encode('utf-8'))

def main():
    ser = setup("COM4", 115200)
    owm = OWM('f67a8bd72af38a177e331d7882d60e03').weather_manager()
    weather = owm.weather_at_place('San Diego, CA, US').weather
    msg = weather.temperature('fahrenheit')['temp']
    now = datetime.now()
    tim = now.strftime("%H:%M:%S")
    dat = now.strftime("%b-%d-%Y")
    message = tim + ',' + dat +',' + 'Temp:' + str(msg)
    send_message(ser,message)
    time.sleep(1)
    close(ser)

if __name__== "__main__":
    while(True):
        main()