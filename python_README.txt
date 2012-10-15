@Author M.P. Tharindu Rusira Kumara, tharindurusira@gmail.com

data resource 

REGRESSION - Linear Regression Test Data
http://orion.math.iastate.edu/burkardt/data/regression/regression.html

									data file format
								 -----------------------
								| index value1 value2   |
								|                       |
								 -----------------------

	 ====================================================================================
	|	The idea here is, we are trying to find an optimal linear decision boundary      |
	|	which seperates a data set given that the data are linearly seperable.           |
	|	                                                                                 |
	|	Objective: find an optimal set of parameters t0,t1                               | 
	|	           such that t0+ t1*X = Y separates the whole data set into two classes. |  
	|																					 |
    |   Procedure: We calculate the overall square cost over the training data set and   |
	|	           minimize the cost using gradient decsent algorithm.					 | 
    |                                                                 					 |
	|	Outcome: the algorithm is capable of predicting the Y value of a new data point  |
	|====================================================================================|
