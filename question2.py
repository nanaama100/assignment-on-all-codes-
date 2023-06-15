UserName = "deluxe100"
PassWord = "password@123"
count = 0 
while count < 4: 
    UserName = str(input("enter username: "))
    PassWord = str(input("enter password: ")) 
    if UserName == "deluxe100" and PassWord == "password@123":
        print("Login Successful") 
        break 
    elif count == 3:
        print("Your Login attempt has exceeded the maximum, please try again later")
        break 
    else:
        print("Input info incorrect, please try again")
        count = count + 1 


    
    
    



    
        
    










        

    


