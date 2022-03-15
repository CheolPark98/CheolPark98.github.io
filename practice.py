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


# a,b=map(int,input().split())
# c=0
# d=[]
# while True:
#     c



# print("c","a","k","e",sep="*")
# print("cake",sep="a")

<<<<<<< HEAD
# n = 10
# print("%f" % n)

# n = int(input())
# 메모 = {0: 0, 1: 1, 2: 1}
# def f(n):
#     if n in 메모:
#         return 메모[n-1]
=======
# a=[]
# for i in range(5):
#     a.append(int(input()))
# print(sum(a))

# for i in range(int(input())):
#     c=[]
#     d=[]
#     n=int(input())
#     for j in range(n):
#         a,b=map(float,input().split())
#         c.append(int(a))
#         d.append(b*a)
#     e=sum(c)
#     f=sum(d)/e
#     print("{} {:.1f}".format(e,f))
# c=[]
# for i in range(int(input())):
#     a,b=map(int,input().split())
#     d=b%a
#     c.append(d)
# print(sum(c))

# a=[]
# for i in range(1,101):
#     a.append(i*i)
# b=int(input())
# c=int(input())
# d=[]
# for j in range(b,c+1):
#     if j in a:
#         d.append(j)
# if d == []:
#     print("-1")
# else:
#     print(sum(d))
#     print(min(d))

# for i in range(int(input())):
#     a={}
#     for j in range(int(input())):
#         b,c=map(str,input().split())
#         a[c]=int(b)
#     print(max(a, key=a.get))

# e={}
# for i in range(int(input())):
#     a,b,c,d=map(str,input().split())
#     e[a]=('%04d%02d%02d'%(int(d),int(c),int(b)))
# print(max(e, key=e.get)) 
# print(min(e, key=e.get)) 

# a={1:1,2:1}
# def f(n):
#     if n in a:
#         return a[n]
#     else:
#         c= f(n-1) + f(n-2)
#         a[n] = c
#         return c
# print(f(int(input())))
# 메모 = { 1: 1, 2: 1}
# def f(n):
#     if n in 메모:
#         return 메모[n]
>>>>>>> cb848e70739674e4ffcd9966027785fb3f6d86ad
#     else:
#         output = f(n-1) + f(n-2)
#         메모[n] = output
#         return output
<<<<<<< HEAD
# print(f(

# a=[]
# b,c=map(int,input().split())
# for i in range(1,b+1):
#     if b%i==0:
#         a.append(i)
# if c>len(a):
#     print(0)
# else:
#     print(a[c-1])

# n=int(input())
# a=[]
# for i in range(n):
#     a.append(str(input()))
a=list(input())
print(a)
=======
# print(f(3))

# sum=0
# result=0
# n=int(input())
# a=list(map(int,input().split()))
# for i in range(n):
#     if a[i]==1:
#         sum+=1
#         result+=sum
#     else:
#         sum=0
# print(result)
# m,n=map(int(input()))
# a=[]
# for i in range(m,n+1):
#     for j in range(2,i+1):
#         if i%jc

# a=2
# b=3
# c=1

# d=a
# a=b
# b=c
# c=d

# print(a)
# print(b)
# print(c)
# print(d)


# result=0
# result+=1
# result+=2
# result+=3
# result+=4
# result+=5
# print("result = {}".format(result))

# n1 = int(input())
# n2 = int(input())
# n3 = n1
# n1 = n2
# n2 = n3
# print("n1 = {}".format(n1))
# print("n2 = {}".format(n2))

# n = int(input())
# print("before = {}".format(n))
# print("after = {}".format(int(n/10*9)))

# a=str(input())
# b=int(input())
# print(a*b)

# a=int(input())
# print("x {}".format(a))
# for i in range(1,10):
#     print("{} x {} = {}".format(a,i,a*i))
n= int(input())
a= n//86400
b= (n%86400)//3600
c= ((n%86400)%3600)//60
d= ((n%86400)%3600)%60

print('%d days %02d:%02d:%02d'%(a,b,c,d))
>>>>>>> cb848e70739674e4ffcd9966027785fb3f6d86ad
