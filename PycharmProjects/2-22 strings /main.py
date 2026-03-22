s = "abcdefghij"
print(len(s))
ss= s[5]
print(ss)
sss = ("k" + ss)
print(sss)
ssss= s[2:5]
print(ssss)
#function types
for i in range (0,10):
    print(s[i])
for i in range(0, len(s)):
    print(s[i])
#for i in range(0, len(s)-4):
    #print(s[i],end="")
for blue in s:
    print(blue)
s = "hello goodbye"
x, y = s.split()
print(y, x, len(y), len(x))