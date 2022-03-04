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

# from re import M


# h,m,s=map(int,input().split())
# t=int(input())

# h+=t//3600
# m+=(t%3600)//60
# s+=(t%3600)%60


# if s>=60:
#     m+=1
#     s-=60
# if m>=60:
#     h+=1
#     m-=60
# if h>=24:
#     h-=24
# print(h,m,s)

# A, B, C = map(int, input().split())
# D = int(input())
# t = A*60*60 + B*60 + C + D
# h = t//60//60 % 24
# m = t//60 % 60
# # s = t%60
# print(h, m, s)

# import datetime

# print(str(datetime.datetime.now())[:10])

# for i in range(int(input())):

# s=3.1444444

# print("%.4f입니다" % s)



# for i in range(int(input())):
#     b = list(map(str, input().split()))
#     a=0
#     for j in range(len(b)):
#         if j==0:
#             a+=float(b[j])
#         else:
#             if b[j]=="@":
#                 a*=3
#             elif b[j]=="%":
#                 a+=5
#             elif b[j]=="#":
#                 a-=7
#     print("%0.2f" %a)

# a=int(input())
# b=input()
# c=int(input()) 


# if b=="+":
#     print(a+c)
# else:
#     print(a*c)


# a=list(map(int,input().split()))
# a = []
# for i in range(int(input())):
#     a.append(int(input()))
# if a.count(0) > a.count(1):
#     print("Junhee is not cute!")
# else:
#     print("Junhee is cute!")
# c = 100
# d = 100
# for i in range(int(input())):
#     a,b = map(int, input().split())
#     if a > b:
#         d -= a
#     elif a < b:
#         c -= b
#     else:
#         pass
# print(c)
# print(d)
# b = []
# for i in range(5):
#     a = int(input())
#     if a >= 40:
#         b.append(a)
#     elif a < 40:
#         b.append(40)
# print(sum(b)/5)
# a=str(input())
# b = 0
# for i in range(len(a)):
#     if i ==0:
#         b+=10
#     elif a[i] == a[i-1]:
#         b+=5
#     else:
#         b+=10
# print(b)

# a= int(input())
# A=0
# B=0
# C=0
# while True:
#     if  a==0:
#         print(A,B,C)
#         break
#     if a<0:
#         print("-1")
#         break
#     if a>=300:
#         a-=300
#         A+=1
#     elif 300>a>=60:
#         a-=60
#         B+=1
#     elif 60>a>=10:
#         a-=10
#         C+=1


a,b=map(int,input().split())
c=0
d=[]
while True:
    c
