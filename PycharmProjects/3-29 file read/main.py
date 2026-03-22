'''
myfile = open("c:/code/tuesday.txt","r")
s=myfile.readline()
print(s)
print (len(s))
s = s.rstrip()
print(s)
print(len(s))
'''
myfile = open("c:/code/tuesday.txt","r")
s=myfile.readline()
while (len(s) != 0):
    s=s.rstrip()
    print(s)
    s=myfile.readline()
myfile.close()
