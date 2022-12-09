from tkinter import *
from tkinter import messagebox


def impDados():

    nota1 = float(txtnota1.get())
    nota2 = float(txtnota1.get())
    nota3 = float(txtnota1.get())
    media = (nota1 + nota2 + nota3)/3
    print("Sua média = ", media)
    messagebox.showinfo(title="Media", message="Sua média é =%s" % media)

app=Tk()
app.title("")
app.geometry("500x300")
app.configure(background="#dde")

vbg="#dde"
vfg="#009"

lblnota1=Label(app, text="Nota 01", background=vbg, foreground=vfg)
lblnota1.place(x=0, y=0, width=100, height=20)
txtnota1=Entry(app)
txtnota1.place(x=40,y=25, width=200, height=20)


lblnota2=Label(app, text="Nota 02", background=vbg, foreground=vfg)
lblnota2.place(x=0, y=50, width=100, height=20)
txtnota2=Entry(app)
txtnota2.place(x=40,y=70, width=200, height=20)


lblnota3=Label(app, text="Nota 03", background=vbg, foreground=vfg)
lblnota3.place(x=0, y=100, width=100, height=20)
txtnota3=Entry(app)
txtnota3.place(x=40,y=120, width=200, height=20)

btnImp = Button(app, text="Calcular", command=impDados)
btnImp.place(x=40,y=170, width=100, height=20)

app.mainloop()