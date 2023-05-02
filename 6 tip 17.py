f= open ('17.txt')
ms = count = 0
a=[int(i) for i in f]
for j in range(len(a)-1):
    for k in range (j+1,len(a)):
        if a[j]*a[k]%62==0:
            count += 1
            ms=max(a[j]+ a[k],ms)
print(count,ms) 
#answer: 2284645 19920          
