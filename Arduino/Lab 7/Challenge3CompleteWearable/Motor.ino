const int MOTOR_PIN = A5;
const int pwmFrequency = 5000; // Set the PWM frequency to 5KHz
const int pwmChannel = 0; // Use PWM channel 0
const int pwmBitResolution = 8; 

void setupMotor() {
  ledcSetup (pwmChannel, pwmFrequency, pwmBitResolution);
  ledcAttachPin(MOTOR_PIN, pwmChannel);
}
void activateMotor(int motorPower) {
  ledcWrite(pwmChannel, motorPower);
 }
void deactivateMotor() {
  ledcWrite(pwmChannel, 0);
 }
