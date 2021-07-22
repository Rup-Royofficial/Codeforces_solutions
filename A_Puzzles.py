from numpy import *

n,m = map(int,input().split())
z = []

x = list(map(int,input().split()))
b = min(x)
for i in range(m):
    a = max(x)
    b_1 = min(x)
    c = a-b
    if c == b:
        print(c)
        break
    else:
        x.remove(a)
        x.remove((b_1))
  