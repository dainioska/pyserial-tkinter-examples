//check condition Serial.available()>0
//read data from analogPin0 and print if condition CHAR 'z' or STRING "zzz" is true
//used together with arduSerialCom01.py 
  
int analogPin = 0;     
int data = 0;           
char userInput;
String str;

void setup(){
  Serial.begin(9600);  
}

void loop(){

if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'z'){                  // if we get expected value 

            data = analogRead(analogPin);    // read the input pin
            Serial.println(data);   
            delay(500);                    
  } 
 } 
} 
