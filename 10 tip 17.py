f = open('17.txt')
count= ms = 0
a=[int(i) for i in f]
for j in range(len(a)-1) :
    for k in range(j+1,len(a)):
        if (a[j]*a[k]%3==0) and (( a[j]+a[k]) %2!=0):
            count +=1
            ms = max(ms,a[j]+a[k])
print(count,ms)
#answer: 13931722 19993                                                                                                                                        