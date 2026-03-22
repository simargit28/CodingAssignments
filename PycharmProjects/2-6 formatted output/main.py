
Page
1
of 2
a = 123.4567
print (a) # no formatting, default one space
between
# printed fields, new line following
print
print ("a=",a,sep='') # set seperator to null
print ("a=",a,end='') # set no new line after print
print ("a=",a,sep='P') # set seperator to P
print ("a=",a,end='***') # display *** after print
print (format(a,'.2f')) # print a with two and only two
decimals
print (format(a,'10.2f')) # print a in a 10 char field with 2
decimals
print ('$',format(a,'10.2f')) # add a dollar sign
print (format(a,'.2f')) # print as above and with comma
separators
print (format(a,'20.10f')) # print in a 20 char field with 10
decimals
a = 345 # make a an int
print (format(a,'5.1f')) # 'f" format still works
print (format(a,'10d')) # and so does d - for "decimal" -
which means
# no decimals
a = 12.34 # make a a float again
#print (format(a,'10d')) # will not work - cannot display a
float with 'd'
b=34.4567
# can combine any or all of these with >1 variable...
print ("a=",format(a,'6.2f'), " and ",
"b=",format(b,'8.3f'),sep='')
output
123.4567
a=123.4567
a= 123.4567a=P123.4567
a= 123.4567***123.46
123.46
$ 123.46
123.46
123.4567000000
345.0
