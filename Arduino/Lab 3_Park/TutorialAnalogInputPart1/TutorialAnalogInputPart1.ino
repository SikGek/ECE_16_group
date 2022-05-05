const int accelX = A2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(accelX, INPUT);
}

void loop() {
  int accel_val = analogRead(accelX);
  // put your main code here, to run repeatedly:
  Serial.println(accel_val);
}
