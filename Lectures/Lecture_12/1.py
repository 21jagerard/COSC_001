def is_increasing(glist):
    for i in range(0, len(glist)-1):
        if glist[i] > glist[i + 1]:
            return False
    return True

def all_increasing(glol):
    for gl in glol:
        print(gl)
        check = is_increasing(gl)
        if check == False:
            return False
    return True 

def atleast_1_increasing(glol):
    for gl in glol:
        check = is_increasing(gl)
        if check:
            return True
    return False

print(all_increasing([[1, 4, 7], [34, 67]]))
