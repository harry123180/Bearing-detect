#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;
int Pin = 12;
bool state = false;
int state2 =true;
int vcc =11;

void setup()
{
  pinMode(vcc,OUTPUT);
  digitalWrite(vcc,HIGH);
  Serial.begin(115200);
  digitalWrite(2, HIGH);
  pinMode(2, OUTPUT);
  pinMode(Pin, INPUT);
  Serial.println("Initialize MPU6050");
  while (!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    delay(500);
  }
}


void loop()
{
  if (digitalRead(Pin) == LOW) {
    state = true;
  }
  else if (digitalRead(Pin) == HIGH) {
    state = false;
  }
  if (state) { //如果PLC將電位拉低

    Serial.println("START");
    for (int i = 0; i < 256; i++) { //採集256點
      
      digitalWrite(vcc,LOW);
      digitalWrite(vcc,HIGH);
      mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G);
      Vector normAccel = mpu.readNormalizeAccel();
      Serial.print(digitalRead(Pin) == LOW);
      Serial.print(" ");
      Serial.print(normAccel.XAxis);
      Serial.print(" ");
      Serial.print(normAccel.YAxis);
      Serial.print(" ");
      Serial.println(normAccel.ZAxis);
      delay(10);
    }
 

  }
}
