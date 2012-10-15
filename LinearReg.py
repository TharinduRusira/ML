'''
Created on Oct 15, 2012

@author: M.P.Tharindu Rusira Kumara, University of Moratuwa
'''
from numpy.core.numeric import zeros, arange, ones, dot
from numpy.matrixlib.defmatrix import matrix




class LinearReg(object):
    '''
    classdocs
    '''

    

    def __init__(self):
        '''
        Constructor
        '''
        
    def readFile(self, filePath,fileSize):
        '''
            
            file format
            ---------------------------
            index1    xx.xxx    yy.yyy
            index2    xx.xxx    yy.yyy
            index3    xx.xxx    yy.yyy
            ---------------------------
            
            we eliminate the 'index' and extract two values into a set.
            
        '''
        
        
        try:
            __fpath=filePath; # path of the file
            __size=fileSize; # number of data items in file
            
            # these values may subject to change depending on the data.txt format
            __firstValStart=2;
            __firstValEnd=12;
            __secondValStart=13;
            __secondValEnd=22;
            
           
            
            from numpy import float64
            
            # 3 columns. bias value, first value, second value 
            
            __array= ones((__size,3),float64);
            
            f=open(__fpath, mode='r', buffering=1, encoding=None, errors=None, newline=None, closefd=True); 
            
            print('reading data from file....');
            for i in range(0,__size):
                
                line= f.readline();
                __firstValue= line[__firstValStart:__firstValEnd];
                __secondValue=line[__secondValStart:__secondValEnd];
                
                
                __array[i,1]= __firstValue
                __array[i,2]= __secondValue;
                #print(__array[i,1],__array[i,2]);
             
            print('data reading complete....');
            
            return __array;
            
        except IOError:
            pass 
        
        
    def linReg(self,arr):
        __matrix=arr;
        
        # public code goes here
        
    
    
    def __computeCost(self,mat,para=zeros((1,2))): 
        # if para is not overridden with custom initial values, use zeros
        # cost computation code goes here
        
        __cost=0.0;
        __size= mat[:,1].size;
        
        for i in mat:
            __cost=__cost + (dot(mat[i,0:2],para)- mat[i,2])**2;
            
            
        __cost= __cost/(2*__size);
        
        return __cost;
           
    
    def __gradientDecent(self,datamat,para=zeros((1,2)),learningRate=1,iterNum=500):
        # optimization code goes here 
        
        __size= datamat[:,1].size;
        __parameterVector= para;
        
        print("Gradient Descent is finding optimal parameters");
        for i in range (0,iterNum):
            __t0= __parameterVector[0];
            __t1= __parameterVector[1];
            
            __t0= __t0 - (learningRate/__size)*(dot(datamat[i,0:2],__parameterVector)- datamat[i,2]);
            __t1= __t1 - (learningRate/__size)* (dot(datamat[i,0:2],__parameterVector)- datamat[i,2])*datamat[i,1];
            
            __parameterVector[0]=__t0;
            __parameterVector[1]=__t1;
            
        minPara= (__t0,__t1);
        
        print("Gradient Descent is complete");
        return minPara;
    
          


