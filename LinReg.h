#pragma once


/* 
	Univariate linear regression model implemented by M.P. Tharindu Rusira Kumara
	Gradient Descent method is used for minimizing the square error of the hypothesis. 
*/


class LinReg
{
public:
	LinReg(void);
	~LinReg(void);

	void setData(float* x, float* y,int size);
	
	float* getX(){
		return X;
	}

	float* getY(){
		return Y;
	}

	int getSize(){
		return dataSize;
	}

	float getCost(float *x,float *y,float t0,float t1); // implements cost function
	
	float* minimizeCost(float* x,float* y,float t0,float t1,float learningRate,int iterations); // this method implements gradient decsent to minimize the cost and hence find optimum theta values 

	



private:

	
	float *X,*Y;
	int dataSize;

	

	
};

