#include <Wire.h>
#include <MPU6050.h>
bool relay_state = false;
bool befor_relay_state = false;
MPU6050 mpu; 
#define Pin 12
bool state = false;
#define vcc 11
float buffer_[2][100];
void get_data(){
  for (int i = 0; i < 100; i++) { //採集256點
      digitalWrite(vcc,LOW);
      digitalWrite(vcc,HIGH);
      mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G);
      Vector normAccel = mpu.readNormalizeAccel();
      buffer_[0][i]=normAccel.XAxis;
      buffer_[1][i]=normAccel.ZAxis;
  }
}
void send_data(){
  Serial.println("START");
  for(int i=0;i<100;i++){
      Serial.print(digitalRead(Pin) == LOW);
      Serial.print(" ");
      Serial.print(buffer_[0][i]);
      Serial.print(" ");
      Serial.println(buffer_[1][i]);
  }
}
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
  relay_state = !digitalRead(Pin);
  if (relay_state == true and befor_relay_state == false) { //如果PLC將電位拉低
    get_data();
    send_data();
  }
 befor_relay_state = relay_state;
}
