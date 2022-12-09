import tkinter
import tkinter.messagebox
# Custom TkInter
import customtkinter
import sys

# Define o Design da Janela
customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Importa Componentes
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

    lblResultadoEtanol = customtkinter.CTkLabel(app, text=myAnswer.format('Etanol', round(ResultadoEtanol, 2)), background='#fff')
    lblResultadoEtanol.place(x=100,y=300, width=280, height=40)

    lblResultadoGasolina = customtkinter.CTkLabel(app, text=myAnswer.format('Gasolina', round(ResultadoGasolina, 2)), background="#fff")
    lblResultadoGasolina.place(x=100,y=330, width=280, height=40)



def Limpar():
    # Função para limpar dados.
    txtCarroEtanol.delete(0, 'end')
    txtEtanol.delete(0, 'end')
    txtCarroGasolina.delete(0, 'end')
    txtGasolina.delete(0, 'end')
    

app = customtkinter.CTk()

app.title("Atividade Nota QTS Python.")
app.geometry("500x400")
# app.configure(background='#ade')

# Preços Combustíveis
lblEtanol = customtkinter.CTkLabel(app, text="Etanol: ", background='#fff')
lblEtanol.place(x=40,y=50, width=150, height=40)
txtEtanol=customtkinter.CTkEntry(app, corner_radius=20)
txtEtanol.place(x=150,y=50,width=200,height=40)


lblGasolina = customtkinter.CTkLabel(app, text="Gasolina: ", background="#fff")
lblGasolina.place(x=40,y=100, width=150, height=40)
txtGasolina=customtkinter.CTkEntry(app, corner_radius=20)
txtGasolina.place(x=150,y=100,width=200,height=40)


# Consumo Médio
lblCarroEtanol = customtkinter.CTkLabel(app, text="Carro Etanol: ", background='#fff')
lblCarroEtanol.place(x=40,y=150, width=150, height=40)
txtCarroEtanol=customtkinter.CTkEntry(app, corner_radius=20)
txtCarroEtanol.place(x=150,y=150,width=200,height=40)


lblCarroGasolina = customtkinter.CTkLabel(app, text="Carro Gasolina: ", background="#fff")
lblCarroGasolina.place(x=40,y=200, width=150, height=40)
txtCarroGasolina=customtkinter.CTkEntry(app, corner_radius=20)
txtCarroGasolina.place(x=150,y=200,width=200,height=40)


# Botão Calcular
btnCalc = customtkinter.CTkButton(master=app, width=60, height=32, corner_radius=20, text="Calcular", command=ResultadoCombustiveis)
btnCalc.place(x=120, y=250)


# Botão Limpar
btnClean = customtkinter.CTkButton(master=app, width=60, height=32, corner_radius=20, text="Limpar", command=Limpar)
btnClean.place(x=250, y=250)


# Executa o app
app.mainloop()