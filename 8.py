import re
def find(s):
     charRe  = '^[a-z]+_[a-z]+$'
     if not re.search(charRe, s):
         return "found a match"
     else :
         return "not matched"    


s= input()
print (find(s) )