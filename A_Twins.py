n = int(input())
a = map(int,input().split())
a.invert(reverse = True)
d = sum(a)
d = int(d/2)+1
sum_1 = 0
x = 0
for i  in a:
    sum_1 +=i
    i+=1
    if sum_1>=d :
        break

print(i)    