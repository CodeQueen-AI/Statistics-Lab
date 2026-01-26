import numpy as np
import pandas as pd

def my_sum(data):
    result = 0
    for value in data:
        result += value
    return result

def mean(data):
    return my_sum(data) / len(data)

# Marks
marks = [80, 50, 45, 91]
print('Mean of Marks is : ' , mean(marks))

# Steps
steps = [4000, 5000, 6000, 7000, 8000]
print('Mean of Steps is : ', mean(steps))

# Using Numpy
marks = [80, 50, 45, 91]
print('Mean of Marks (Numpy) is : ' , np.mean(marks))