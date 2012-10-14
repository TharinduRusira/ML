'''
Created on Oct 15, 2012

@author: M.P.Tharindu Rusira Kumara, University of Moratuwa
'''



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
            
           
            from numpy import zeros
            from numpy import float64
            
            __array= zeros((__size,2),float64);
            
            f=open(__fpath, mode='r', buffering=1, encoding=None, errors=None, newline=None, closefd=True); 
            
            print('reading data from file....');
            for i in range(0,__size):
                
                line= f.readline();
                __firstValue= line[__firstValStart:__firstValEnd];
                __secondValue=line[__secondValStart:__secondValEnd];
                
                #print(__firstValue+'  '+__secondValue);
                __array[i,0]= __firstValue
                __array[i,1]= __secondValue;
                #print(__array[i,0],__array[i,1]);
             
            print('data reading complete....');
            
            return __array;
            
        except IOError:
            pass 
        
lr=LinearReg();
a=lr.readFile('data.txt',62);
print(a[1,0],a[1,1]);
 