#include <wiringPi.h>
#define LED_PIN 4
int main (void)
{
  // wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED_PIN, OUTPUT) ;
  for (int i=0; i<10; i++)
  {
    digitalWrite (LED_PIN, HIGH) ; delay (200) ;
    digitalWrite (LED_PIN,  LOW) ; delay (200) ;
  }
  return 0 ;
}
