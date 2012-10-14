implementation of univariate linear regression with gradient decsent
-----------------------------------------------------------------------

--------> iterations are loop-based.
--------> Performance can be raised dramtically by using a vectorized matrix manipulation mechanism which is natively unavailable in C++
--------> Performance development is currently based on Armadillo C++ linear algebra library. http://arma.sourceforge.net/

float* LinReg::minimizeCost(float* x,float* y,float t0,float t1,float learningRate,int iterations); 

--------> This method returns an array of two elements with minimized parameter values after a given number of iterations of gradient decsent

float LinReg::getCost(float* x,float* y,float t0,float t1)

--------> This method calculates the overall square error over a given data point set(X) and an actual value set (Y)

M.P. Tharindu Rusira Kumara
30.9.2012 2.20 A.M. (GMT+ 0530)