// color swirl! connect an RGB LED to the PWM pins as indicated
// in the #defines
// public domain, enjoy!
 
#define REDPIN 9
#define GREENPIN 10
#define BLUEPIN 11
#define FADESPEED 5     // make this higher to slow down


int colorRGB[3];
int redPin = 10;
int greenPin = 9;
int bluePin = 11;

int delayVal = 50;
int blnFade = 0;
int h_int;
float h;
int r=0, g=0, b=0;

void setup() {
  Serial.begin(9600);
  
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
}
 
 
void loop() {
//  if (Serial.available()){
   if(Serial.available() >= 2){
     switch( byte( Serial.read() )) {
       case 'r':
         colorRGB[0] = Serial.read();
         blnFade = 0;
         break;
       case 'g':
         colorRGB[1] = Serial.read();
         blnFade = 0;
         break;   
       case 'b':
         colorRGB[2] = Serial.read();
         blnFade = 0;
         break;
       case 'c':
         Serial.flush();
         blnFade = 0;
         break;
       case 'f':
         delayVal = Serial.read();
         Serial.flush();
  //       colorFade();
         blnFade = 1;
    }
  }
  analogWrite(redPin, colorRGB[0]); 
  analogWrite(greenPin, colorRGB[1]);
  analogWrite(bluePin, colorRGB[2]);
  delay(20);
  
//    int r, g, b;
//   
//    // fade from blue to violet
//    for (r = 0; r < 256; r++) { 
//      analogWrite(REDPIN, r);
//      analogWrite(GREENPIN, r);
//      analogWrite(BLUEPIN, r-20);
//      delay(FADESPEED);
//    } 
//    // fade from violet to red
//    for (b = 255; b > 0; b--) { 
//      analogWrite(REDPIN, b);
//      analogWrite(GREENPIN, b);
//      analogWrite(BLUEPIN, b);
//      delay(FADESPEED);
//    }
//  }
}
