#PASSOWRD GENERATOR (Mini Project)
#1.Must have a minimum of 8 characters
#2.At least 1 Upper Case
#3.At least 1 lower Case
#4.At least 1 number
#5.At least 1 special character
#6. Must Generate a unique password

#Things we need (Building blocks)
#1. List all upper case .... choose 1 randomly
#2. List all numbers ... choose 1 randomly
#3. List all lower case ....choose 1 randomly

# import random
#
# def passwordGenerator():
#     lowerchars = ['a', 'b', 'c', 'd', 'e']
#     upperchars = ['A', 'B', 'C', 'D', 'E']
#     specialchars = ['&', '!', '*']
#     numericchars = ['1', '2', '3', '4', '5', '6']
#
#     password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(numericchars)
#     password = password + password
#     return password
#
# print(passwordGenerator())


#Random password generator using Tkinter (test 1)
# import random
# from tkinter import *
# import string
#
# def passwordGenerator():
#     password = list()
#     for i in range(5):
#         alpha = random.choice(string.ascii_letters)
#         symbol = random.choice(string.punctuation)
#         numbers = random.choice(string.digits)
#         password.append(alpha)
#         password.append(symbol)
#         password.append(numbers)
#     password_string = "".join(str(x) for x in password)
#     label1.config(text=password_string)
#
#
#
# root = Tk()
#
# root.geometry("250x200")
# button1 = Button(root, text="Generate password", command=passwordGenerator)
# button1.grid(row=2, column=2)
#
# label1 = Label(root, font=("times", 15, "bold"))
# label1.grid(row=4, column=2)
#
# root.mainloop()


#Random password generator using Tkinter (test 2)
import random
from tkinter import *
import string

root = Tk()

root.geometry("450x250")
root.title("Secure Password Generator (Produced by GeoTech)")

#intro text
intro_text = StringVar()
label1 = Label(root, textvariable=intro_text).pack()
intro_text.set("Password Strength:")


def selection():
    selection = choice.get()

choice = IntVar()
radio_but1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
radio_but2 = Radiobutton(root, text="MEDIUM", variable=choice, value=2, command=selection).pack(anchor=CENTER)
radio_but3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection).pack(anchor=CENTER)

Labelchoice = Label(root)
Labelchoice.pack()

lenlabel = StringVar()
lenlabel.set("Password length")
lentitle = Label(root, textvariable=lenlabel).pack()

val = IntVar()
spinlength = Spinbox(root, from_=8, to_=34, textvariable=val, width=20).pack()


def callback():
    password_label.config(text=password_gen())

generate_button = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3, padx=3)
generate_button.pack()

password = str(callback)

password_label = Label(root, text="", font=("times", 15, "bold"), fg="blue")
password_label.pack(side=BOTTOM)

#Logic for creating various password types
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
advanced = poor + average + string.punctuation

def password_gen():
    if choice.get()==1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average, val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advanced, val.get()))

root.mainloop()
