#include <Arduino.h>

int speed_pwm_pin = 5;
int direction_pwm_pin = 6;

void setup() {
  Serial.begin(9600);
  pinMode(speed_pwm_pin,OUTPUT);
  pinMode(direction_pwm_pin,OUTPUT);

}

void loop() {
  int sensor_value = analogRead(A0);
  sensor_value = map(sensor_value,0,1023,0,255);
  Serial.println(sensor_value);
  analogWrite(speed_pwm_pin,sensor_value);
  analogWrite(direction_pwm_pin,sensor_value);
  _delay_ms(50);
}