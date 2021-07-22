h,w = map(int,input().split())
for i in range(h):
    count = 0
    while count<=h:
        x = str(input())
        if x[0]=="*":
            count+=1
        else:
            pass    

        try:
    
            if  x[1] == "*":
                count+=1
        except :
            pass
                

        try:
            if x[2]=="*":
                count+=1
        except:
            pass

        try:
            if x[3]=="*":
                count+=1
        except :
            pass

        try:
            if x[4]=="*":
                 
        except :
            pass
            


print(count)                   
                    
        