li = int(input(f"Fale o limite inicial"))
lf = int(input(f"Fale o limite final"))

if li % 3 == 0:
    while li != lf:
        print(li)
        li = li + 3 
elif li % 3 == 1:
    li = li + 2
    while li != lf:
        print(li)
        li = li + 3 
else:
    li = li +1
    while li != lf:
        print(li)
        li = li + 3 
