# Purpose: demo building a dictionary

# Purpose: print for each character how many times it appears in s
def func(s):  # O(n), n is length of s
    d_count = {}  # O(1)

    for ch in s:  # O(n)
        if ch in d_count:
            d_count[ch] += 1
        else:
            d_count[ch] = 1

    for k in d_count:  # O(n)
        print(k, d_count[k])

func("chocolate")