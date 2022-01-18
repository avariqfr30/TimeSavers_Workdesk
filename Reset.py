import subprocess
from tkinter import *


#General setup
root = Tk()
root.geometry('300x200')
root.title("Reset Password")

#Function
def ResetPassword():
    Password = open("Password",'r').read()
    if (Password == PasswordTextArea.get()):
        open('Password','w').write(NewPasswordTextArea.get())
        root.withdraw()
        subprocess.run(['python','Main.py'])
        root.destroy()
        quit()
    else:
        PasswordTextArea.delete(0,'end')
        NewPasswordTextArea.delete(0,'end')


#Labels and password entering areas:
Label(root, font=('arial',8,'bold'), text="Please enter old password:").pack()
PasswordTextArea = Entry(root, width=30)
PasswordTextArea.pack()

Label(root, font=('arial',8,'bold'), text="Please enter new password").pack()
NewPasswordTextArea = Entry(root, width=30)
NewPasswordTextArea.pack()

Button(root, text="Reset", command=ResetPassword).pack()

root.mainloop()