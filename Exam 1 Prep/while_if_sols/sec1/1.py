def check_triangle(a1, a2, a3):

    if (a1 == a2) and (a2 == a3):
        print("Equilateral")
    elif (a1 == a2) or (a2 == a3) or (a3 == a1):
        print("Isosceles")
    else:
        print("Scalene")


check_triangle(70, 40, 70)