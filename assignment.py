
#To Obtain valid Science marks
def Science_marks(name):
    while True: 
        Science = int(input("Enter your marks in Science:"))
        if Science > 100 or Science < 0:
            print(f"{name} you have entered invalid marks, Please enter Valid marks")         
        else: return Science

#To obtain valid Math marks
def Maths_marks(name):
    
    while True:
        Maths = int(input("Enter your marks in Maths:"))
        if Maths > 100 or Maths < 0:
            print(f"{name} you have entered invalid marks,Please enter Valid marks")
        else:
            return Maths

#Function to obtain valid english marks
def English_marks(name):
    while True:
        English = int(input("Enter your marks in English:"))
        if English > 100 or English < 0:
            print(f"{name} you have entered invalid marks,Please enter Valid marks")
        else:
            return English

#function to calculate grade            
def Grade_obtained(Average_marks):    
    if Average_marks >= 80 :
        Grade = "A"

    elif Average_marks >=60:
        Grade = "B"

    elif Average_marks >=40:
        Grade = "C"

    else :
        Grade = "D"

    return Grade

#Function to calculate pass or fail
def pass_fail(Average_marks):
    if Average_marks >= 40:
        print ("Pass")
    else:
        print("Fail")

#To Calculate marks and find out grade, average marks and total marks
def calculator():
    # All_students = []
    Highest_marks = 0
    Marks_count = int(input("How many students results you want to enter:"))

    for i in range(Marks_count):
        name = input("Enter your name:")
        Science = Science_marks(name)
        Maths = Maths_marks(name)
        English = English_marks(name)
        

        Total_marks = Science + Maths + English
        Average_marks = Total_marks / 3

        if Average_marks > Highest_marks:
            Highest_marks = Average_marks
            Topper = name

        Grade = Grade_obtained(Average_marks)
        pass_fail(Average_marks)

        # All_students.append({
        #     "Name" : name,
        #     "Science" : Science,
        #     "Maths" : Maths,
        #     "Average_marks":Average_marks,
        #     "Grade" : Grade
        # })

        print(f"Name :{name} Total marks= {Total_marks} Averagemarks = {Average_marks} Grade = {Grade}")
        
    print (f"Congratulations {Topper} for obtaining Highest Marks {Highest_marks}") 

    # for students_details in All_students:
    #     Name ,Science ,Maths, Average_marks,Grade = students_details
    #     print(f"{Name} got {Science} {Maths}, {Average_marks} {Grade} in science")

    



    #Asking user if they want to restart

    while True:
        Again = input("Do You Want to Start Again Y/N: ").upper()
        if Again !="Y" and Again != "N":
            print ("Enter valid INput")

        elif Again == "Y":
            calculator()
            break

        else:
            print("Thankyou")
            break


       

        


calculator()



    




    








    

