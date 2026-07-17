## to find the pairs of prime numbers which adds to an even number greater than 2.
def isPrime(n):
    if n<0:
        return False
    
    for i in range(2,int(n**0.5 + 1)):
        if(n % i == 0):
            return False
    return True

def goldbach(n):
    l = []
    for i in range(2, n//2 + 1):
        if isPrime(i) and isPrime(n-i):
            l.append((i,n-i))
    print(l)

goldbach(26)

## for larger inputs this logic will not work, therefore we need a more efficient algo. 
## the idea is simple. we first find all the primes from 0 to n in a list marking the primes in the list as true and non primes as false and after maintaining the list, we check if they adds up to the given no.

# def findPrimePairs(n):
#     primes = [True] * (n+1)
#     primes[0] = primes[1] = False
#     for i in range(2, n+1):
#         if primes[i]:
#             for j in range(i*2, n+1, i):
#                 primes[j] = False
    
#     result = []
#     for i in range(2, n//2 + 1):
#         if primes[i] and primes[n-i]:
#             result.append([i,n-i])  
#     print(result)
    
# findPrimePairs(52345146)

