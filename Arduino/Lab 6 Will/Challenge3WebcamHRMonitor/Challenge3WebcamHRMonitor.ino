void setup() {
  //setupPhotoSensor();
  setupCommunication();
  setupDisplay();
  writeDisplay("Sleep", 0, true);
}

void loop() {
  //writeDisplay("ass cheecks", 0, false);
  String command = receiveMessage();
  if(command == "sleep") {
    writeDisplay(command.c_str(), 0, true);
  }
  else if(command == "wearable") {
    writeDisplay(command.c_str(), 0, true);
  }
  else {
    if(command != "") {
      String msg = command + " BPM";
      writeDisplay(msg.c_str(), 0, false);
    }
  }
}
