#include <DHT.h>

#define DHT1PIN 2 // Pin for DHT11 sensor 1
#define DHT2PIN 3 // Pin for DHT11 sensor 2
#define DHT3PIN 4 // Pin for DHT11 sensor 3

DHT dht1(DHT1PIN, DHT11);
DHT dht2(DHT2PIN, DHT11);
DHT dht3(DHT3PIN, DHT11);

void setup() {
  Serial.begin(9600); // Initialize serial communication
  dht1.begin(); // Initialize DHT11 sensor 1
  dht2.begin(); // Initialize DHT11 sensor 2
  dht3.begin(); // Initialize DHT11 sensor 3
}

void loop() {
  float t1 = dht1.readTemperature(); // Read temperature from sensor 1
  float h1 = dht1.readHumidity(); // Read humidity from sensor 1
  float t2 = dht2.readTemperature(); // Read temperature from sensor 2
  float h2 = dht2.readHumidity(); // Read humidity from sensor 2
  float t3 = dht3.readTemperature(); // Read temperature from sensor 3
  float h3 = dht3.readHumidity(); // Read humidity from sensor 3
  
  Serial.print("Temperature 1: ");
  Serial.print(t1);
  Serial.print(" °C, Humidity 1: ");
  Serial.print(h1);
  Serial.print("%\t");

  Serial.print("Temperature 2: ");
  Serial.print(t2);
  Serial.print(" °C, Humidity 2: ");
  Serial.print(h2);
  Serial.print("%\t");

  Serial.print("Temperature 3: ");
  Serial.print(t3);
  Serial.print(" °C, Humidity 3: ");
  Serial.print(h3);
  Serial.println("%");

  delay(10000); // Wait for 10 seconds
}
