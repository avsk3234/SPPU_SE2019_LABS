#include <Arduino.h>
#include "DHT.h"
#define DHTPIN 12     // what pin we're connected to
#define DHTTYPE DHT11 // DHT 11
// Initialize DHT sensor for normal 16mhz Arduino
DHT dht(DHTPIN, DHTTYPE);
void setup()
{
    // put your setup code here, to run once:
    Serial.begin(9600);
    // Serial.println("DHT-11 test!");
    dht.begin();
}
void loop()
{
    // put your main code here, to run repeatedly:
    // Wait a few seconds between measurements.
    delay(500);
    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    // Read temperature as Fahrenheit
    float f = dht.readTemperature(true);
    // Check if any reads failed and exit early (to try again).
    if (isnan(f))
    {
        Serial.println("Failed to read from DHT sensor!");
        return;
    }
    Serial.println(f);
}