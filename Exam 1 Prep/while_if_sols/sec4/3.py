#Define a function lcm that takes two positive integer parameters m and n,
#and prints the smallest number that is divisible by both m and n.

def lcm(m, n):

    #lcm of two numbers is always greater
    #than or equal to the numbers. So we
    #start with greatest of the two numbers m and n

    if m < n:
        i = n
    else:
        i = m

    while (i%n != 0) or (i%m != 0): #continue as long i is not divisble by either m or n
        i = i + 1

    #The first number that is divisible by
    #both m and n is the lcm
    print(i)

lcm(10, 20)
lcm(3, 7)
lcm(6, 15)