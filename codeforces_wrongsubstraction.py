a,b = input().split()
count = 0
a = int(a)
b = int(b)

while count!=b:
    if a[-1] != 0:
        a-=1
        count+=1
    if a[-1] == 0:
        a = a/10
        count+=1



print(a)            