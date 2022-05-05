int sampleTime = 0; // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
bool sending;

void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  sending = false;
  writeDisplay("Sleep", 0, true);
}

void loop() {
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
      String msg = command + " steps";
      writeDisplay(msg.c_str(), 0, false);
    }
  }
  if(sending && sampleSensors()) {
    String response = String(sampleTime) + ",";
    response += String(ax) + "," + String(ay) + "," + String(az);
    sendMessage(response);    
  }
}
