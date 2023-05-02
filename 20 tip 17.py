f = open('17.txt')
ms = count =0
a= [int(i) for i in f]
for j in range(len(a)-1):
    for k in range(j+1,len(a)):
        if ((a[j]+a[k])%60==0) and ((a[j]%40==0) or (a[k]%40==0)):
            count+=1
            ms= max(ms,a[j]+a[k])
print(count,ms)
#answer: 29278 19860           
