import numpy as np
import pandas as pd

def variance(data):
    mean = sum(data) / len(data)
    total = 0
    for value in data:
        total += (value - mean) ** 2
    return total / len(data)

marks = [80, 50, 45, 91]
print('Variance of Marks is : ', variance(marks))

# Using Numpy
marks = [80, 50, 45, 91]
print('Variance Numpy is : ', np.var(marks))

# Using Pandas
marks = [80, 50, 45, 91]
series = pd.Series(marks)
print('Variance Pandas is : ', series.var())