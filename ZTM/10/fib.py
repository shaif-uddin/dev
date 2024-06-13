def fib(number):
    a=0
    b=1
    result=[]
    for i in range(number):
        result.append(a)
        temp=a
        a=b
        b=temp+b
    return result
# for i in fib(10):
#     print(i)
print(fib(10))