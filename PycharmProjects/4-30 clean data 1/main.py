infile = open("c:/code/flies.csv", "r")
allflies=[]
for s in infile:
    l = s.split(",")
    allflies.append(l)
print(allflies)
print(allflies[1])
print(allflies [1][3])
