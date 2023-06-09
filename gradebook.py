import time, statistics
username = "Admin"
password = 'password'


#defining a loop for the user to login. Can's access the gradebook until true.
def loginsequence():
    login = False
    while login == False:
        userinput = input('Enter your username:' )
        if username == userinput:
            passwordtry = input("Enter Your password:")
            if passwordtry == password:
                print()
                login = True
                return login
            else:
                print("Thats not right.")
        else:
            print('sorry that is not right')



loginsequence()

#Making more like a real program. Load times. 
print("Wait... Logging on")
time.sleep(5)

class Student_Grades:
    def __init__(self):
        self.definitions = {}

    def addgrade(self,name,grade):
        self.definitions[name] = grade
    




studentgrades = Student_Grades()

#This function allows the user to choose what they want to do within the gradebook. Via entering numbers and then definitions to add to a dictionary of students and their grades. 
def makingchoices():
    pick = '0' 
    list = ('1','2','3','4','0')
    while pick == '0':
        print('\n-Enter [1] to enter student names and grades.\n-Enter [2] to view student names and grades\n-Enter [3] to delete student from gradebook\n-Enter [4] to logout')
        pick = input("Make a single selection:")
        
    if pick == '1':
        name = input("enter student name: ")
        grade = int(input("enter grade as a number:"))
        studentgrades.addgrade(name, grade)
        print(f"\nName added {name}: with a grade of {grade} to gradebook: \n")

        
    if pick =='2':
        print('\nCurrent gradebook: \n')
        print (studentgrades.definitions)
    if pick =='3':
        deletestudent = input("Enter the name of the student you wish to delete: ")
        if deletestudent not in studentgrades.definitions:
            try:
                print('\nThis is not found in the gradebook\n')
                pick = "3"
            except:
                ValueError
        if deletestudent in studentgrades.definitions:
            studentgrades.definitions.pop(deletestudent)
            print("\n"+str(deletestudent)+" has been removed from the gradebook.\n")
    if pick not in list:
        try:
            print("\nPlease choose one of the listed options\n")
            pick = '0'
        except:
            ValueError
    return pick
print('\nWelcome To Grade-Book!')
last_pick = '-1'
while (last_pick != '4'):
    last_pick = makingchoices()
