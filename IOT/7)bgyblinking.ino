const int green_led = 10;
const int red_led = 11;
const int blue_led = 9;
void setup()
{
    pinMode(green_led, OUTPUT);
    pinMode(red_led, OUTPUT);
    pinMode(blue_led, OUTPUT);
}
unsigned char key;
void loop()
{
    Serial.begin(9600);
    while (1)
    {
        key = Serial.read(); // reads the incoming serial data in the Arduino.
        if ((key == 'g') || (key == 'G'))
            break;
        if ((key == 'r') || (key == 'R'))
            break;
        if ((key == 'y') || (key == 'Y'))
            break;
        if ((key == 'b') || (key == 'B'))
            break;
        delay(100);
    }
    Serial.end();
    delay(200);
    if ((key == 'g') || (key == 'G'))
    {
        digitalWrite(green_led, HIGH);
        delay(3000);
        digitalWrite(green_led, LOW);
    }
    else if ((key == 'y') || (key == 'Y'))
    {
        digitalWrite(blue_led, HIGH);
        delay(3000);
        digitalWrite(blue_led, LOW);
    }
    else if ((key == 'r') || (key == 'R'))
    {
        digitalWrite(red_led, HIGH);
        delay(3000);
        digitalWrite(red_led, LOW);
    }
    else if ((key == 'b') || (key == 'B'))
    {
        digitalWrite(green_led, HIGH);
        delay(1000);
        digitalWrite(green_led, LOW);
        delay(1000);
        digitalWrite(green_led, HIGH);
        delay(1000);
        digitalWrite(green_led, LOW);
        delay(1000);
        // key=0;
    }
}
