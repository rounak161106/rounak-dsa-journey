"""
Goldbach's conjecture is one of the oldest and best-known unsolved problems in number
theory. It states that every even number greater than 2 is the sum of two prime numbers.

For Example:
12 = 5 + 7
26 = 3 + 23 or 7 + 19 or 13 + 13

Write a function Goldbach(n) where n is a positive even number (n > 2) that returns a list of
tuples. In each tuple (a, b) where a <= b, a and b should be prime numbers and the sum of
a and b should be equal to n.

Sample Input 1:
12

Output:
[(5, 7)]

Sample Input 2:
26

Output:
[(3, 23), (7, 19), (13, 13)]
"""

def Goldbach(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    res = []
    for i in range(2,n//2+1):
        if(primes[i] and primes[n-i]):
            res.append((i, n-i))
    return res

print(Goldbach(10))