/*	Author: Abdullah Chaudhry
 *  Partner(s) Name: 
 *	Lab Section: 021
 *	Assignment: Lab #3  Exercise #1
 *	Exercise Description: Count the number of 1s on ports A and B and output that number on port C
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
	DDRA = 0x00; PORTA = 0xFF;
	DDRB = 0x00; PORTB = 0xFF;
	DDRC = 0xFF; PORTC = 0x00;

	/* Insert your solution below */
	unsigned char tmpA = 0x00;
	unsigned char tmpB = 0x00;
	unsigned char tmpC = 0x00;
	unsigned char cnt = 0;
	while (1) {
		tmpA = PINA;
		tmpB = PINB;
		cnt = ((tmpA & 0x80) >> 7) + ((tmpA & 0x40) >> 6) + 
					((tmpA & 0x20) >> 5) + ((tmpA & 0x10) >> 4) + 
					((tmpA & 0x08) >> 3) + ((tmpA & 0x04) >> 2) + 
					((tmpA & 0x02) >> 1) + ((tmpA & 0x01)) + 
					((tmpB & 0x80) >> 7) + ((tmpB & 0x40) >> 6) + 
					((tmpB & 0x20) >> 5) + ((tmpB & 0x10) >> 4) + 
					((tmpB & 0x08) >> 3) + ((tmpB & 0x04) >> 2) + 
					((tmpB & 0x02) >> 1) + ((tmpB & 0x01));

		tmpC = cnt;
		PORTC = tmpC;		
	}
	return 1;
}
