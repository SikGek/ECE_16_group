#include <string>
int sampleTime = 0; // Time of last sample (in Sampling tab)
const int BUTTON_PIN  = 14;
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
int i = 1,j = 0;
int axStore[1500];
int ayStore[1500];
int azStore[1500];
int storeTime[1500];
String stepCount = "", jumpCount = "";
bool sending;
unsigned long current_button_time;
unsigned long before_button_time;
unsigned long current_request_time;
unsigned long before_request_time;

void setup() {
  Serial.begin(9600);
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
    writeDisplay("Sleep", 0, true);
  }
  else if(command == "wearable") {
    sending = true;
    writeDisplay("Wearable", 0, true);
  }
  //store ax,ay,az in the arrays at the sampled times.
  if(sampleSensors()) {
    //Serial.println("we are storing accel data");
    readAccelSensor();
    axStore[i] = ax;
    ayStore[i] = ay;
    azStore[i] = az;
    storeTime[i] = sampleTime;
  }
  current_button_time = millis();
  //can only press the button once a second
  if(current_button_time - before_button_time > 1000) {
    if(digitalRead(BUTTON_PIN) == LOW) {
      Serial.print("button pressed");
      sendMessage("uploadData");
      for(j=0; j<1501;j = j+1){
        //send the arrays to python to be analyzed
        String response = String(storeTime[j]) + ",";
        Serial.println(String(azStore[i]));
        response += String(axStore[j]) + "," + String(ayStore[j]) + "," + String(azStore[j]);
        sendMessage(response);
      }
      //tell python our upload is complete
      sendMessage("uploadComplete");
      //reset all the arrays and i
      i = 1;
    }
    before_button_time=millis();
  }
  //if our arrays fill up lets reset them
  if(i==1500){
    i=1;
  }
  //we must request for the jump and walk counter
  current_request_time=millis();
  if(current_request_time - before_request_time > 500) {
    stepCount = receiveMessage();
    before_request_time = millis();
  }
  //display our stepCount and jumpCount on the OLED
  //receive step and jump count separated by a comma, save each to separate variables and print them individually
  int startIndex = 0;
  writeDisplay("Steps: ", 0, false);
  writeDisplay("Jumps: ", 2, false);
  int index = stepCount.indexOf(',', startIndex);           
  String subMessage = stepCount.substring(startIndex, index);
  startIndex = index + 1;
  int index1 = stepCount.indexOf(',', startIndex);
  String subMessage2 = stepCount.substring(startIndex, index1);
  writeDisplay(subMessage.c_str(), 1, false);
  writeDisplay(subMessage2.c_str(), 3, false);
  i+=1;
}
