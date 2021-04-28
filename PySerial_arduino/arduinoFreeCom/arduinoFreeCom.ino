//read data from analogPin0 and print
//used to arduFreeCom.py

int analogPin = 0;     
int data = 0; 
char userInput;          

void setup(){
  Serial.begin(9600);  //setup serial
  Serial.println("Startas");
}

void loop(){
      data = analogRead(analogPin);  //read the input analogPin
      //Serial.print(data);
      Serial.print(analogPin);
      Serial.println(data);
      delay(500);
} 
