print("x y z w")
k = 0,1
for x in k:
    for  y in k:
        for z in k:
            for w in k:
                if not (((x and y) <= (not(z) or w))and ((not(w)<=x) or (not(y)))):
                    print (x,y,z,w)
                    #answer: