x = int(input())
y = 0
total = 0
a = {1,2,3,4,5}

for i in range(5) :
    if x <= 5:
        y+=1

    if y == 1:    
        print(y)


if x > 5:
    while True:
        res_1 = random.sample(a,3)
        total = sum(res_1)
        if total == x:
            print(total)

