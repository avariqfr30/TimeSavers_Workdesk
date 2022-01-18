from tkinter import *
import subprocess

# Please put the application path and its exr in FilePath:
FilePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

#General Setup
root = Tk()
root.geometry('300x80')
root.title("LOCK")


#Functions
def Enter():
    Password = open("Password",'r').read()

    if (TextArea.get() == Password):
        root.withdraw()
        subprocess.run(FilePath)
        root.destroy()
        quit()
    else:
        TextArea.delete(0, 'end')

def Reset():
    root.withdraw()
    subprocess.run(['python','Reset.py'])
    root.destroy()
    quit()


# Password Entering TextAreas:
TextArea = Entry(root, font=('arial', 10, 'bold'), width=40)
TextArea.place(x=10,y=20)

Button(root, text="Enter", command=Enter).place(x=50,y=50)
Button(root, text="Reset", command=Reset).place(x=190,y=50)

root.mainloop()