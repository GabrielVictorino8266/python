from tkinter import *

# Importa MessageBox para Python
from tkinter import messagebox


def ResultadoCombustiveis():
    # Recebe informações do preço do combustível
    etanolPreco = float(txtEtanol.get())
    gasolinaPreco = float(txtGasolina.get())
    
    # Recebe informações do preço do consumo
    consumoEtanol = float(txtCarroEtanol.get())
    consumoGasolina = float(txtCarroGasolina.get())

    ResultadoEtanol = etanolPreco / consumoEtanol
    ResultadoGasolina = gasolinaPreco / consumoGasolina

    # Comparações
    if ResultadoEtanol > ResultadoGasolina:
        messagebox.showwarning("Escolha Gasolina", "A gasolina custa: R$" + str(round(ResultadoGasolina, 2))) #Exibe em uma janela
    elif ResultadoGasolina > ResultadoEtanol:
        messagebox.showwarning("Escolha Etanol", "O etanol custa: R$"+ str(round(ResultadoEtanol, 2)))#Exibe em uma janela
    else:
        messagebox.showwarning("Atenção!", "Ambos são iguais.")#Exibe em uma janela

    # Resultado dos Cálculos
    myAnswer = 'O(A) {} está valendo R$ {} .'

    lblResultadoEtanol = Label(app, text=myAnswer.format('Etanol', round(ResultadoEtanol, 2)), background='#fff')
    lblResultadoEtanol.place(x=40,y=230, width=280, height=20)

    lblResultadoGasolina = Label(app, text=myAnswer.format('Gasolina', round(ResultadoGasolina, 2)), background="#fff")
    lblResultadoGasolina.place(x=40,y=260, width=280, height=20)



def Limpar():
    # Função para limpar dados.
    txtCarroEtanol.delete(0, END)
    txtEtanol.delete(0, END)
    txtCarroGasolina.delete(0, END)
    txtGasolina.delete(0, END)
    

app = Tk()

app.title("Atividade Nota QTS Python.")
app.geometry("500x400")
app.configure(background='#ade')

# Preços Combustíveis
lblEtanol = Label(app, text="Etanol: ", background='#fff')
lblEtanol.place(x=40,y=50, width=100, height=20)
txtEtanol=Entry(app)
txtEtanol.place(x=150,y=50,width=200,height=20)


lblGasolina = Label(app, text="Gasolina: ", background="#fff")
lblGasolina.place(x=40,y=80, width=100, height=20)
txtGasolina=Entry(app)
txtGasolina.place(x=150,y=80,width=200,height=20)


# Consumo Médio
lblCarroEtanol = Label(app, text="Carro Etanol: ", background='#fff')
lblCarroEtanol.place(x=40,y=110, width=100, height=20)
txtCarroEtanol=Entry(app)
txtCarroEtanol.place(x=150,y=110,width=200,height=20)


lblCarroGasolina = Label(app, text="Carro Gasolina: ", background="#fff")
lblCarroGasolina.place(x=40,y=140, width=100, height=20)
txtCarroGasolina=Entry(app)
txtCarroGasolina.place(x=150,y=140,width=200,height=20)


# Botão Calcular
btnCalc = Button(app, text="Calcular", command=ResultadoCombustiveis)
btnCalc.place(x=120,y=200,width=80,height=20)


# Botão Limpar
btnClean = Button(app, text="Limpar", command=Limpar)
btnClean.place(x=220,y=200,width=80,height=20)


# Executa o app
app.mainloop()