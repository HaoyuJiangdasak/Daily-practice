n = int(input("Please enter a number："))
m = int(input("Please enter a number："))
numberlist = []
for i in range(1,n+1):
       numberlist.append(i)
while True:
    if not len(numberlist) == 1:
       num = m%len(numberlist)
       del numberlist[num-1]
    else:
       print(numberlist)
       break



    
        




        


