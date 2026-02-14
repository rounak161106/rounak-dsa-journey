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







backtrack_way2(0,10)
