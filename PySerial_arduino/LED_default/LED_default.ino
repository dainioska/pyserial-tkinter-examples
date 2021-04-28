//LED_default.py
//TKinter.py
//data input '1' is LED"ON"
//data input '0' is LED"OFF"

int LED = 13;
//int data;
char data;

void setup() {
  Serial.begin(9600);
  Serial.println("startas");
  pinMode(LED,OUTPUT);
  digitalWrite(LED,LOW);
}
void loop() {

  while(Serial.available()>0)
  {
    data = Serial.read();
  }
  if(data == '1')
  {
  digitalWrite(LED, HIGH);
  delay(10);
  Serial.println("LED on");
  }
  else if(data == '0')
  {
  digitalWrite(LED, LOW);
  delay(10);
  Serial.println("LED off");
 }
}
