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

# n=int(input())
# print(" "*(n-1)+"*")
# if n!=1:
#     for i in range(1,n):
#         print(" "*(n-i-1)+"*"+" "*(i*2-1)+"*")
# n=int(intput())
# if n==0:
#     print("Yonsei")
# else:
#     print("Leading the Way to the Future")


# for i in range(3):
#     a=list(map(int,input().split()))
#     if sum(a)==0:
#         print("D")
#     elif sum(a)==1:
#         print("C")
#     elif sum(a)==2:
#         print("B")
#     elif sum(a)==3:
#         print("A")
#     else:
#         print("E")
# b=0
# for i in range(8):
#     a=str(input())
#     if i%2==0:
#         for i in range(4):
#             if a[i*2]=="F":
#                 b+=1
#     else:
#         for i in range(4):
#             if a[i*2+1]=="F":
#                 b+=1
# print(b)




# a="FFFFFFFF"
# b=0
# for i in range(4):
#     if a[i*2]=="F":
#         b+=1
# print(b)

# print(sum([n**2 for n in map(int,input().split())])%10)

# arr=input() 
# cnt=[0]*26 
# for i in arr:
#     cnt[ord(i)-97]+=1 
# print(*cnt)

# for i in range(int(input())):
#     a,b=map(int,input().split())
#     print(str(a**b)[-1])\

# while True:
#     a,b=map(int,input().split())
#     if a==0 and b==0:
#         break
#     if a/b == int(a/b):
#         print("multiple")
#     elif b/a == int(b/a):
#         print("factor")
#     else:
#         print("neither")
# a=[]
# b=[]
# for i in range(3):
#     c,d=map(int,input().split())
#     a.append(c)
#     b.append(d)
# for i in range(3):
#     if a.count(a[i])==1:
#         e=a[i]
#     if b.count(b[i])==1:
#         f=b[i]
# print(e,f)
# c=0
# d=[]
# for i in range(4):
#     a,b=map(int,input().split())
#     c-=a
#     d.append(c)
#     c+=b
#     d.append(c)
# print(max(d))

# while True:
#     a=int(input())
#     if a==0:
#         break
#     if ''.join(reversed(str(a)))== str(a):
#         print("yes")
#     else:
#         print("no")

# import sys

# S=[]
# M=int(input())
# def f(c,x):
#     global S
#     if c=="add":
#         if x not in S:
#             S.append(x)
#     elif c=="remove":
#         if x in S:
#             S.remove(x)
#     elif c=="check":
#         if x in S:
#             print("1")
#         else:
#             print("0")
#     elif c=="togle":
#         if  x in S:
#             S.remove(x)
#         else:
#             S.append(x)
#     elif c=="all":
#         S=[i for i in range(1,21)]
#     else:
#         S=[]

# for i in range(M):
#     c=sys.stdin.readline().strip()
#     if c=="all" or c=="empty":
#         f(c,0)
#     else:
#         c,x=c.split()
#         f(str(c),int(x))

a,b=map(int,input().split())
c=int(input())
if b+c>=60:
    print((a+(b+c)//2),(b+c)%60)
else:
    print(a,b+c)