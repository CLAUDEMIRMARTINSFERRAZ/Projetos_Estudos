#Calculadora Simples

from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import st
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

#Cores
cor1 = '#b0aeb5' #cinza
cor2 ='#f4f2f7' #Branca
cor3 = '#0c1bed' #Azul 
cor4 = '#e0f52a' #amarelo
cor5 = '#f77605' #Laranja


janela = Tk()
janela.title('Calculadora')
janela.geometry('235x300')
janela.config(bg=cor1)

#Craindo Frames
frame_tela = Frame (janela, width= 235, height = 50, bg=cor3)
frame_tela.grid(row=0, column= 0)

frame_corpo = Frame (janela, width= 235, height =268)
frame_corpo.grid(row=1, column= 0)


#Variavel para todos os valores

todos_valores = ''

#Criando label da tela
valor_texto = StringVar()

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)



#passando valor para tela principal
    valor_texto.set(todos_valores)

#Função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#funçãod e limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

app_label = Label (frame_tela, textvariable= valor_texto, width=16, height= 2 , padx= 7 , relief=FLAT, anchor= 'e', justify=RIGHT,font= ('Ivy 18') )
app_label.place(x=0, y=0)

#Criando os botões

b_1 = Button (frame_corpo, text='C',command=limpar_tela , width=11, height=2, bg= cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=0)
b_2 = Button (frame_corpo, command=lambda: entrar_valores('%'), text='%', width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118,y=0)
b_3 = Button (frame_corpo,command=lambda: entrar_valores('/' ), text='/', width=5, height=2, bg= cor5, fg= cor2, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177,y=0)

b_4 = Button (frame_corpo, command=lambda: entrar_valores('7'),text='7', width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0,y=50)
b_5 = Button (frame_corpo,command=lambda: entrar_valores('8'), text='8', width=5, height=2, bg= cor4,font= ('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=59,y=50)
b_6 = Button (frame_corpo, command=lambda: entrar_valores('9'),text='9', width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118,y=50)
b_7 = Button (frame_corpo, command=lambda: entrar_valores('*'),text='*', width=5, height=2, bg= cor5, fg= cor2, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177,y=50)

b_8 = Button (frame_corpo, command=lambda: entrar_valores('4'),text='4', width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0,y=100)
b_9 = Button (frame_corpo, command=lambda: entrar_valores('5'), text= '5', width=5, height=2, bg= cor4,font= ('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=59,y=100)
b_10 = Button (frame_corpo, command=lambda: entrar_valores('6'), text= '6' , width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118,y=100)
b_11 = Button (frame_corpo, command=lambda: entrar_valores('-'),text='-', width=5, height=2, bg= cor5, fg= cor2, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177,y=100)

b_12 = Button (frame_corpo, command=lambda: entrar_valores('1'),text='1', width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0,y=150)
b_13 = Button (frame_corpo,command=lambda: entrar_valores('2'), text='2', width=5, height=2, bg= cor4,font= ('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=59,y=150)
b_14 = Button (frame_corpo, command=lambda: entrar_valores('3'),text='3', width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118,y=150)
b_15 = Button (frame_corpo, command=lambda: entrar_valores('+'),text='+', width=5, height=2, bg= cor5, fg= cor2, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177,y=150)

b_1 = Button (frame_corpo, command=lambda: entrar_valores('0'),text='0', width=11, height=2, bg= cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0,y=200)
b_2 = Button (frame_corpo, command=lambda: entrar_valores('.'), text='.', width=5, height=2, bg=cor4, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118,y=200)
b_3 = Button (frame_corpo, command=calcular,text='=', width=5, height=2, bg= cor5, fg= cor2, font= ('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177,y=200)


janela.mainloop()