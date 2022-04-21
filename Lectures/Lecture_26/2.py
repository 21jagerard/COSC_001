#
# def count_freq(gstr, c):
#     count = 0
#     for x in gstr:
#         if c == x:
#             count += 1
#
#     return count
#
# def check_strings(str1, str2):
#     if len(str1) != len(str2):
#         return False
#
#     for x in str1:
#         c1 = count_freq(str1, x)
#         c2 = count_freq(str2, x)
#
#         if c1 != c2:
#             return False
#
#     return True


# Purpose: demo building a dictionary

# Purpose: print for each character how many times it appears in s
def char_count(s):  # O(n), n is length of s
    d_count = {}  # O(1)

    for ch in s:  # O(n)
        if ch in d_count:
            d_count[ch] += 1
        else:
            d_count[ch] = 1

    return d_count

def compare_strings(s1, s2):  # O(n)
    d1 = char_count(s1)
    d2 = char_count(s2)

    # if d1 == d2:
    #     return True
    #
    # return False

    if len(d1) != len(d2):
        return False

    for k in d1:  # O(n), n is the length of the string
        if k in d2:
            if d1[k] != s2[k]:
                return False
        else:
            return False
    return True
