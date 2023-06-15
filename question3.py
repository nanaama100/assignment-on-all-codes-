num_integers = 2,4,-3,1,-5,6,-7,8,-9,10
total = 0 
for i in num_integers: 
    if i < 0:
        continue
    if i > 0: 
        print (i)
    total = total + i 
print("the sum of remaining positive numbers = ", total)


