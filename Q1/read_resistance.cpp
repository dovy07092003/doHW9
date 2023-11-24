// Name: read_resistance.cpp
// This file determine the value of the bottom resistor in a voltage divider

#include "AnalogIn.h"

int main(int argc, char *argv[])
{
	AnalogIn P9_39(0);
	short int num_pin = P9_39.getNumber();
	cout <<"The number of the pin is " <<num_pin<<endl;
	short int adc_value = P9_39.readAdcSample();
	cout <<"The analog to digital value of the pin is "<<adc_value<<endl;
	int r_value = -((adc_value - 1.8)*1/10000)/adc_value;
	r_value = 1/r_value;
	cout <<"The resistor value is "<<r_value<<endl;


}

