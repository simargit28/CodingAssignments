#count from 1-10 inclusive
counter = 1
while (counter <=10):
    print (counter)
    counter += 1
print(counter)

#counting loops

print("*** part 2 ***")
# count from 1-10 inclusive, as above
for counter in range (1,11):
    print (counter)
for counter in range (1,11,2):
    print(counter)
for counter in range (10,0,-1):
    print(counter)

# iterating through things
print("*** part 3 ***")
# iterate through a list  [ ... ]
list1= [35, -2, 14, 0, 44, 127, 16]
list2=[]
for i in list1:
    print(i)
list3= ["sam,","betty","alamo"]
for j in list3:
    print(j)
list4= list1+list3
for k in list4:
    print(k)
print (type(list4))
# nested loops
hh = 0
mm = 0
ss = 0
for hh in range (00,23+1):
    for mm in range (00,59+1):
        for ss in range (00,59+1):
            print (format(hh, '02d'), ":", format( mm,'02d'), ":", format(ss, '02d'), sep="")
