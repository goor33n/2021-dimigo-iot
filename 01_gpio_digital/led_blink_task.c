#include <wiringPi.h>
#include <stdio.h>
#define LED_RED 4
#define LED_GRE 17
#define LED_YEL 22
int main (void)
{
  // wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED_RED, OUTPUT) ; // OUTPUT
  pinMode (LED_GRE, OUTPUT) ;
  pinMode (LED_YEL, OUTPUT) ;
  // LED ON OFF
  digitalWrite (LED_RED, HIGH) ; delay (2000) ;
  digitalWrite (LED_RED,  LOW) ;
  digitalWrite (LED_GRE, HIGH) ; delay (2000) ;
  digitalWrite (LED_GRE,  LOW) ;
  digitalWrite (LED_YEL, HIGH) ; delay (2000) ;
  digitalWrite (LED_YEL,  LOW) ;
  
  pinMode (LED_RED, INPUT) ; // INPUT
  pinMode (LED_GRE, INPUT) ;
  pinMode (LED_YEL, INPUT) ;
  
  return 0 ;
}
