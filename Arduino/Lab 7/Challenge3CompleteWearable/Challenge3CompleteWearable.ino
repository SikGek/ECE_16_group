int sampleTime = 0; // Time of last sample (in Sampling tab)
const int BUTTON_PIN  = 14;
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
int ppg = 0;   
bool sending;
unsigned long current_button_time, before_button_time;
int weatherState = 0, stepState = 1, heartState = 2;
int counter = 0;

void setup() {
  setupPhotoSensor();
  setupAccelSensor();
  setupCommunication();
  setupMotor();
  setupDisplay();
  sending = true;
  writeDisplay("Sleep", 0, true);
}

void loop() {
 //we want to have the button switch the state of what is displayed
 current_button_time = millis();
 if (current_button_time - before_button_time > 1000) {
    if (digitalRead(BUTTON_PIN) == HIGH) {
      counter = counter + 1;
      activateMotor(50);
      //reset the counter back to 0 if it exceeds 2.
      if ( counter > 2 ) {
        counter = 0;
      }
    }
  }
  
  
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
      String msg = command
      writeDisplay(msg.c_str(), 0, false);
    }
  }

  
  //Send if heart rate state is active
  if(sending && sampleSensors() && counter == heartState) {
    sendMessage("Heart");
    String response = String(sampleTime) + ",";
    response += String(ppg);
    sendMessage(response);    
  }
  //Send if pedometer state is active
  if(sending && sampleSensors() && counter == stepState) {
    sendMessage("Steps");
    String response = String(sampleTime) + ",";
    response += String(ax) + "," + String(ay) + "," + String(az);
    sendMessage(response);    
  }
  //Send if weather state is active
  if(sending && counter == weatherState) {
    sendMessage("Weather");
  }

  
}
