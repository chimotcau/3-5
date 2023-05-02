def f(x,y,h):
    if x+y>=77 and h==3:
        return 1
    if x+y<77 and h==3:
        return 0
    return f(x+1,y,h+1) or f(x*2,y,h+1) or f(x,y+1,h+1) or f(x,y*2,h+1)
for y in range(1,69):
    if f(8,y,1)==1:
        print(y)
        break
        #answer: 18       
