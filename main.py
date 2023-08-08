#Importações
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date
#Estruturas:
janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry("500x600")
janela.config(bg="black")

#Parte de cima
forms = Frame(janela,width=500, height=200, bg="black", padx=0, pady=0,relief="flat")
forms.grid(row=0,column=0)
#Visor
visor = Frame(janela,width=500, height=400, bg="gray", padx=0, pady=0,relief="flat")
visor.grid(row=1, column=0)

#Crindo a Função
def calcular():
    nascimento= data_1.get()
    atual = data_2.get()
    
    #Tranformando dados:
    dia1, mes1, ano1=[int(f) for f in nascimento.split('/')]
    d_nascimento=date(ano1, mes1, dia1)
    
    dia2, mes2, ano2=[int(f) for f in atual.split('/')]
    d_atual=date(ano2, mes2, dia2)

    dias=relativedelta(d_atual, d_nascimento).days
    meses=relativedelta(d_atual, d_nascimento).months
    anos=relativedelta(d_atual, d_nascimento).years
    
    #Enviando dados:
    r_dia["text"]= dias
    r_mes["text"]= meses
    r_ano["text"]= anos
    
#Textos:
#Parte de cima_Calculadora
l_nome1 = Label(forms,text="Calculadora",width=30, height=1, padx=0, pady=0, relief="flat", anchor="center", font=("Nimbus\Mono\PS 20 bold"), fg="white",bg="black")
l_nome1.place(x=0, y=40)
#Parte de cima_De
l_nome1 = Label(forms,text="de",width=30, height=1, padx=0, pady=0, relief="flat", anchor="center", font=("Nimbus\Mono\PS 20 bold"), fg="white",bg="black")
l_nome1.place(x=0, y=90)
#Parte de cima_Idade
l_nome2 = Label(forms, text="Idade",width=30, height=1, padx=0, pady=0, relief="flat", anchor="center", font=("Nimbus\Mono\PS 20 bold"), fg="white",bg="black")
l_nome2.place(x=0, y=140)
#Visor_Nascimento
l_nome1 = Label(visor,text="Nascimento:",width=0, height=1, padx=0, pady=0, relief="flat", anchor="nw", font=("Nimbus\Mono\PS 20 bold "), fg="black",bg="gray")
l_nome1.place(x=20, y=40)
#Visor_Atual
l_nome2 = Label(visor, text="Data Atual:",width=0, height=1, padx=0, pady=0, relief='flat', anchor='nw', font=("Nimbus\Mono\PS 20 bold"), fg="black",bg="gray")
l_nome2.place(x=20, y=140)

#Calendarios:
#Nascimento
data_1 = DateEntry(visor,width=15, bg="red", fg="white",borderwidth=5, date_patter="dd/mm/y", y=2023,)
data_1.place(x=300, y=45)
#Atual
data_2 = DateEntry(visor,width=15, bg="red", fg="white",borderwidth=5, date_patter="dd/mm/y", y=2023,)
data_2.place(x=300, y=145)

#Resultados
#Resultado_Dia
r_dia = Label(visor, text="",width=0, height=1, relief='flat', anchor='nw', font=("Ani 30 bold"), fg="black",bg="gray")
r_dia.place(x=20, y=230)

#Texto_Dia
t_dia = Label(visor, text="DIAS",width=0, height=1, relief='flat', anchor='nw', font=("Nimbus\Mono\PS 18 bold"), fg="black",bg="gray")
t_dia.place(x=16, y=290)
#Resultado_Mes
r_mes = Label(visor, text="",width=0, height=1, relief='flat', anchor='nw', font=("Ani 30 bold"), fg="black",bg="gray")
r_mes.place(x=210, y=230)
#Texto_Mes
t_mes = Label(visor, text="MESES",width=0, height=1, relief='flat', anchor='nw', font=("Nimbus\Mono\PS 18 bold"), fg="black",bg="gray")
t_mes.place(x=200, y=290)
#Resultado_Ano
r_ano = Label(visor, text="",width=0, height=1, relief='flat', anchor='nw', font=("Ani 30 bold"), fg="black",bg="gray")
r_ano.place(x=410, y=230)
#Texto_Anos
t_ano = Label(visor, text="ANOS",width=0, height=1, relief='flat', anchor='nw', font=("Nimbus\Mono\PS 18 bold"), fg="black",bg="gray")
t_ano.place(x=407, y=290)

#Botão
botão = Button(visor, command=calcular, text="CALCULAR",width=15,height=2, relief="raised", overrelief="ridge", font=("Nimbus\Mono\PS 12 bold"), bg="black", fg="white")
botão.place(x=150, y=335)



janela.mainloop()