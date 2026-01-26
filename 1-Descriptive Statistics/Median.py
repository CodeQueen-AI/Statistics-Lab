import numpy as np
import pandas as pd

# Median
def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (data[n//2 - 1] + data[n//2]) / 2
    return data[n//2]

# Marks
marks = [80, 50, 45, 91]
print('Median of Marks is : ' , median(marks))

# Using Numpy
marks = [80, 50, 45, 91]
print('Median of Marks (Numpy) is : ' , np.median(marks))

# Using Pandas
marks = [80, 50, 45, 91]
marks_series = pd.Series(marks)
print('Median of Marks (Pandas) is : ' , marks_series.median())