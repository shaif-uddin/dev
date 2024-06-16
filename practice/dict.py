n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)

# Using dictionary comprehension

n=int(input())
ans={i: i*i in range(1,n+1)}