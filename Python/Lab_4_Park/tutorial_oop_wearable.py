from ECE16Lib.Communication import Communication
from time import sleep

if __name__ == "__main__":
  try:
    # Main program code should go here
    count = 0
    comms = Communication('COM4', 115200)
    comms.clear()
    #comms.setup()
    for count in range(30):
        comms.send_message(str(count))
        count += 1
        sleep(1)
        msg = comms.receive_message()
        print(msg)
    print("Normal program execution finished")
  except KeyboardInterrupt:
    print("User stopped the program with CTRL+C input")
  finally:
    comms.close()
    # Clean up code should go here (e.g., closing comms)
    print("Cleaning up and exiting the program")