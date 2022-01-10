char serialData;
int pin=6; 

void setup() {
  pinMode(pin,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() >0){
    serialData = Serial.read();
    Serial.print(serialData);

  if(serialData == '1'){
    analogWrite(pin, 255);}
  else if(serialData == '0'){
    analogWrite(pin, 100);}
  }

}
