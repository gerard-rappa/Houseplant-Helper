#include <dht.h>
#define DHT11_PIN 3
dht DHT;

void setup(){

  Serial.begin(9600);
}
void loop()
{
  int soil = analogRead(0);
  int chk = DHT.read11(DHT11_PIN);
  
  //Soil Moisture Sensor
  Serial.println(soil);
  
  //Temp/Humidity Sensor
  //Celsius to Farenheit conversion
  Serial.println((DHT.temperature * 1.8) + 32);
  Serial.println(DHT.humidity);
  delay(2000);
}
