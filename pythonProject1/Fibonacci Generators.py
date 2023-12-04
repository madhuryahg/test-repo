def fibonacci(num):
    a = 0
    b = 1
    for item in range(num):
        yield a
        # temp = a
        # a = b
        # b = temp + b
        a,b = b,a+b
        
for i in fibonacci(10):
    print(i)
