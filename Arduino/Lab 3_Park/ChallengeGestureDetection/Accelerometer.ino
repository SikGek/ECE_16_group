const int X_PIN = A2;
const int Y_PIN = A3;
const int Z_PIN = A4;

void setupAccelSensor() {
  pinMode(X_PIN, INPUT);
  pinMode(Y_PIN, INPUT);
  pinMode(Z_PIN, INPUT);
}

void readAccelSensor() {
  ax = analogRead(X_PIN);
  ay = analogRead(Y_PIN);
  az = analogRead(Z_PIN);
}

/*if a tap is detected according to the threshold, add 1 to taps*/ 
void detectTaps() {
  if(az > 2450 || az < 2300){
    numTaps += 1;
    delay(50);
    before_time = millis();
  }
}
