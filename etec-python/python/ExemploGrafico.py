from tkinter import *


def impDados():
  print("Nome =", txtNome.get())
  print("Telefone =", txtTelefone.get())
  print("Email = ", txtEmail.get())
  print("Obs: ", txtobs.get("1.0", END))


app = Tk()

app.title("Janela Gráfica com Python.")
app.geometry("500x400")
app.configure(background='#ade')

lblNome = Label(app, text="Nome do Usuário: ", background='#fff')
lblNome.place(x=40,y=50, width=100, height=20)
txtNome=Entry(app)
txtNome.place(x=150,y=50,width=200,height=20)


lblTelefone = Label(app, text="Telefone: ", background="#fff")
lblTelefone.place(x=40,y=80, width=100, height=20)
txtTelefone=Entry(app)
txtTelefone.place(x=150,y=80,width=200,height=20)

lblEmail = Label(app, text="E-mail: ", background="#fff")
lblEmail.place(x=40,y=110, width=100, height=20)
txtEmail=Entry(app)
txtEmail.place(x=150,y=110,width=200,height=20)

lblobs = Label(app, text="Obs.", background="#dde", foreground="#009")
lblobs.place(x=40, y=140, width=100, height=20)
txtobs = Text(app)
txtobs.place(x=150,y=140,width=200,height=50)


btnImp = Button(app, text="Imprimir", command=impDados)
btnImp.place(x=180,y=200,width=80,height=20)

app.mainloop()