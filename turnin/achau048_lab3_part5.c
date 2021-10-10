/*	Author: Abdullah Chaudhry
 *  Partner(s) Name: 
 *	Lab Section: 021
 *	Assignment: Lab #3  Exercise #5
 *	Exercise Description: 
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
	/* Insert DDR and PORT initializations */
	DDRD = 0x00; PORTD = 0xFF; 
	DDRB = 0xFE; PORTB = 0x00;

	/* Insert your solution below */
	unsigned char tmpD = 0x00;
	unsigned char tmpB = 0x00;
	unsigned short totalWeight = 0;

	while (1) {
		tmpD = PIND;
		tmpB = PINB;

		totalWeight = ((tmpD << 1) | (tmpB & 0x01));

		if(totalWeight > 70){
			tmpB = (tmpB | 0x02);
		}else if(totalWeight > 5){
			tmpB = (tmpB | 0x04);
		}

		PORTB = tmpB;
	}
	return 1;
}
