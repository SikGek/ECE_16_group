import serial
import time

def setup(serial_name, baud_rate):
    ser = serial.Serial(serial_name, baudrate=baud_rate)
    return ser

def close(ser):
    ser.close()

"""
Main entrypoint for the application
"""
def send_message(ser, message):
   if(message[-1] != '\n'):
       message = message + '\n'
   ser.write(message.encode('utf-8'))


def receive_message(ser, num_bytes=50):
    if(ser.in_waiting > 0):
        return ser.readline(num_bytes).decode('utf-8')
    else:
        return None

def main():
    ser = setup("COM4", 115200)
    send_message(ser, "hello world\n")
    message = receive_message(ser)
    print(message)
    time.sleep(3)
    close(ser)

"""
Main entrypoint for the application
"""

if __name__== "__main__":
    main()