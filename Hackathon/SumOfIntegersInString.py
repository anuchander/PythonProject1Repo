'''
//Two Number in string _ Add those and print their Addition number
'''

def find_sum(s):
 n=len(s)
 sum=0
 for i in range(n):
  if (s[i].isdigit()==True):
   sum+=int(s[i])
 print("the sum of the integers is: ", sum)







s ="He4ll5o5"
find_sum(s)


