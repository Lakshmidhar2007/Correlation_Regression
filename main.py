import numpy as np
import matplotlib.pyplot as plt

# Getting Inputs
print("Enter the values of X separated by space")
X = np.array([int(i) for i in input().split()])

print("Enter the values of Y separated by space")
Y = np.array([int(i) for i in input().split()])

N = len(X)
print(X, Y, N, sep='\n')

# Calculating Sums and Means
SumX = np.sum(X)
SumY = np.sum(Y)
SumX2 = np.sum(X**2)
SumY2 = np.sum(Y**2)
SumXY = np.sum(X * Y)

MeanX = SumX / N
MeanY = SumY / N

# Calculating Regression Coefficient
num = (N * SumXY) - (SumX * SumY)
den = (N * SumX2) - (SumX**2)
RegressionCoef = num / den

# Regression Line Equation
print(f"The Regression Y on X is Y = {RegressionCoef:.3f} ( X - {MeanX:.3f}) + {MeanY:.3f}")

# Define Regression Function
def Regression(x):
    return MeanY + (RegressionCoef * (x - MeanX))

# Plotting the Graph
plt.scatter(X, Y)
plt.plot(X, Regression(X))
plt.xlabel("X-Data")
plt.ylabel("Y-Data")
plt.legend(['Data points', 'Regression Line'])
plt.show()