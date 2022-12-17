for x in range(5):
    for y in range(5):
        print("*", end="")
    print()
print("")
for x in range(5):
    for y in range(5-x):
        print("*", end="")
    print()

print("")
for x in range(5):
    for y in range(1 + x):
        print("*", end="")
    print()
for j in range(4):
    for i in range(4-j):
        print("*", end="")
    print()
print()
for x in range(5):
    for y in range(5):
        if y == x or y == 4 - x:
            print('*', end='')
        else:
            print(' ', end='')
    print()