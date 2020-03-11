#Calculate the attendance of a student by taking input of class_held and class_attended.
#attendance = (class_attended/class_held)  * 100. If attendace is less than 75 then, ask student for any
#medical certifiate. If medicate certificate is there. Print Student can sit in exam. If attendace is less
#than 75 and student doesn't have medical certifcate then print student can't sit in exam.

#If student percentage is greater thn 75. Then, student is allowed to sit in exam.

class_held = int( input("Enter the number of class held = " ))
class_attended = int( input("Enter the number of class attended = " ))

if( class_attended > class_held ):
    print("Wrong Input")

else:
    attendance = (class_attended/class_held) * 100

    if( attendance >= 75 ):
        print(f"Student is allowed to sit in class and attendance% = {attendance}")

    else:
        medical_issue = input("Do you have any medical problem : Y/N = ")
        if(medical_issue == 'Y'):
            print(f"Student is allowed to sit in class and attendance% = {attendance}")

        elif( medical_issue == 'N' ):
            print(f"Student is not allowed to sit in class and attendance% = {attendance}")

        else:
            print("Wrong Input")

#Note : This is nested if-else program. if inside outer if or outer else.