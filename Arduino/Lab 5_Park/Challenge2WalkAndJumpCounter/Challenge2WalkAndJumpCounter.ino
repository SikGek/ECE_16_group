#include <string>
int sampleTime = 0; // Time of last sample (in Sampling tab)
const int BUTTON_PIN  = 14;
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
int i = 1,j = 0;
int axStore[512];
int ayStore[512];
int azStore[512];
int storeTime[512];
String stepCount = "", jumpCount = "";
bool sending;
unsigned long current_button_time;
unsigned long before_button_time;
unsigned long current_request_time;
unsigned long before_request_time;
unsigned long current_display_time;
unsigned long before_display_time;

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
//  if(sending && sampleSensors()) {
//    String response = String(sampleTime) + ",";
//    response += String(ax) + "," + String(ay) + "," + String(az);
//    sendMessage(response);
//  }
  //store ax,ay,az in the arrays at the sampled times.
  if(sampleSensors()) {
    //Serial.println("we are storing accel data");
    readAccelSensor();
    axStore[i] = ax;
    ayStore[i] = ay;
    azStore[i] = az;
    storeTime[i] = sampleTime;
    //Serial.print(ax);
    //Serial.print(ay);
    //Serial.println(String(azStore[i]));
  }
  current_button_time = millis();
  //can only press the button once a second
  if(current_button_time - before_button_time > 1000) {
    if(digitalRead(BUTTON_PIN) == HIGH) {
      Serial.print("button pressed");
      sendMessage("uploadData");
      for(j=0; j<513;j = j+1){
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
//      memset(axStore, 0, sizeof axStore);
//      memset(ayStore, 0, sizeof axStore);
//      memset(azStore, 0, sizeof axStore);
    }
    before_button_time=millis();
  }
  //if our arrays fill up lets reset them
  if(i==512){
    i=1;
//    memset(axStore, 0, sizeof axStore);
//    memset(ayStore, 0, sizeof axStore);
//    memset(azStore, 0, sizeof axStore);
  }
  //we must request for the jump and walk counter
  current_request_time=millis();
  if(current_request_time - before_request_time > 1000) {
    sendMessage("stepRequest");
    stepCount = receiveMessage();
    sendMessage("jumpRequest");
    jumpCount = receiveMessage();
    before_request_time = millis();
  }
  //display our stepCount and jumpCount on the OLED
  current_display_time = millis();
  if(current_display_time - before_display_time > 500) {
    writeDisplay("Jumps: ", 0, true);
    writeDisplay(jumpCount.c_str(), 1, false);
    writeDisplay("Steps: ", 2, false);
    writeDisplay(stepCount.c_str(), 3, false);
    before_display_time = millis();
  }
  i+=1;
}
