array = [6, 1, 3, 9, 4, 0, 8, 7, 2]
for i in range (0,8):
    for j in range (0,8):
        if (array [j] > array [j +1]):
            temp = array [j]
            array [j] = array [j+1]
            array [j+1] = temp
print (array)

# or array.sort()

