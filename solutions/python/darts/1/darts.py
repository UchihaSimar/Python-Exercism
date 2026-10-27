from math import sqrt

def score(x, y):
    distance_from_center = sqrt(x**2 + y**2)

    if distance_from_center <=1:
        return 10

    if distance_from_center <=5:
        return 5

    if distance_from_center <=10:
        return 1

    return 0
    
