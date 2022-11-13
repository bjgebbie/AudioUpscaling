class linearSpline:
    def __init__(self, X, Y, precision):
        self.points = []
        for j in range (len(X)): 
            for i in range (precision - 1):
                ls = Y[j] + (Y[j+1] - Y[j])/(X[j+1] - X[j]) * ((1/precision) - X[j])
                precision = 
       
   


            
    