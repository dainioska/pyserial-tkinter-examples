#include<Servo.h>

Servo servoVer; //Vertical Servo
Servo servoHor; //Horizontal Servo

int x;
int y;

int prevX;
int prevY;

void setup()
{
  Serial.begin(9600);
  servoVer.attach(5); //Attach Vertical Servo to Pin 5
  servoHor.attach(6); //Attach Horizontal Servo to Pin 6
  servoVer.write(70);
  servoHor.write(90);
  delay(2000);
}

void Pos()
{
  if(prevX != x || prevY != y)
  {
    //tune this range to generate map
    int servoX = map(x, 600, 0, 100, 80); 
    //tune this range to generate map
    int servoY = map(y, 450, 0, 90, 60); 

    servoX = min(servoX, 100);
    servoX = max(servoX, 80);
    servoY = min(servoY, 90);
    servoY = max(servoY, 60);

    servoHor.write(servoX);
    delay(50);  
    servoVer.write(servoY);
    delay(50);
  }
}

void loop()
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if(Serial.read() == 'Y')
      {
        y = Serial.parseInt();
       Pos();
       delay(50);
      }
    }
    while(Serial.available() > 0)
    {
      Serial.read();
    }
  }
}
