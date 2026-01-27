def mode(data):
    return max(data, key=data.count)

marks = [80, 50, 45, 91]
print('Mean of Marks is : ' , mode(marks))


import numpy as np
import pandas as pd

# Using NumPy
data = [2, 4, 6, 4, 8, 10]
print('Mode Numpy is : ', np.bincount(data.argmax()))

# Using Pandas
data = [2, 4, 6, 4, 8, 10]
series = pd.Series(data)
print('Mode Pandas is : ', series.mode()[0])