def gcd(a,b):
    if a==0 or b==0:
        return abs(a-b)
    else:
        return gcd(abs(a-b),min(a,b))
    
# improved version of euclidean algorithm
def gcd2(a,b):
    if a==0 or b==0:
        return abs(a-b)
    else:
        return gcd(max(a,b)%min(a,b),min(a,b))
    
print(gcd2(1,1_000_000))