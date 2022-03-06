from tkinter.simpledialog import askinteger


CHILD_AGE = 13
age = int(input("What is your age?"))
if age < CHILD_AGE:
    print("You pay the child price!")
print("Welcome to the zoo.")
