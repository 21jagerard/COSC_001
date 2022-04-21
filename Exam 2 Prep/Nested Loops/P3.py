#  Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set
#  of characters but possibly with a different frequency. For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return True

def is_dirty_anagram(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

print(is_dirty_anagram("tooooo ", "too"))