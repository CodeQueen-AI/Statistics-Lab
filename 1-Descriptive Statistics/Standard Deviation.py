import math

def standard_deviation(data):
    mean = sum(data) / len(data)
    total = 0
    for value in data:
        total += (value - mean) ** 2
    variance = total / len(data)
    return math.sqrt(variance)

marks = [80, 50, 45, 91]
print('Standard Deviation of Marks is : ', standard_deviation(marks))