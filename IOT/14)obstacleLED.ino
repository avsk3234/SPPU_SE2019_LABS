#include <Arduino.h>
#define IR_PIN 5
#define LED 4
#define BUZZER 6
void setup()
{
    // put your setup code here, to run once:
    pinMode(IR_PIN, INPUT);
    pinMode(LED, OUTPUT);
    pinMode(BUZZER, OUTPUT);
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);
    digitalWrite(0, LOW);
    digitalWrite(1, LOW);
    digitalWrite(LED, LOW);
    digitalWrite(BUZZER, HIGH);
    // Serial.begin(9600);
    delay(500);
}
void loop()
{
    // put your main code here, to run repeatedly:
    // Serial.print("OUTPUT: ");
    // Serial.println(digitalRead(IR_PIN));
    if (digitalRead(IR_PIN))
    {
        digitalWrite(LED, HIGH);
        digitalWrite(BUZZER, LOW);
    }
    else
    {
        digitalWrite(LED, LOW);
        digitalWrite(BUZZER, HIGH);
    }
    // delay(1000);
}