from tkinter import *
from tkinter.filedialog import asksaveasfile
import math
import json

root = Tk()
root.geometry("400x300")

v1 = DoubleVar()
v2 = DoubleVar()
f1 = DoubleVar()


def savejson():
    f = asksaveasfile(initialfile = 'Wyniki.json',
                        defaultextension=".json",filetypes=[("All Files","*.*"),("Json File","*.json")])
    wyniki = cal1()
    f.write(json.dumps({
        'h1':wyniki[0],
        'h2':wyniki[1],
        'f':wyniki[2],
        'd':wyniki[3],
        'frenel':wyniki[4]
    }))



def cal1():
    global v1, v2, l1
    R = 6371 * 1000
    d1 = math.sqrt(2 * (4 / 3) * R * v1.get())
    d2 = math.sqrt(2 * (4 / 3) * R * v2.get())
    d = d1 + d2
    f = int(f1.get())
    frenel = round(17.31*(math.sqrt((d)/(4*f))),2)
    l1.config(text=f"F = {f}\n D = {d}")
    return (v1.get(),v2.get(),f,d,frenel)



e1 = Entry(root, textvariable=f1)

s1 = Scale(root, variable=v1,
           from_=0, to=100,
           orient=HORIZONTAL)
s2 = Scale(root, variable=v2,
           from_=0, to=100,
           orient=HORIZONTAL)

b2 = Button(root, text="Wynik to: ",
            command=cal1)
b3 = Button(root, text="Zapisz do json: ",
            command=savejson)


l1 = Label(root)

s1.pack(anchor=CENTER)
s2.pack(anchor=CENTER)
e1.pack(anchor=CENTER)
l1.pack()
b2.pack(anchor=CENTER)

b3.pack(anchor=CENTER)

root.mainloop()