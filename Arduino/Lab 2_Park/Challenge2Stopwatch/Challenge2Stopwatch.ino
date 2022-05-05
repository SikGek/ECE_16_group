//initialize the button pin and differnet time variables along with counter
const int BUTTON_PIN = 14;
unsigned int counter = 0;
unsigned long start_time = millis();
unsigned int state = 1;
unsigned long elapsed_time = 0;
unsigned long before_time;
unsigned long clocked_time = 0;

void setup() {
  // put your setup code here, to run once:
  //set up the button pin as input as well as start the serial monitor
  pinMode(BUTTON_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  before_time = clocked_time;
  // put your main code here, to run repeatedly:
  //if button has been pressed and the stopwatch was off, turn it on
  if(digitalRead(BUTTON_PIN) == LOW && state == 1){
    state = 2;
    delay(10);
  }
  //if button has been pressed and the stopwatch was on, turn it off
  else if(digitalRead(BUTTON_PIN) == LOW && state == 2){
    state = 1;
    delay(10);
  }
  //if stopwatch is on, check if elapsed time is greater than 1, and if it is add 1 to counter
  if(state == 2){
    elapsed_time = millis();
    if(elapsed_time - before_time >= 1000){
      clocked_time = millis();
      counter = counter + 1;
    }
  }
   Serial.println(counter);
   delay(100);
}
