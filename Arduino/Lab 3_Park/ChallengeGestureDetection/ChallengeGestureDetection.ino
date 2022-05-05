int numTaps = 0;
int sampleTime = 0; // Time of last sample (in Sampling tab)
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; 
int ay = 0;
int az = 0;
int timer = 0;
long start_time = millis();
int state = 1;
long elapsed_time = 0;
long before_time = 0;
long clocked_time = 0;
long now_time;
const int BUTTON_PIN = 14;
int timer_time = 0;
int timer_time2 = 0;


void setup() {
  // put your setup code here, to run once:
     setupAccelSensor();
     setupDisplay();
     pinMode(BUTTON_PIN, INPUT);
     setupMotor();
     Serial.begin(115200);
}

void loop() {
     now_time = millis();
  // put your main code here, to run repeatedly:
     /*check for taps every iteration */
     if(sampleSensors() && Serial.availableForWrite()) {
        detectTaps();
     }
     /*if 4 seconds have passed since tap has been detected count down*/
     if(now_time - before_time > 4000 && numTaps > 0 && now_time - elapsed_time > 1000){
       elapsed_time = millis();
       numTaps -= 1;
     }
     /*if number of taps has reached 0 vibrate the motor*/
     if(numTaps == 0) {
      activateMotor(255);
     }
     /*otherwise turn off the motor*/
     if(numTaps != 0) {
      deactivateMotor();
     }
     /*if button is pressed, record time, and if 2 seconds have passed, then set timer to 0*/
     if(digitalRead(BUTTON_PIN) == LOW) {
      timer_time = millis();
      while(digitalRead(BUTTON_PIN) == LOW){
        timer_time2 = millis();
        if(timer_time2 - timer_time >= 2000){
          numTaps = 0;
        }
      }
     }
     /*display number of taps on OLED*/
     String msg = String(numTaps) + " taps";
     writeDisplay(msg.c_str(),1, true);
}
