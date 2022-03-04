# # print("|\\_/|")
# # print("|q p|   /}")
# # print('( 0 )"""\\')
# # print('|"^"`    |')
# # print("||_/=\\\\__|")

# # a, b, c = input().split()
# # x = int(a)
# # y = int(b)
# # z = int(c)
# # print((x+y)%z)
# # print(((x%z)+(y%z))%z)
# # print((x*y)%z)
# # print(((x%z)*(y%z))%z)

# # a, b = input().split()
# # x = int(a)
# # y = int(b)
# # print(x * y[2])
# # print(x * y[1])
# # print(x * y[0])
# # print(x * y)
# # a = int(input())
# # b = input
# # print(a * int(b[2]))
# # print(a * int(b[1]))
# # print(a * int(b[0]))
# # print(a)

# # a, b = input().split()
# # x = int(a)
# # y = int(b)
# # if x > y:
# #     print(">")
# # elif x < y:
# #     print("<")
# # elif x == y:
# #     print("==")

# # a = int(input())

# # if 90 <= a <= 100:
# #     print("A")
# # elif 80 <= a < 90:
# #     print("B")
# # elif 70 <= a < 80:
# #     print("C")
# # elif 60 <= a < 70:
# #     print("D")
# # else:
# #     print("F")

# # a = int(input())
# # if a % 4 == 0 and a % 100 != 0:
# #     print("1")
# # elif a % 400 == 0:
# #     print("1")
# # else:
# #     print("0")

# # x = int(input())
# # y = int(input())
# # if x > 0 and y > 0:
# #     print("1")
# # elif x < 0 and y > 0:
# #     print("2")
# # elif x < 0 and y < 0:
# #     print("3")
# # else:
# #     print("4")


# # a, b = input().split()
# # x = int(a)
# # y = int(b)
# # if y >= 45:
# #     print(x, y - 45)
# # elif y < 45 and x != 0:
# #     print(x - 1, y + 15)
# # elif y < 45 and x == 0:
# #     print(23, y + 15)

# # a = int(input())

# # for i in range(1, 10):
# #     print(a, "*", i, "=", a*i)

# # t = int(input())

# # for i in range(t):
# #     a, b = map(int, input().split())
# #     print(a + b)

# # n = int(input())

# # sum = 0
# # for i in range(1, n + 1):
# #     sum += i
# # print(sum) 

# # import sys

# # t = int(sys.stdin.readline())

# # for i in range(t):
# #     a,b = map(int, sys.stdin.readline().split())
# #     print(a + b)

# # n = int(input())

# # for i in range(n, 0, -1):
# #     print(i)

# # t = int(input())

# # for i in range(1, t + 1):
# #     a, b = map(int, input().split())
# #     print("Case #{}:".format(i), a + b)

# # t = int(input())
# # for i in range(1, t + 1):
# #     star = "*"* i
# #     print(star.rjust(n))

# # n, x = map(int, input().split())
# # A = list(map(int, input().split()))
# # for i in range(n):
# #     if A[i] < x:
# #         print(A[i], end = " ")

# # while True:
# #     a, b = map(int, input().split())
# #     if a == 0 and b == 0:
# #         break
# #     else:
# #         print(a + b)

# # while True:
# #     try:
# #         a, b = map(int, input().split())
# #         print(a+b)
# #     except:
# #         break

# # input_num = int(input())
# # num = input_num
# # cnt = 0
# # while True:
# #     sum_num = (num // 10) + (num % 10)
# #     new_num = ((num % 10)*10) + (sum_num % 10)
# #     cnt += 1
# #     if new_num == input_num:
# #         break
# #     num = new_num
# # print(cnt)  
# # b = int(input())
# # A = list(map(int, input().split()))
# # print(min(A), max(A))

# # list = []
# # for i in range(9):
# #     list.append(int(input()))
# # print(max(list))
# # print(list.index(max(list))+ 1)

# # a = int(input())
# # b = int(input())
# # c = int(input())
# # result = list(str(a * b * c))

# # for i in range(10):
# #     print(result.count(str(i)))

# # list = []
# # for i in range(10):
# #     list.append(int(input()) % 42)
# # list = set(list)
# # print(len(list))

# # n = int(input())
# # list = []
# # for i in range(n + 1):
# #     list.append(int(input()))
# # M = max(list)
# # print(sum(list) * M / 100 / n)

# # n = int(input())
# # score = list(map(int, input().split()))
# # M = max(score)
# # print(sum(score)*100/M/n)

# # n = int(input())
# # for i in range(n):
# #     list_1 = list(input())
# #     score = 0
# #     sum = 0
# #     for j in list_1:
# #         if j == 'O':
# #             score += 1
# #             sum += score
# #         else:
# #             score = 0
# #     print(sum)

# # for i in range(0):
# #     list_1 = list["OOOOOOXXXX"]
# #     score = 0
# #     sum = 0
# #     for j in list_1:
# #         if j == 'O':
# #             score += 1
# #             sum += score
# #         else:
# #             score = 0
# #      print(sum)

# # for i in range(int(input())):
# #     list_1 = list(map(int, input().split()))
# #     avg = sum(list_1[1:])/list_1[0]
# #     student = 0
# #     for score in list_1[1:]:
# #         if score > avg:
# #             student += 1
# #     rate = student/list_1[0] * 100
# #     print(f'{rate:.3f}%')

# #백준15596 정수 N개의 합
# # def total():
# #     return sum()

# #백준4673 셀프넘버
# # numbers = list(range(1, 10001))
# # remove_list = []
# # for num in numbers:
# #     for n in str(num):
# #         num += int(n)
# #     if num <= 10000:
# #         remove_list.append(num)
# # for remove_num in set(remove_list):
# #     numbers.remove(remove_num)
# # for self_num in numbers:
# #     print(self_num)

# #백준1065 한수
# # def hansu(n):
# #     hansu_cnt = 0
# #     for i in range(1, n+1):
# #         num_list =list(map(int, str(i)))
# #         if i < 100:
# #             hansu_cnt += 1
# #         elif num_list[0]-num_list[1] == num_list[1] - num_list[2]:
# #             hansu_cnt += 1
# #     return hansu_cnt

# # n = int(input())
# # print(hansu(n))

# # a,b,c = map(int, input().split())

# #백준11720 숫자의 합
# # if b >= c:
# #     print(-1)
# # else:
# #     print(a//(c-b)+1)
# # n = int(input())
# # nums = input()
# # total = 0
# # for i in range(n):
# #    total += int(nums[i])
# # print(total)

# #백준10809 알파벳찾기  
# # a = input()
# # abc ='abcdefghijklmnopqrstuvwxyz'

# # for i in abc:
# #     if i in a:
# #         print(a.index(i), end=' ')
# #     else:
# #         print(-1, end='')

# #백준2675 문자열반복
# # for i in range(int(input())):
# #     cnt, word = input().split()
# #     for j in word:
# #         print(j*int(cnt), end="")
# #     print()

# #백준1157 단어공부
# # words = input().upper()
# # unique_words = list(set(words))
# # cnt_list = []
# # for i in unique_words:
# #     cnt = words.count(i)
# #     cnt_list.append(cnt)
# # if cnt_list.count(max(cnt_list)) > 1 :
# #     print("?")
# # else:
# #     max_index = cnt_list.index(max(cnt_list))
# #     print(unique_words[max_index])

# #백준1152 단어의 개수
# # words = list(input().strip())
# # print(len(words))


# #백준2798 블랙잭
# # N, M = map(int, input().split())
# # nums = list(map(int, input().split()))

# # result = 0
# # Max = 0

# # for i in range(N-2):
# #     for j in range(i+1,N-1):
# #         for k in range(j+1, N):
# #             if nums[i]+nums[j]+nums[k] > M:
# #                 continue
# #             else:
# #                 result = nums[i]+nums[j]+nums[k]
# #                 if Max <= result:
# #                     Max = result
# # print(Max)

# #백준2908 상수
# # a, b = map(int, input().split())

# # c = (a // 100) + ((a // 10) % 10)*10 + (a % 10)*100
# # d = (b // 100) + ((b // 10) % 10)*10 + (b % 10)*100

# # if d > c:
# #     print(d)
# # else:
# #     print(C)

# #백준5622 다이얼
# # alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# # words = input())
# # time = 0
# # for i in alpabet_list:
# #     for j in i:
# #         for h in words:
# #             if h == j:
# #                 time += alpabet_list.index(i) + 3

# # print(time)

# #백준2941 크로아티아 알파벳
# # word = "ljes=njak"
# # croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# # for i in croatia:
# #     word = word.replace(i,"*")
# # print(len(word))

# #백준1316 그룹단어
# # N = int(input())
# # result = N
# # for i in range(N):
# #     word = input()
# #     for j in range(len(word)-1):
# #         if word[j] == word[j+1]:
# #             pass
# #         elif word[j] in word[j+1:]:
# #             result -= 1
# #             break
# # print(result)

# #백준2292 벌집
# # n = int(input())
# # comb = 1
# # cnt = 1
# # while n > comb:
# #     comb += 6*cnt
# #     cnt +=1
# # print(cnt)

# #백준1193 분수찾기
# # n = int(input)
# # line = 0
# # max_num = 0
# # while n > max_num:
# #     line += 1
# #     max_num += line

# # gap = max_num - n
# # if line % 2 ==0:
# #     top = line - gap
# #     under = gap + 1
# # else:
# #     top = gap + 1
# #     under = line - gap
# # print(f'{top}/{under}')

# #백준2869 달팽이는 올라가고싶다
# # A,B,V = map(int, input().split())
# # d = (v-b)/(a-b)
# # print(int(d) if d == int(d) else int(d) +1)

# #백준10250 ACM호텔
# # for i in range(int(input())):
# #     H,M,N = map(int, input().split())
# #     num = n//h + 1
# #     floor = n % h
# #     if n % h == 0:
# #         num = n//h
# #         floor = h
# #     print(f'{floor*100+num}')

# #백준2775 부녀회장이 될테야
# # for i in range(int(input())):

# #백준2839 설탕배달
# # n = int(input())
# # bag = 0
# # while n>=0:
# #     if n % 5 ==0:
# #         bag += (n//5)
# #         print(bag)
# #         break
# #     n -=3
# #     bag +=1
# # else:
# #     print(-1)    

# #백준1011 Fly me to the Alpha Centauri
# # for i in range(int(input())):
# #     x, y = map(int, input().split())
# #     y - x

# #백준10817 세수
# # list_1 = list(map(int, input().split()))
# # list_1.remove(max(list_1))
# # print(max(list_1))

# #백준2750 수 정렬하기

# # n = int(input())
# # list_1 = []
# # for i in range(n):
# #     list_1.append(int(input()))

# # list_1.sort()
# # for i in range(n):
# #     print(list_1[i])

# #백준2558 A+B-2
# # a = int(input())
# # b = int(input())
# # print(a+b)

# #백준 10872 팩토리얼

# # t = int(input)
# # def factorial_1(n):
# #     변수 = 1 
# #     for i in range(1, n + 1):
# #         변수 *= i
# #     return 변수

# # print(factorial_1(t))

# #백준2440 별찍기 -3
# # n = int(input())
# # for i in range(n,0,-1):
# #     print('*'*i) 

# #백준2441 별찍기 -4
# # n = int(input())
# # for i in range(n,0,-1):
# #     print(' '*(n-i)+'*'*i) 

# #백준10870 피보나치 수
# # n = int(input())
# # 메모 = {0: 0, 1: 1, 2: 1}
# # def f(n):
# #     if n in 메모:
# #         return 메모[n]
# #     else:
# #         output = f(n-1) + f(n-2)
# #         메모[n] = output
# #         return output
# # print(f(n))

# 백준11721 10개씩 끊어 출력하기
# a = input()
# for i in range(0,len(a),10):
#     print(a[i:i+10])

# 백준2920 음계
# a = list(map(int, input().split()))
# if a == sorted(a):
#     print("ascending")
# elif a == sorted(scale, reverse = True):
#     print("descending")
# else:
#     print("mixed")

# # #백준10797 10부제
# # n = int(input())
# # a = list(map(int, input().split()))
# # print(a.count(n))

# 백준10773 제로
# a =[]
# for i in range(int(input())):
#     n = int(input())
#     if n != 0:
#         a.append(n)
#     else:
#         a.pop()

# # print(sum(a))

# #백준1475 방 번호
# # a = {}
# # b = input()
# # for i in b:
# #     try:
# #         a[i] +=1
# #     except:
# #         a[i] = 1


#백준2442 별 찍기 5
# for i in range(1,6):
#     b =" "*(5-i)+"*"*(2*i-1)
#     print(b)

# n = int(input())
# for i in (n, 1):
#     b =" "*(5-i)+"*"*(2*i-1)
#     print(b)

# a = list(map(int, input().split()))
# print(max(a),min(a))

# a=int(input())
# b=0
# for i in range(9):
#     c=int(input())
#     b+=c
# print(a-b)

# a,b,c= map(int,input().split(":"))
# d,e,f= map(int,input().split(":"))
# now = a*3600+b*60+c
# start = d*3600+e*60+f
# g= 0
# if now > start:
#     g = 24 * 60 * 60 - (now - start)
# else:
#     g = start - now
# h=g//3600
# m=g//60%60
# s=g%60
# print(f'{h:02d}:{m:02d}:{s:02d}')

# a=int(input())
# for i in range(a):
#     b= int(input())
#     f = 0
#     for j in range(int(input())):
#         c,d=map(int,input().split)
#         g=c*d
#         f+=g
#     print(b+f)

# for i in range(int(input())):
#     b=int(input())
#     a=sum(list(map(int,input().split())))
#     print(a)

# a= str(input())
# b= a.split()
# print(b)

# for i in range(int(input())):
#     a,b=map(int,input().split())
#     c=a//b
#     d=a%b
#     print("You get {} piece(s) and your dad gets {} piece(s).".format(c,d))

# a=[]
# for i in range(7):
#     b=int(input())
#     if b%2!=0:
#         a.append(b)
# if sum(a)!=0:        
#     print(sum(a))
#     print(min(a))
# else:
#     print("-1")

# for i in range(int(input())):
#     a,b=map(int,input().split())
#     print(2+b-a)
n=int(input())
for i in range(n):
    if i%2==0:
        for j in range(n*2):
            if j%2==0:
                print('*',end='')
            else:
                print(' ',end='')
    else:
        for j in range(n*2):
            if j%2==0:
                print(' ',end='')
            else:
                print('*',end='')