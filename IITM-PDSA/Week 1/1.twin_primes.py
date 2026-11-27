# Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
# Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive). The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.
def Twin_Primes(m, n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    res = []
    flag = False
    for i in range(m, n+1):
        if(primes[i]):
            flag = True
            last_prime = i
            break
    if flag:
        for j in range(last_prime, n+1):
            if(primes[j]):
                if(j - last_prime == 2):
                    res.append((last_prime,j))
                last_prime = j
    print(res)
Twin_Primes(1, 100)