from ECE16Lib.IdleDetector import Idle_Detector as id


if __name__ == "__main__":
    detect = id(250, "COM4", 115200)
    detect.run()