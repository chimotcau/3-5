print("x y z w")
k = 0,1
for x in k:
    for  y in k:
        for z in k:
            for w in k:
                if ((z <= w) or (y == w))and((x or z) == y):
                    print (x,y,z,w)
                    #answer: