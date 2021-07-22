x = input()
count =0
for i in range(len(x)-1):
    if x[i]==x[i+1]: #Either use x[i-1] or x[i+1]
        count+=1
    if x[i]!=x[i+1] and count<7:  #Either use x[i-1] or x[i+1]
        count = 1  

if count>=6:
    print("YES")
    
else:
    print("NO")       