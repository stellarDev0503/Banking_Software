from tkinter import *
from PIL import Image, ImageTk
import itertools

root = Tk()
root.title("Best & Bank")
root.geometry("668x504")  # set starting size of window
root.maxsize(668, 504)  # width x height
root.resizable(False, False)

# Insert background
img=Image.open("C:\wonderful.jpg")
photo=ImageTk.PhotoImage(img)
label = Label(image = photo)
label.image_names = photo
label.place(x=-2, y=0)

# Enter specific information for your profile into the following widgets
enter_info = Label(root, text="Please enter your information:",background='black', font=('Times', 24), foreground='#D9CB9E')
enter_info.grid(row=25, column=2, columnspan=4, padx=40, pady=60)

# Name label and entry widgets
Label(root, text="User_ID", background='black', font=('Times', 18), foreground='#D9CB9E').grid(row=30, column=2, padx=40, pady=30, sticky=E)
ID = Entry(root, bd=5, width=20, font=('Times', 18))
ID.grid(row=30, column=4, padx=10, pady=30)

# Password label and entry widgets
Label(root, text="Password", background='black', font=('Times', 18), foreground='#D9CB9E').grid(row=40, column=2, padx=40, pady=30, sticky=E)
password = Entry(root, show="*", bd=5, width=20, font=('Times', 18))
password.grid(row=40, column=4, padx=10, pady=30)

style_1 = {'fg': 'black', 'bg': 'RoyalBlue3', 'activebackground':'gray71', 'activeforeground': 'gray71'}
style_2 = {'fg': 'white', 'bg': 'OliveDrab2', 'activebackground':'gray71', 'activeforeground': 'gray71'}
style_3 = {'fg': 'black', 'bg': 'purple1', 'activebackground':'gray71', 'activeforeground': 'gray71'}
style_4 = {'fg': 'white', 'bg': 'coral2', 'activebackground':'gray71', 'activeforeground': 'gray71'}
style_cycle = itertools.cycle([style_1, style_2, style_3, style_4 ])
#Define a function to update the button style
def update_style():
   style = next(style_cycle)
   btn.configure(**style)

btn = Button(root, text="Submit", font=('Helvetica 18 bold'), command=update_style)
btn.grid(row=50, column=3, padx=30, pady=30)

root.mainloop()