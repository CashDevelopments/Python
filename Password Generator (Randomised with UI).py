############################################################################################################
##                         Password Generator with User Interface by 💸#8658                             ##
############################################################################################################

from tkinter import *
import random
import string
root=Tk()
root.geometry("600x140")
root.title("Cash Developments | Password Generator")
root.configure(bg="#2c2a2a")
passString=StringVar()
passLength=IntVar()
passLength.set(8)

def Setup():
    global length, passString

    def generate():

        global length, passString
        pass1=string.ascii_letters+string.digits+string.punctuation
        password=""
        for x in range(passLength.get()):
            password=password+random.choice(pass1)
        passString.set(password)

    def save():
        random_password = passString.get()
        f= open("Generated Passwords.txt", "a")
        f.write(random_password)
        f.write("\n")
        f.close()

    pass_label=Label(root, text="Password Length", bg="#3d3d3d", fg="#ffffff", font="courier 14 bold")
    pass_label.place(x=30, y=30)

    length=Entry(root, textvariable=passLength)
    length.place(x=210, y=30, height= 26, width=200)

    gen_passbtn=Button(root, text="Generate", font="courier", width=16, bg="#3d3d3d", fg="#ffffff", command=generate)
    gen_passbtn.place(x=30, y=80)

    gen_passentry=Entry(root, textvariable=passString)
    gen_passentry.place(x=210, y=80, height=29, width=200)

    save_btn=Button(root, text="Save", font="courier", width= 12, bg="#3d3d3d", fg="#ffffff", command=save)
    save_btn.place(x= 440,y=80)

def reset():
    global length, passString
    length.delete(0, END)
    passString.set("")

reset_btn=Button(root, text= "Reset", width=12, bg="#3d3d3d", fg="#ffffff", font= "courier", command=reset)
reset_btn.place(x=440, y=25)
Setup()
mainloop()
