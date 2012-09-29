#include "LinReg.h"
#include<iostream>

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

void LinReg::minimizeCost()
{
	

	
}