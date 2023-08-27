#define ledRed 11
#define ledGreen 10
#define ledBlue 9
#define potRed A0
#define potGreen A1
#define potBlue A2
void setup()
{
    pinMode(ledRed, OUTPUT);
    pinMode(ledGreen, OUTPUT);
    pinMode(ledBlue, OUTPUT);
    pinMode(potRed, INPUT);
    pinMode(potGreen, INPUT);
    pinMode(potBlue, INPUT);
}
void loop()
{
    analogWrite(ledRed, analogRead(potRed) / 4);
    analogWrite(ledGreen, analogRead(potGreen) / 4);
    analogWrite(ledBlue, analogRead(potBlue) / 4);
    // analogWrite- Writes an analog value to a pin as a digital PWM (pulse-width modulated) signal.
    delay(100);
}
