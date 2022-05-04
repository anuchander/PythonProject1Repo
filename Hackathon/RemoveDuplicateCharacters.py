'''
//remove duplicate characters from string abcabcabc as abc
'''

def remove_duplicates(str):
    n=len(str)
    ns=""
    for a in str:
        if (a in ns):
            pass
        else:
            ns=ns+a

    print("The non duplicate characters are: ", ns)

def remove_duplicates_set(str):
    s=set(str)
    s="".join(s)
    print("The non dupliacte characters are: ", s)

str="abcabcabc"
print("The given string is: ", str)
remove_duplicates(str)
remove_duplicates_set(str)
