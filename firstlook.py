def Information():
    print "Account Information"
    print "Name:",Student
    print "Age:",Age
    print "School or University:",School
def Announcements():
    print "Welcome to Nerdism, You currently have no Announcements"
def Exams():
    return Information()
    print "Exams have not yet started."
print "Welcome to Nerdism V0.1 Beta Version"
print "Please fill in your details so you can access the Nerdism Service"
Student=raw_input("What is your name?")
Age=input("How old are you?")
School=raw_input("Which school do you go to?")
print "Menu"
print "1.View Profile"
print "2.Announcements"
print "3.Exams"
Choice=raw_input("Enter your Choice:")
if Choice == '1':
   Information()
elif Choice == '2':
     Announcements()
elif Choice == '3':
     Exams()
else:
    print "You havent chosen anything"
