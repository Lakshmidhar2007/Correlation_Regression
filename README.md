# Correlation and regression for data analysis
# Aim : 

To analyse given data using coeffificient of correlation and regression line
![image](https://user-images.githubusercontent.com/104613195/168224136-d6b64e64-7d3d-4775-9337-c8f96fe41f2d.png)


# Software required :  

Python

# Theory:

Correlation describes the strength of an association between two variables, and is completely symmetrical, the correlation between A and B is the same as the correlation between B and A. However, if the two variables are related it means that when one changes by a certain amount the other changes on an average by a certain amount.  

If y represents the dependent variable and x the independent variable, this relationship is described as the regression of y on x. The relationship can be represented by a simple equation called the regression equation. The regression equation representing how much y changes with any given change of x can be used to construct a regression line on a scatter diagram, and in the simplest case this is assumed to be a straight line.

# Procedure :

![image](https://user-images.githubusercontent.com/104613195/168225866-ac8f6610-bdc3-4ac2-a24e-2b24ba08e189.png)

# Program :

```py
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
```


# Result

![alt text](image.png)

# Output 
