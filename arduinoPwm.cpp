#include <Arduino.h>

// String InBytes;
// String pwm_signal;
// String pwm_value;

// int speed_pwm_pin = 5;
// int dir_pwm_pin = 6;
// int duty = 0;
// void setup() {
//   Serial.begin(9600);
//   Serial.setTimeout(0.5);
//   pinMode(LED_BUILTIN,OUTPUT);
//   pinMode(speed_pwm_pin, OUTPUT);
//   pinMode(dir_pwm_pin,OUTPUT); 
// }

// void loop() {
//  if (Serial.available()>0){
//  InBytes = Serial.readStringUntil('\n');
//  pwm_signal = InBytes;
//  pwm_value = InBytes;
//  pwm_signal.remove(2);
//  pwm_value.remove(0,2);
//  duty = pwm_value.toInt();
//  //duty = 100;
//  if (pwm_signal == "s:"){
//   digitalWrite(LED_BUILTIN, HIGH);
//   analogWrite(speed_pwm_pin, duty);
//   Serial.write("Led On");
//   }
//   if (pwm_signal == "d:"){
//   digitalWrite(LED_BUILTIN, LOW);
//   analogWrite(dir_pwm_pin, duty);
//   //Serial.write("Led Off");
//   }
//   else{
//     Serial.write("Invalid input");
//   }
// }
// }

int speed_pwm_pin = 5;
int dir_pwm_pin = 6;
int duty = 0;

void setup(){
  pinMode(speed_pwm_pin, OUTPUT);
  pinMode(dir_pwm_pin,OUTPUT);
  Serial.begin(9600);
}
void loop(){
  
  if(Serial.available()>0){
    String speed  = Serial.readStringUntil(',');
    Serial.read(); //next character is comma, so skip it using this
    String direction = Serial.readStringUntil('\n');
    analogWrite(speed_pwm_pin, speed.toInt());
    analogWrite(dir_pwm_pin, direction.toInt());
  }

}
