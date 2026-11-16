s = 5
h = 1

for x in range(s):
    for y in range(s):
        print("", end=" ")
        if x == 0 or x == s - 1 or x + y == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()            

