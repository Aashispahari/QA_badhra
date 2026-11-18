#Python operator 


# student=["Aashish", 25 , True],["John", 30, True]

# for full_name in student: 
#   name, age, is_valid = full_name 

#   if age >= 30 and is_valid:
#     print(f"{name} with age {age} is allowed to play")

#   else: 
#     print(f"{name}is not alloweed to participate")




# name = input("Enter your name:")
# age = int(input("enter you age:")) 

# if age >=18 :
#       print(f"{name} is allowrd to vote")

# else:
#       print(f"{name} is not eligible to vote")  
# 
#  


# Even = int(input("Enter a number:"))

# if Even % 2 == 0 and Even > 0:
#     print(f"{Even} is even number")
# elif Even % 2 != 0 and Even > 0:
#     print(f"{Even} is odd number")

# else:
#     print(f"{Even} is not a valid number")


name = input("Enter your name:")
marks = int(input("Enter your marks:"))

if marks > 100 or marks < 0:
    print(f"{name} you have entered invalid marks")

elif marks >= 80 :
    print(f"Congrtualtions {name} you have got Distinction")

elif marks >=60 :
    print(f"Congrtualtions {name} you have got First Division")

elif marks >=50 :
    print(f"Congrtualtions {name} you have got Second Division")

elif marks >= 40  :
    print(f" {name} you have got Third Division - You need to work hard")

else:
    print(f" {name} you have failed - You are not promoted to next class")








