// parseInt examples for testing 2021-04-06 

int dataIn;

void setup(){
  Serial.begin(9600);  
  Serial.print("kiek: ");
}

void loop(){
  //Serial.print("kiek: ");
  while (Serial.available() > 0)
 {
  dataIn = Serial.parseInt();
  Serial.print(dataIn);
 }
} 
