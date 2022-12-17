import random

kortit = ["ässä", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jätkä", "kuningatar", "kuningas"]

for x in range(20):
    A = random.choice(kortit)
    B = random.choice(kortit)

    while A == 'ässä' and B == 'ässä':
        B = random.choice(kortit)

    print('Kortit: A-', A, ' B-', B, sep='')

    kortti = ["jätkä", "kuningatar", "kunigas"]

    D = B
    E = A

    if D == 'ässä' or D == 'jätkä' or D == 'kuningatar' or D == "kuningas":
        if D == "ässä":
            D = 11
        else:
            D = 10

    if E == "ässä" or E == "jätkä" or E == "kuningatar" or E == "kuningas":
        if E == "ässä":
            E = 11
        else:
            E = 10

    C = D + int(E)

    print(E, "+", D, "=", + C)

    if C == 21:
        print("BLACKJACK")
    elif C < 17:
        print("nosto kannattaa")
    else:
        print("kannattaa pysyä")


    if A and B != [2,3,4,5,6,7,8,9,10]:
        if A == B:
            print("käden voi jakaa!")