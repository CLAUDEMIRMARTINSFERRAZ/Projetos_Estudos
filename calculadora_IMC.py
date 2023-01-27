
from tkinter import *
from tkinter import ttk
from tkinter import font


janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg='white')

#Abaixo do peso = menor de 18,5
#Normal = maior ou igual a 18,5 e menor que 25
#Sobrepeso = Maior ou igual a 25 a menos que 30
#Obsidade = 30 ou mais

# IMC = peso/altura^2

#Cores

cor1= '#fafafa' #Branca
cor2= '#444466' #Preto
cor3= '#ff990a' #laranja


#____Divisão de Pagina__

Frame_cima = Frame(janela, width= 295, height=50, bg= cor1, pady=0, padx=0, relief='flat')
Frame_cima.grid (row=0, column=0, sticky=NSEW)

Frame_baixo = Frame(janela, width= 295, height=180, bg=cor1, pady=0, padx=0, relief='flat')
Frame_baixo.grid (row=1, column=0, sticky=NSEW)


#_______Configurando o Frame cima

app_nome = Label (Frame_cima, text= 'Calculadora de IMC', width= 23, bg= cor1, height=1, padx=0, relief='flat', anchor='center', font= ('Ivy 16 bold'), fg = cor2)
app_nome.place(x=0, y=0)

app_linha = Label (Frame_cima, text= '', width= 450, bg= cor2, height=1, padx=0, relief='flat', anchor= 'center', font= ('Ivy 1'), fg = cor2)
app_linha.place(x=0, y=35)


#-----------FUNÇÂO: Calculo----------

def calcular():
    peso = float (e_peso.get())
    altura=  float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] ='Seu IMC é: Abaixo do Peso. Tome Cuidado.!'
    elif resultado >=18.5  and resultado < 25.0:
        l_resultado_texto['text'] ='Seu IMC é: Normal. Parabéns!'
    elif resultado >=25.0 and  resultado < 30.0:
        l_resultado_texto['text'] ='Seu IMC é: Sobrepeso. Fique Atento!!'
    else:
        l_resultado_texto['text'] ='Seu IMC é: Obsidade. Tome Cuidado!!'

    l_resultado ['text'] = '{:.{}f}'.format(resultado,2)


#_______Configurando o Frame baixo

l_peso = Label (Frame_baixo, text= 'Insira seu Peso', bg= cor1, height=1, padx=0, relief='flat', anchor= 'center', font= ('Ivy 10 bold'), fg = cor2)
l_peso.grid(row=0, column=0, sticky= NSEW, pady= 10, padx=3)
e_peso = Entry (Frame_baixo, width=5, relief='solid', font= ('Ivy 10 bold'),justify='center')
e_peso.grid(row=0, column=1, sticky= NSEW, pady= 10, padx=3)

l_altura = Label (Frame_baixo, text= 'Insira sua Altura', bg= cor1, height=1, padx=0, relief='flat', anchor= 'center', font= ('Ivy 10 bold'), fg = cor2)
l_altura.grid(row=1, column=0, sticky= NSEW, pady= 10, padx=3)
e_altura = Entry (Frame_baixo, width=5, relief='solid', font= ('Ivy 10 bold'),justify='center')
e_altura.grid(row=1, column=1, sticky= NSEW, pady= 10, padx=3)


l_resultado= Label (Frame_baixo, text= '---', width= 5, bg= cor3, height=1, padx=6, pady=12, anchor= 'center', font= ('Ivy 24 bold'), fg = cor1)
l_resultado.place(x=170, y=10)


#========Label para ostrar o resultado

l_resultado= Label (Frame_baixo, text= '---', width= 5, bg= cor3, height=1, padx=6, pady=12, anchor= 'center', font= ('Ivy 24 bold'), fg = cor1)
l_resultado.place(x=175, y=10)

l_resultado_texto= Label (Frame_baixo, text= 'Seu IMC é:', width=37, height=1, padx=0, pady=12, anchor='center', font= ('Ivy 10 bold'), bg= cor1, fg = cor2)
l_resultado_texto.place(x=0, y=105)

l_calcular= Button (Frame_baixo, command=calcular, text= 'Calcular', width=34, height=1, overrelief=SOLID, relief='raised', font= ('Ivy 10 bold'), bg= cor3, fg = cor1)
l_calcular.grid(row=4, column=0, sticky= NSEW, pady= 60, padx=5, columnspan=30)



janela.mainloop()
