int a;
void setup()
{
    Serial.begin(9600);
    Serial.println("Please Enter the number for Square= ");
}
void loop()
{
    if (Serial.available() > 0)
    {
        a = Serial.parseInt();
        // a=Serial.readString().toInt();
        Serial.println(a);
        a = a * a;
        // a=sq(a);
        Serial.println("Square of Entered number is= ");
        Serial.println(a);
    }
}