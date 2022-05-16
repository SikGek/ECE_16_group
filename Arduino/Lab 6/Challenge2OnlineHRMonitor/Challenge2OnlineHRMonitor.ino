int sampleTime = 0; // Time of last sample (in Sampling tab)
int ppg = 0;   
bool sending;

void setup() {
  setupPhotoSensor();
  setupCommunication();
  setupDisplay();
  sending = true;
  writeDisplay("Sleep", 0, true);
}

void loop() {
  //writeDisplay("ass cheecks", 0, false);
  String command = receiveMessage();
  if(command == "sleep") {
    sending = false;
    writeDisplay(command.c_str(), 0, true);
  }
  else if(command == "wearable") {
    sending = true;
    writeDisplay(command.c_str(), 0, true);
  }
  else {
    sending = true;
    if(command != "") {
      String msg = command + " BPM";
      writeDisplay(msg.c_str(), 0, false);
    }
  }
  if(sending && sampleSensors()) {
    String response = String(sampleTime) + ",";
    response += String(ppg);
    sendMessage(response);    
  }
}
