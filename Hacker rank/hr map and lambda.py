cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        listFibo = [0,1]
        for i in range(2,n):
            listFibo.append(listFibo[-1] + listFibo[-2])
        return listFibo
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
