#include <Wire.h>

int MODE = 0;

void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x8);

  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
    
}

void receiveEvent(int howMany) {
  while (Wire.available()) {
    int i = Wire.read();
//    Serial.print(i);
//    Serial.print("\n");
    MODE = i;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  switch(MODE) {
    case 0:
      Serial.print(0);
      break;
     case 1:
      Serial.print(1);
      break;
     case 2:
      Serial.print(2);
      break;
  }
  Serial.print("\n");
  delay(100);
}
