
count = 0
m = -20001
f = open('17.txt')
l = [int(i) for i in f]
for j in range(len(l) - 1):
    if (l[j] % 3 == 0) or (l[j + 1] % 3 == 0):
        count += 1
        m = max(m, l[j]+ l[j + 1])
print(count, m)