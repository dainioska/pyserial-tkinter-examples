
void setup() {
Serial.begin(9600);
Serial.println("Ready"); 
}
void loop() {
char inByte = ' ';

if(Serial.available()){ 
char inByte = Serial.read(); // read the incoming data
Serial.println(inByte); // send the data back in a new line so that it is not all one long line
}
delay(100); // delay for 1/10 of a second
}
