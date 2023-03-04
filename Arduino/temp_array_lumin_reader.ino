#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_TSL2591.h"

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591);

void displaySensorDetails(void) {
  sensor_t sensor;
  tsl.getSensor(&sensor);
  Serial.println("--------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" lux");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" lux");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" lux");  
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}

int deviceCount = 0;
float tempC;

float tempSensor1, tempSensor2, tempSensor3, tempSensor4, tempSensor5, tempSensor6, lum;

uint8_t sensor1[8] = { 0x28, 0xFF, 0x47, 0x0E, 0xC1, 0x16, 0x05, 0x64 };
uint8_t sensor2[8] = { 0x28, 0xE7, 0xB7, 0x1E, 0x0B, 0x00, 0x00, 0x40 };
uint8_t sensor3[8] = { 0x28, 0xBF, 0x45, 0x1F, 0x0B, 0x00, 0x00, 0x65 };
uint8_t sensor4[8] = { 0x28, 0x1E, 0x86, 0x1E, 0x0B, 0x00, 0x00, 0xED };
uint8_t sensor5[8] = { 0x28, 0xF0, 0xC1, 0x1D, 0x0B, 0x00, 0x00, 0xE7 };
uint8_t sensor6[8] = { 0x28, 0x28, 0x2F, 0x1E, 0x0B, 0x00, 0x00, 0x72 };

void configureSensor(void) {
  // tsl.setGain(TSL2591_GAIN_LOW);
  // tsl.setGain(TSL2591_GAIN_MED);
  // tsl.setGain(TSL2591_GAIN_HIGH);

//  tsl.setTiming(TSL2591_INTEGRATIONTIME_100MS); // Shortest Integration time (bright light);
//  tsl.setTiming(TSL2591_INTEGRATIONTIME_200MS);
//  tsl.setTiming(TSL2591_INTEGRATIONTIME_300MS);
//  tsl.setTiming(TSL2591_INTEGRATIONTIME_400MS);
//  tsl.setTiming(TSL2591_INTEGRATIONTIME_500MS);
  tsl.setTiming(TSL2591_INTEGRATIONTIME_600MS); // Longest integration time (dim light);

//  Serial.println("----------------------------------");
//  Serial.print("Gain:       ");
  tsl2591Gain_t gain = tsl.getGain();
//  switch(gain)
//  {
//    case TSL2591_GAIN_LOW:
//      Serial.println("1x (Low)");
//      break;
//    case TSL2591_GAIN_MED:
//      Serial.println("25x (Medium)");
//      break;
//    case TSL2591_GAIN_HIGH:
//      Serial.println("428x (High)");
//      break;
//    case TSL2591_GAIN_MAX:
//      Serial.println("9876x (Max)");
//      break;
//  }

//  Serial.print("Timing:       ");
//  Serial.print((tsl.getTiming()+1)*100, DEC);
//  Serial.print(" ms");
//  Serial.println("-------------------------");
//  Serial.println("");
}

float simpleRead(void) {
  uint16_t x = tsl.getLuminosity(TSL2591_VISIBLE);
  //uint16_t x = tsl.getLuminosity(TSL2591_FULLSPECTRUM);
  //uint16_t x = tsl.getLuminosity(TSL2591_INFRARED);
//  Serial.print("[ "); Serial.print(millis()); Serial.print(" ms ]");
//  Serial.print("Luminosity: ");
//  Serial.println(x, DEC);

  return x;
}

void advancedRead(void)
{
  // More advanced data read example. Read 32 bits with top 16 bits IR, bottom 16 bits full spectrum
  // That way you can do whatever math and comparisons you want!
  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir, full;
  ir = lum >> 16;
  full = lum & 0xFFFF;
  Serial.print("[ "); Serial.print(millis()); Serial.print(" ms ] ");
  Serial.print("IR: "); Serial.print(ir);  Serial.print("  ");
  Serial.print("Full: "); Serial.print(full); Serial.print("  ");
  Serial.print("Visible: "); Serial.print(full - ir); Serial.print("  ");
  Serial.print("Lux: "); Serial.println(tsl.calculateLux(full, ir));
}

void unifiedSensorAPIRead(void)
{
  /* Get a new sensor event */ 
  sensors_event_t event;
  tsl.getEvent(&event);
 
  /* Display the results (light is measured in lux) */
  Serial.print("[ "); Serial.print(event.timestamp); Serial.print(" ms ] ");
  if ((event.light == 0) |
      (event.light > 4294966000.0) | 
      (event.light <-4294966000.0))
  {
    /* If event.light = 0 lux the sensor is probably saturated */
    /* and no reliable data could be generated! */
    /* if event.light is +/- 4294967040 there was a float over/underflow */
    Serial.println("Invalid data (adjust gain or timing)");
  }
  else
  {
    Serial.print(event.light); Serial.println(" lux");
  }
}

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  delay(100);

  // Thermistor array setup
  sensors.begin();
//  Serial.println("Locating Devices");
//  Serial.print("Found ");
//  deviceCount = sensors.getDeviceCount();
//  Serial.print(deviceCount, DEC);
//  Serial.println( " devices.");
//  Serial.println("");  

  // Luminosity Sensor setup
  if (tsl.begin()) {
    
  }
  else {
    Serial.println("No TSL2591 sensor found... check the wiring?");
  }

  //displaySensorDetails();
  configureSensor();
}

void loop() {
  // put your main code here, to run repeatedly:
  sensors.requestTemperatures();
  tempSensor1 = sensors.getTempC(sensor1); // Gets the values of the temperature
  tempSensor2 = sensors.getTempC(sensor2); // Gets the values of the temperature
  tempSensor3 = sensors.getTempC(sensor3); // Gets the values of the temperature
  tempSensor4 = sensors.getTempC(sensor4); // Gets the values of the temperature
  tempSensor5 = sensors.getTempC(sensor5); // Gets the values of the temperature
  tempSensor6 = sensors.getTempC(sensor6); // Gets the values of the temperature
  lum = simpleRead();

  Serial.print(tempSensor1);
  Serial.print(", ");
  Serial.print(tempSensor2);
  Serial.print(", ");
  Serial.print(tempSensor3);
  Serial.print(", ");
  Serial.print(tempSensor4);
  Serial.print(", ");
  Serial.print(tempSensor5);
  Serial.print(", ");
  Serial.print(tempSensor6);
  Serial.print(", ");
  Serial.print(lum);
  Serial.println();

  delay(1000UL*60*10);
}
