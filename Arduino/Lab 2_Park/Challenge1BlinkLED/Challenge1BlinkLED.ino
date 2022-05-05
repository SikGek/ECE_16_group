// Specify the LED pins
const int LED_pin = 12;
const int LED_pin_red = 14;

unsigned long before_time = millis();

// How long the LED stays on or off this will vary depending on gif
int period;
int on_period = 20;
int off_period = 1000;

// Start LED logic as “OFF”
int LED = LOW;

void setup() {
  // Setup the LED for output
  pinMode(LED_pin, OUTPUT);
       //initialize digital pin LED_BUILTIN as an output
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_pin_red, OUTPUT);
}

void loop() {
  // Get the current time every time we loop
  unsigned long now_time = millis();

  // Check if enough time has elapsed and updates the LED logic state
  // Also change the period for different durations of ON/OFF times
  if (now_time - before_time >= period){
    before_time = millis(); //update before time

    if (LED == LOW) {
      LED = HIGH;
      period = on_period;
    }
    else {
      LED = LOW;
      period = off_period;
    }
  }
  //depending on gif, uncomment the proper led
  digitalWrite(LED_pin, LED);
  //digitalWrite(LED_pin_red, LED);
  //digitalWrite(LED_BUILTIN, LED);
}
