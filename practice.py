# a =1
# n = a//2
# for i in range(n+1):
#     print("* "*n)
#     print(" *"*n)

# n=int(input())
# a=n//2
# b=n-n//2
# for i in range(n):
#     print("* "*b)
#     print(" *"*a)



# n=3
# a="* "*n
# map(print,(a[:n],a[1:n+1])*n)

# a,b=map(int,input().split())
# c=list(map(int,input().split()))
# for i in c:
#     print(i-a*b,end=" ")

# n = int(input())
# print(" "*(n-1)+"*")
# if n != 1:
#     for i in range(1,n-1):
#         print(" "*(n-i-1)+"*"+" "*(i*2-1)+"*")
#     print("*"*(n*2-1))




# a,b=map(int,input().split())
# print(abs(a-b))

# a=[]
# for i in range(4):
#     a.append(int(input()))
# b=sum(a)
# print(b//60,b%60)

n=int(input())
print(" "*(n-1)+"*")
if n!=1:
    for i in range(1,n):
        print(" "*(n-i-1)+"*"+" "*(i*2-1)+"*")
n=int(intput())
if n==0:
    print("Yonsei")
else:
    print("Leading the Way to the Future")


for i in range(3):
    a=list(map(int,input().split()))
    if sum(a)==0:
        print("D")
    elif sum(a)==1:
        print("C")
    elif sum(a)==2:
        print("B")
    elif sum(a)==3:
        print("A")
    else:
        print("E")