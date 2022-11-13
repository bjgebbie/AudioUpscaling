import numpy as np

class PiecewiseLinear:
    def __init__(self, X, Y, precision):
        self.data = np.array([0,0])
        
        for j in range (len(X)-5): 
            c = 0
            self.data = np.vstack([self.data, [Y[j],Y[j]]])
            for i in range (precision - 1):
                c = 1/precision + c
                c = round(c , 1)
                ls = Y[j] + ((Y[j+1] - Y[j])/(X[j+1] - X[j])) * (c) 
                t = [ls, ls]
                self.data = np.vstack([self.data, t])
                
             
               
               
            


       
   


            
    
