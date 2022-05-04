'''
str=malayalam
'''

def check_palindrome(a):
 n = len(a)
 n1=n
 print("the length of the string malayalam is:", n1)
 for i in range(int(n/2)):
     if a[i]!=a[n1-1]:
         print("The given string", a ,"is not a palindrome!")
         return False
     else:
         n1-=1
 print("the given string is a palindrome!")

a="python"
b=a.lower()
check_palindrome(b)
