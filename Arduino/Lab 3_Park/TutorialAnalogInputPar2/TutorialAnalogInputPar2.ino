unsigned int ax = 0;
unsigned int ay = 0;
unsigned int az = 0;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  setupAccelSensor();
}

void loop() {
  readAccelSensor();
  Serial.print(ax);
  Serial.print(",");
  Serial.print(ay);
  Serial.print(",");
  Serial.println(az);
}
