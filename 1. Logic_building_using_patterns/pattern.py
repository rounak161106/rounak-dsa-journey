def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()
def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()   
def pattern3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1," ", end="")
        print()   
def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1," ", end="")
        print()   
def pattern5(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("* ", end="")
        print()  
def pattern6(n):
    for i in range(n):
        for j in range(n,i,-1):
            print(n-j+1," ", end="")
        print() 
def pattern7(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print("  ", end="")
        for j in range(1,2*i):
            print("* ", end="")
        print()   
def pattern8(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print("  ", end="")
        for j in range(1,2*n-2*i+2):
            print("* ", end="")
        print()             
def pattern9(n):
    pattern7(n)
    pattern8(n) 
def pattern10(n):
    pattern2(n)
    pattern5(n-1)
def pattern11(n):
    for i in range(1,n+1):
        for j in range(i):
            if(i+j)%2==0:
                print(0, end=" ")
            else:
                print(1,end=" ")
        print()
def pattern12(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1, end="")

        for j in range(2*n-2*i):
            print(" ",end="")
        
        for j in range(i,0,-1):
            print(j,end="")
        
        print()
def pattern13(n):
    ctr=1
    for i in range(n):
        for j in range(i+1):
            print(ctr," ", end="")
            ctr+=1
        print()  
def pattern14(n):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(i+1):
            print(alpha[j], end="")
        print()  
def pattern15(n):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        x=0
        for j in range(n,i,-1):
            print(alpha[x], end="")
            x+=1
        print() 
def pattern16(n):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(i+1):
            print(alpha[i], end="")
        print() 
def pattern17(n):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end="")
        st=2
        for j in range(1,2*i):
            if j<=i:
                print(alpha[j-1], end="")
            else:
                print(alpha[i-st],end="")
                st+=1
        print()
def pattern18(n):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    start=n
    for i in range(1,n+1):
        for j in range(start,n+1):
            print(alpha[j-1],end="")
        start-=1
        print()
def pattern19(n):
    end=n//2
    for i in range(1,n//2+1):
        
        for j in range(end):
            print("*",end="")
        for j in range(0,2*i-2):
            print(" ",end="")
        for j in range(end):
            print("*",end="")
        end-=1
        print()

    end=n-2
    for i in range(1,n//2+1):
        
        for j in range(i):
            print("*",end="")
        for j in range(end):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        end-=2
        print()    
def pattern20(n):
    st=n-1
    for i in range((n+1)//2):
        print("*"*(i+1) + " "*(st) + "*"*(i+1))
        st-=2
    st=n-(n+1)//2
    st2=2
    for i in range((n+1)//2):
        print("*"*(st) + " "*(st2) + "*"*(st))
        st-=1
        st2+=2
def pattern21(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==n-1 or i==n-1 or j==0:
                print("*",end="")
            else:
                print(" ", end="")
        print()
def pattern22(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top=i
            bottom=2*n-2-i
            right=2*n-2-j
            left=j
            point=min([left,right,top,bottom])
            print(n-point,end="")

        print()
pattern17(5)

