int val;
int tempPin = 0;



void setup()
{
Serial.begin(9600);
}

void loop()
{
val = analogRead(tempPin);
float mv = ( val/1024.0)*5000; 
float cel = mv/10;
if(cel>=22.00){
Serial.println(cel);
}
delay(1000);
}
