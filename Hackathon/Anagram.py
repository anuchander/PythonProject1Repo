'''
str = 'Listen'
str1 = 'Silent'
Write a function to check whether two given strings are anagram of each other or not.
An anagram of a string is another string that contains the same characters, only the order of
characters can be different. For example, “abcd” and “dabc” are an anagram of each other
'''

def check_anagram(a, b):
    str_l = sorted(a.lower())
    str1_l = sorted(b.lower())

    i=len(a)
    j=len(b)
    if i != j :
        print("The strings", a, "and ", b, "are not anagrams")
        return False
    else:
        print("The strings", a, "and ", b, "are anagrams")
    for x in range(i):
        if str_l[x] != str1_l[x]:
            print("The strings", a, "and ", b, "are not anagrams")
            return False
    print("The strings", a, "and ", b, "are anagrams")
    return True




a="Listen"
b="Silent"
print(a)
print(b)

check_anagram(a, b)

