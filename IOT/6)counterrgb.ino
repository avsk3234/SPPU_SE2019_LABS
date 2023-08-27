const int green_led = 10;
const int blue_led = 9;
const int red_led = 11;
unsigned int counter;
void setup()
{
    // put your setup code here, to run once:
    pinMode(green_led, OUTPUT);
    pinMode(red_led, OUTPUT);
    pinMode(blue_led, OUTPUT);
}
void loop()
{
    counter = counter + 1;
    delay(50);
    if (counter <= 100) // Gree LED High
    {
        digitalWrite(green_led, HIGH);
        digitalWrite(blue_led, LOW);
        digitalWrite(red_led, LOW);
    }
    else if ((counter > 100) && (counter <= 200)) // blue LED High
    {
        digitalWrite(green_led, LOW);
        digitalWrite(blue_led, HIGH);
        digitalWrite(red_led, LOW);
    }
    else if (counter > 200) // red LED High
    {
        digitalWrite(green_led, LOW);
        digitalWrite(blue_led, LOW);
        digitalWrite(red_led, HIGH);
    }
    if (counter > 250)
        counter = 0;
}
