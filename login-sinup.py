
import json, os
 
def sinup():
   if os.path.exists("data.json"):
       with open("data.json", "r") as f:
           allDetails = json.load(f)
   else:
       allDetails = []
 
   userData = {
           "name":input("Enter your name: "),
           "username":input("Enter your username: "),
           "email":input("Enter email: "),
           "password":input("Enter your password: "),
           "dob":input("Enter your date of birth: ")
       }
      
  
   allDetails.append(userData)
   with open("data.json", 'w') as f:
    
       json.dump(allDetails, f, indent=4)
     
   print("successfully sinup\nThankyou!!!!!!!!!!!!!!!!")
 
def login(inputEmail, inputPassword):
   with open("data.json", "r") as f:
       allDetails = json.load(f)
 
   for detail in allDetails:
       if detail['email'] == inputEmail and detail['password'] == inputPassword:
           return f"welcome your login successfully-{detail['name']}"
   return "invalid input"
 
 
choose = int(input("press - 1 for Sinup : - \npresss - 2 for Login : - "))
if choose == 1:
   sinup()
else:
   print(login(input("email"), input("password")))











