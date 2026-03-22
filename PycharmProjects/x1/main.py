import statistics


b = 4%2
print(b)








'''
l=[51,52,50,49,49,50,51,48,50,51,52,58]
n=12
#compute mean
m = statistics.mean(l)
print(m)
summ = 0
for i in l:
    summ += (i - m)**2
summ = summ / n
summ = summ ** .5
print(summ)
print(statistics.pstdev(l))
'''