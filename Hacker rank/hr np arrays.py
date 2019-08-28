import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = list(map(float, arr))
    arr = sorted(arr, key=abs, reverse=True)
    a = numpy.array(arr, float)
    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
