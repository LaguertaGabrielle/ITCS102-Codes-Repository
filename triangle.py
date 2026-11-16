s = 7
l = 13

for x in range(s):
    for y in range(13):
        print("", end=" ")
        if x + y == s - 1 or x == y:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()            

for x in range(l):
    for y in range(l):
        print('', end=" ")
        if x == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()                