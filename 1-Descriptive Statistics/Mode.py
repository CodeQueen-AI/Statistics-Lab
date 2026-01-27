def mode(data):
    return max(data, key=data.count)

marks = [80, 50, 45, 91]
print('Mean of Marks is : ' , mode(marks))
