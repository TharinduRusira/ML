'''
Created on Oct 15, 2012

@author: M.P.Tharindu Rusira Kumara, University of Moratuwa
'''
import numpy;
import sys;

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
            
            f=open(__fpath, mode='r', buffering=1, encoding=None, errors=None, newline=None, closefd=True); 
            
            print('reading data from file....');
            for i in range(0,__size):
                
                line= f.readline();
                __firstValue= line[__firstValStart:__firstValEnd];
                __secondValue=line[__secondValStart:__secondValEnd];
                
                print(__firstValue+'  '+__secondValue);
             
            print('data reading complete....');
            
        except IOError:
            pass 
        
lr=LinearReg();
lr.readFile('data.txt',62);
 