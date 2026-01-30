#include <Arduino.h>

#define LED_R 5
#define LED_G 6
#define LED_B 7

void setup() {
  Serial.begin(115200);

  pinMode(LED_R, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);

  analogWrite(LED_R, 0);
  analogWrite(LED_G, 0);
  analogWrite(LED_B, 0);
}

void loop() {
  if (Serial.available()) {
    int r = Serial.parseInt();
    int g = Serial.parseInt();
    int b = Serial.parseInt();

    r = constrain(r, 0, 255);
    g = constrain(g, 0, 255);
    b = constrain(b, 0, 255);

    analogWrite(LED_R, r);
    analogWrite(LED_G, g);
    analogWrite(LED_B, b);
  }
}
