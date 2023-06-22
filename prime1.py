import math 
for num in range(2,50): 
    num1 = int(input("enter positive number greater than 1: ")) 
    for i in range(2, int(math.sqrt(num)+1)):
        if num1 % i == 0:
            print(num1, " -Number is not a prime number") 
            break 
    else: 
        print(num1, " -Number is a prime number")
    
    
    
   


 