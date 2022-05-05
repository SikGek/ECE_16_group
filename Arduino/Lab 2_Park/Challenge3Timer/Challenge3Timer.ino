//initiailize button pin, timer and different time variables
const int BUTTON_PIN = 14;
unsigned int timer = 0;
unsigned long start_time = millis();
unsigned int state = 1;
unsigned long elapsed_time = 0;
unsigned long before_time = 0;
unsigned long clocked_time = 0;
unsigned long now_time;

void setup() {
  // put your setup code here, to run once:
  //initialize button pin as input and start serial monitor
  pinMode(BUTTON_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  now_time = millis();
  // put your main code here, to run repeatedly:
  //if button is pressed add 1 to timer regardless of anything else
  if(digitalRead(BUTTON_PIN) == LOW){
    before_time = millis();
    timer += 1;
    delay(10);
  }
  //if button hasnt been pressed for 3 seconds, timer is greater than 0, and a second has passed since the last time this part has been ran, subtract 1 from timer.
  if(now_time - before_time > 3000 && timer > 0 && now_time - elapsed_time > 1000){
    elapsed_time = millis();
    timer -= 1;
    if(digitalRead(BUTTON_PIN) == LOW){
      before_time = millis();
    }
  }
  
  Serial.println(timer);
  delay(100);
}
