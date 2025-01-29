Course={
       "UI/UX":5000 ,
       "Django":15000 ,
       "python":8000, 
       "Java":7000 
}
total_amt=0
print("Welcome to our IT courses")
def menu_list():
        print("List of courses:")
        for menu in Course:
                print(menu,":", Course[menu])

menu_list()
subject=input("Enter the subject you would like to take:")
if subject in Course:
        total_amt+=Course[subject]
        # print("Your total amount=", total_amt)
else:
        print("We donot have such course")

menu_list()
ask_agn=input("Do you want to add another course also?(yes/No)")
if ask_agn=="yes":
        menu_list()
        subject=input("Enter the subject you would like to add:")
        if subject in Course:
                total_amt+=Course[subject]
                print("Your total amount=", total_amt)
        else:
                print("We donot have such course")   
else:
        print("Your total amount=", total_amt)        




