import numpy as np
"""
    Interpolates using the r-Cubic Spline method
    Input:
        X = List of all the X values
        Y = List of all the Y values
    Output: 
        coef = Sets a list of all the coefcients need to call the interpolate method
"""
class CubicSpline:
    def __init__(self, X, Y):
        self.coef = []
        self.X = X
        self.Y = Y
        self.n = len(X)

      
        r = 3.732
        h = X[1] - X[0]

        # Generate E matrix
        E = []
        for i in range(self.n - 1):  
            m = 0 
            result = 0
            if i == 0: 
                m = (3 * r) / (2 * h)
                result = m * ((Y[i + 1] - Y[ i ]) / h)
                E.append(result)
            else: 
                m = 3 / (h * h)
                result = m * (Y[i - 1] - (2 * Y[i]) + Y[i + 1])
                E.append(result)
        E.append(0)

        # Generate alpha matrix
        A = []
        for i in range(self.n - 1):
            if i == 0:
                A.append(E[i] / r)
            else:
                A.append((E[i] - A[i - 1])/r)
        A.append(0)

        # Generate c matrix
        C = [0]
        for i in range(self.n-1):
            j = self.n - i - 1
            result = A[j-1] - C[i] / r
            C.append(result)
        C.reverse()

        # Generate B matrix
        B = []
        for i in range(self.n-1):
            result = ((Y[i+1] - Y[i]) / h)\
                     - (((2 * C[i] + C[i+1]) / 3) * h)
            B.append(result)
            
        # Generate d matrix
        D = []
        for i in range(self.n-1):
            result = 1 / (3 * h) * (C[i+1]-C[i])
            D.append(result)
        self.coef.append(C)
        self.coef.append(B)
        self.coef.append(D)

    """
        Interpolate between 2 given points x.
        Input:
            idx = The idx of the X-th element
            t = x input that you are interpolating between the X_i and X_i+1
        Output:
            ans = The Y value associated with t
    """
    def interpolate(self, idx, t):
                 
        ans = self.Y[idx] + self.coef[1][idx] * (t - self.X[idx])\
                          + self.coef[0][idx] * np.power((t - self.X[idx]), 2)\
                          + self.coef[2][idx] * np.power((t - self.X[idx]), 3)
        return ans
