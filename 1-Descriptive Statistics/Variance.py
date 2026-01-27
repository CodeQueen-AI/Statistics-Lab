def variance(data):
    mean = sum(data) / len(data)
    total = 0
    for value in data:
        total += (value - mean) ** 2
    return total / len(data)

