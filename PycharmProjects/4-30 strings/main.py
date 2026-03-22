def is_palindrome (s):
    # remove blanks, set them to all l/c, etc
   return s == s[s:: -1]
s = "abcdedcba"
print (is_palindrome(s))










'''
s = "abcde"
ss = s[2:3]
print (ss)
print (s)
print (s[0:6])
print (s[0:6:1])
print (s[0:6:2])
print (s[-1:-1])
'''