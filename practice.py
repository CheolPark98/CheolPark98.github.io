a = {0: 0, 1: 1, 2: 1}
def f(n):
     if n in a:
         return a[n]
     else:
         output = f(n-1) + f(n-2)
         a[n] = output
         return output

print(f(4))