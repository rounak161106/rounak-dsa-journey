def fibo(i,a,b,n):
    if i==n:
        return
    print(a+b, end=" ")
    fibo(i+1,b,a+b,n)

#classic way nth fibonacci number
def fibon(n):
    if n<=1:
        return n
    return fibon(n-1) + fibon(n-2)

print(0,end=" ")
fibo(1,1,0,10)

print("\n",fibon(9))