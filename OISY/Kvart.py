# https://en.wikipedia.org/wiki/Quadrant_(plane_geometry) 
if x > 0 and y > 0:
    K = "kvadrantti = I"
    print(round(x, 2),round(y, 2), sep = ",", end = " ")
    print(K)
if x < 0 and y < 0:
    K = "kvadrantti = III"
    print(round(x, 2),round(y, 2), sep = ",", end = " ")
    print(K)
if x > 0 and y < 0:
    K = "kvadrantti = IV"
    print(round(x, 2),round(y, 2), sep = ",", end = " ")
    print(K)
if y > 0 and x < 0:
    K = "kvadrantti = II"
    print(round(x, 2),round(y, 2), sep = ",", end = " ")
    print(K)
