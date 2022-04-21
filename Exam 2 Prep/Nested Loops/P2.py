# Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set
# of characters that occur with the same frequency (you are checking if s1 and s2 are anagrams). For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return False

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i not in s2:
            return False
    return True

print(is_anagram("dirtymore", "dormitory"))
