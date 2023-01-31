import string
import random
def captcha():
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    global cap
    cap=res
    print("The generated random string : " + str(res))
    
 
i=0
a='admin'
b='admin'
while(i<3):
   user_name=input('Enter the user Name')
   password=input('Enter the Password')
   if(user_name==a and password==b):
      print('Valid Credentials')
      break;
   elif(user_name!=a and password!=b):
       print('Invalid Credentials')
       i=i+1
       if(i==3):
           print('\n',' ***This is your last chance***')
           user_name=input('Enter the user Name')
           password=input('Enter the Password')
           captcha()
           d=input('Enter the above captcha')
           if(user_name==a and password==b and d==cap):
               print('your password is correct')
           else:
               print('Your Password is still Incorrect ','\n','Your Account is locked')
            
            
   
   

 
            
            

