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

lc.setRow(0, 0, 54);
lc.setRow(0, 1, 73);
lc.setRow(0, 2, 65);
lc.setRow(0, 3, 34);
lc.setRow(0, 4, 34);
lc.setRow(0, 5, 54);
lc.setRow(0, 6, 20);
lc.setRow(0, 7, 8);
      
    



}
