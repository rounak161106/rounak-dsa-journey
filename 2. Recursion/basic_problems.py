ctr = 0
def print_name(n): 
    global ctr
    if ctr == n:
        return
    print("Rounak Prasad")
    ctr+=1
    return print_name(n)
def print1_to_n(n):
    global ctr
    if ctr==n:
        return
    print(ctr+1)
    ctr+=1
    return print1_to_n(n)
def printn_to_1(n):
    if n==0:
        return
    print(n)
    return printn_to_1(n-1)
def backtrack_way(n):
    if n==0:
        return
    backtrack_way(n-1)
    print(n)
def backtrack_way2(i,n):
    if i==n:
        return
    i+=1
    backtrack_way2(i,n)
    print(i)




def print_n_to_1(n):
    if(n==0):
        return
    print(n)
    print_n_to_1(n-1)

def way2(i):
    if(i==0):
        return
    way2(i-1)
    print(i)

def parameterized_sum(i,sum):
    if(i<1):
        print(sum)
        return
    parameterized_sum(i-1,sum+i)

parameterized_sum(10,0)
