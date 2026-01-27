def variance(data):
    mean = sum(data) / len(data)
    total = 0
    for value in data:
        total += (value - mean) ** 2
    return total / len(data)

marks = [80, 50, 45, 91]
print('Variance of Marks is : ', variance(marks))

import numpy as np
marks = [80, 50, 45, 91]
print('Variance Numpy is : ', np.var(marks))

import pandas as pd
marks = [80, 50, 45, 91]
print('Variance Numpy is : ', np.var(marks))
