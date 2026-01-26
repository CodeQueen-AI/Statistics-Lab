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

# Using Numpy
marks = [80, 50, 45, 91]
print('Mean of Marks (Numpy) is : ' , np.mean(marks))

# Using Pandas
marks = [80, 50, 45, 91]
marks_series = pd.Series(marks)
print('Mean of Marks (Pandas) is : ' , marks_series.mean())

# Median
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted)

