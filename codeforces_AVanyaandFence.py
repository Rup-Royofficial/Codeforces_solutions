a,b = map(int,input().split())
c = input().split()
count = 0
b = str(b)

for i in range(a):
    if c(i)<=b:
        count+=1
    if c(i)>b:
        count+=2

    print(count)            