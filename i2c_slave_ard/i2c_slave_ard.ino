#include <Wire.h>

void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x8);

  Wire.onReceive(receiveEvent);

  
}

void receiveEvent(int howMany) {
  while (Wire.available()) {
    char c = Wire.read();
    Serial.print(c);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
}
