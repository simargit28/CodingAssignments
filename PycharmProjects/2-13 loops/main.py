'''
a = 3
b = a
while ( a == b):
    #print("in loop")
    c=4
    d=5
'''
#count from 1 to 10 inclusive
'''
counter = 1
while(counter <= 10):
    print ("in loop", counter)
    counter = counter + 1
# count from 10 to 1 backwards
counter=10
while (counter >=1):
    print("in loop",counter)
    counter=counter- 1
# count from 1-50 by 2's
counter=1
while(counter <= 50 ):
    print("in loop", counter)
    counter += 2
# count from 1-10 using a flag
stopper=False
counter=1
while(stopper == False):
    print("in loop", counter )
    counter+=1
    if(counter >=10):
        stopper= True
'''
item= input("what item are you looking at?")
while (item != "peas" and item != "ENDOFSTORE"):
    print ("go get next item")
    item = input ("what item are you looking at?")


