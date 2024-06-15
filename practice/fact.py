# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x* fact(x-1)
# print(fact(8))

# Using While Loop

n=int(input())
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1

print(fact)