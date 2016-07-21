#include "LedControl.h"

LedControl lc = LedControl(12, 11, 10, 1);


byte recData[8];


void setup() {
  Serial.begin(38400);
  
  // put your setup code here, to run once:
  lc.shutdown(0,false);
  /* Set the brightness to a medium values */
  lc.setIntensity(0,4);
  /* and clear the display */
  lc.clearDisplay(0);

}

void loop() {
  // put your main code here, to run repeatedly:

  while ( Serial.available() >= 8 ){
    for(int i = 0 ; i < 8 ; i++){
       //recData[i] = Serial.read();
       lc.setRow(0, i, Serial.read());
    }
      
}
    



}
