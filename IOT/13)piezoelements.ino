#include <Arduino.h>
#define IR_PIN 8
#define BUZZER 2
void setup()
{
    // put your setup code here, to run once:
    pinMode(IR_PIN, INPUT);
    pinMode(BUZZER, OUTPUT);
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);
    digitalWrite(0, LOW);
    digitalWrite(1, LOW);
    digitalWrite(BUZZER, HIGH);
    delay(500);
}
void loop()
{
    if (digitalRead(IR_PIN))
    {
        digitalWrite(BUZZER, LOW);
    }
    else
    {
        digitalWrite(BUZZER, HIGH);
    }
}
