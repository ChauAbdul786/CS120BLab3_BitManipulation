/*	Author: Abdullah Chaudhry
 *  Partner(s) Name: 
 *	Lab Section: 021
 *	Assignment: Lab #3  Exercise #3
 *	Exercise Description: Fuel sensor on A3 - A0. C5 - C0 display the corresponding fuel level. C6 is a low fuel light that lights when the fuel is level 4 or less. A4 is 1 if key is in ignition A5 is 1 if driver is seated. A6 is 1 if the seatbelt is fastened. A7 should be 1 if the key is in ignition, driver is seated, and seatbelt is NOT fastened.
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
	DDRA = 0x00; PORTA = 0x00; 
	DDRC = 0xFF; PORTC = 0x00;

	/* Insert your solution below */
	unsigned char tmpA = 0x00;
	unsigned char tmpC = 0x00;

	while (1) {
		tmpA = PINA;

		unsigned char tmpALower4Bits = (tmpA & 0x0F);

		switch(tmpALower4Bits){
		case 0x00:
			tmpC = 0x40; //Fuel Level 0 => 0100 000
					//Not described in lab spec, assuming this is the intended behavior 
			break;
		case 0x01:
		case 0x02:
			tmpC = 0x60; //Fuel Level 1 or 2 => 0110 0000
			break;
		case 0x03:
		case 0x04:
			tmpC = 0x70;	//Fuel Level 3 or 4 => 0111 0000
			break;
		case 0x05:
		case 0x06:
			tmpC = 0x38; //Fuel Level 5 or 6 => 0011 1000
			break;
		case 0x07:
		case 0x08:
		case 0x09:
			tmpC = 0x3C; //Fuel Level 7 - 9 => 0011 1100
			break;
		case 0x0A:
		case 0x0B:
		case 0x0C:
			tmpC = 0x3E; //Fuel Level 10 - 12 => 0011 1110
			break;
		case 0x0D:
		case 0x0E:
		case 0x0F:
			tmpC = 0x3F; //Fuel Level 13 - 15 => 0011 1111
		default:
			tmpC = 0x3F; //If none of these cases, 
					//Fuel Level was likely mistakenly set > 15 => 0011 1111
			break;
		}

		unsigned char tmpAHigherBitsToCheck = (tmpA & 0x70);	

		if(tmpAHigherBitsToCheck == 0x30){
			tmpC = (tmpC | 0x80);
		}

	PORTC = tmpC;
	}

	return 1;
}
