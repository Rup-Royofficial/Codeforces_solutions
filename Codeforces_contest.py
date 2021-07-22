n = int(input())
for i in range(n):
    r,b,d = map(int,input().split())
    if (r-b) <= d and r>=1 and b>=1:
        print("YES")
    else:
        print("NO")