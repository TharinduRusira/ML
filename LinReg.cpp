#include "LinReg.h"
#include<iostream>
#include<math.h>

using namespace std;


LinReg::LinReg(void)
{
}


LinReg::~LinReg(void)
{
}

void LinReg::setData(float* x,float* y,int size)
{
	X=x;
	Y=y;
	dataSize=size;
}

float LinReg::getCost(float* x,float* y,float t0,float t1)
{
	/* implements the cost function and return the cost for a given x-y pair under given t parameters */

	float _cost=0; // overall cost
	float _costi; // cost for the i th data-value pair

	for(int i=0;i<dataSize;i++)
	{
		_costi=(t0+ t1* (*(x+i*sizeof(float)))- *(y+i*sizeof(float)));
		_cost= _cost + _costi*_costi; 
	}

	return _cost;
}

float* LinReg::minimizeCost(float* x,float* y,float t0,float t1,float learningRate,int iterations)
{
	
	/* implements the minimizing function of cost using gradient decsent 
		learningRate is given, 
		number of iterations is given, 
		initial guesss for parameters is given 

		assumption: parameters reach it's lowest values within the given number of iterations
		or in other words,
		number of iterations are enough to obtain a reasonable values for parameters
	*/
	float result[2]; // holds final values of t0 and t1 respectively

	float _tempt0,_tempt1;

	for(int i=0;i<iterations;i++)
	{
		_tempt0= t0;
		_tempt1=t1;

		float gradt0=0,gradt1=0;

		for(int j=0;j<dataSize;j++)
		{
			/* gradients are calculated inside the for loop */

			gradt0 = gradt0 + (t0+ t1* (*(x+j*sizeof(float)))- *(y+j*sizeof(float)));
			gradt1= gradt1+ (t0+ t1* (*(x+j*sizeof(float)))- *(y+j*sizeof(float)))* (*(x+j*sizeof(float)));
		}

		t0= t0 - (learningRate/dataSize)* gradt0;
		t1= t1 - (learningRate/dataSize)* gradt1;
				
	}

	result[0]= t0;
	result[1]= t1;

	return result;
	
}