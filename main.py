
#ask for user input
passw = str(input("input a password: "))

passs = False 

#lc uc stuff 
count = 0 
count2 = 0


#special ch stuff up here for neatness
char = "!,@,#,$,%,^,&,*,(,-,=, ;,',:,,,.,/,<,>,?"

num = "1,2,3,4,5,6,7,8,9,0"


#create while loop
while passw == False :
  #8- 16 characters
  if str(len(passw)) < 8 or str(len(passw)) > 16 :
    passw == str(False) 
    print("invalid")
      
  #lowercase and UPPERCASE
  elif count < 1 or count2 < 1:
   
    for c in passw :
      if (c.islower()):
        count = count + 1 
    for c in passw :
      if (c.isupper()):
        count2 = count2 + 1 
    passw == False
    print("invalid")

  #number and special char
  elif passw != num or passw != char :
    passw == False 
    print ("invalid")
  else :
   passw == True
   print ("valid") 
 
  

   
  
