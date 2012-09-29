#pragma once
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

	void minimizeCost();



private:

	
	float *X,*Y;
	int dataSize;

	float getCost(float x,float y,float t0,float t1)
	{
		for(int i=0;i<dataSize;i++)
		{
				float _cost=0;
				_cost = _cost+ (0.5/dataSize)*(lin_hypothesis(x,t0,t1)-y)*(lin_hypothesis(x,t0,t1)-y);
				
		}
	}

	float lin_hypothesis(float x,float theta0,float theta1)
	{
		return (theta0+ x*theta1);
	}
};

