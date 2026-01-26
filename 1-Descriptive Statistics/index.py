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