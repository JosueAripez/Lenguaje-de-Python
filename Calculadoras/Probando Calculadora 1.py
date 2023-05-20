# --- Importando ---

from tkinter import *
from tkinter import messagebox
import math

# --- Ventana ---

Ventana = Tk()
Ventana.title("Kalkulilo")
Ventana.iconbitmap("Calculadoras\imagenes\icono-Calculadora.ico")
Ventana.resizable(0,0)
Ventana.configure(background="black")
Ventana.geometry("318x460+10+10")
Ventana.config(cursor="hand2")

# --- Funciones ---

def Ent_Valores(tecla):
    try:
        if tecla >= "0" and tecla <= "9" or tecla == ".":
            Ent_Win.set(Ent_Win.get() + tecla)
            
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            if tecla == "*":
                Ent_Win.set(Ent_Win.get() + "*")
            elif tecla == "/":
                Ent_Win.set(Ent_Win.get() + "/")
            elif tecla == "+":
                Ent_Win.set(Ent_Win.get() + "+")
            elif tecla == "-":
                Ent_Win.set(Ent_Win.get() + "-")
    except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        Ent_Win.set("")
        
def Ent_Val_T(event):
    try:
        tecla = event.char
        Ent_Valores(tecla)
    except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        Ent_Win.set("")

def Mos_Res(tecla, *args):
    try:
        resultado = eval(Ent_Win.get())
        Ent_Win.set(resultado)
    except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        Ent_Win.set("")
        
def Raiz_Cuadrada():
    try:
        resultado = math.sqrt(float(Ent_Win.get()))
        Ent_Win.set(resultado)
    except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        Ent_Win.set("")
    
def Del(*args):
    inicio = 0
    final = len(Ent_Win.get())
    Ent_Win.set(Ent_Win.get()[inicio:final-1])
    
def C_Borrar(*args):
    Ent_Win.set("")
    
def Mmas():
    resultado = eval(Ent_Win.get()) + float(Ent_Win.get())
    Ent_Win.set(resultado)

def Mmenos():
    resultado = eval(Ent_Win.get()) - float(Ent_Win.get())
    Ent_Win.set(resultado)
    
def Mc():
    Ent_Win.set("")
    
def Mr_Ms():
    try:
        resultado = eval(Ent_Win.get())
        Ent_Win.set(resultado)
    except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        Ent_Win.set("")
    
def Uno_X():
    try:
        resultado = 1/float(Ent_Win.get())
        Ent_Win.set(resultado)
    except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        Ent_Win.set("")
    
def Porciento():
    try:
        resultado = float(Ent_Win.get())/100
        Ent_Win.set(resultado)
    except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        Ent_Win.set("")
        
def Mas_Menos():
   print("")

# --- Widgets --- 

Barra_Menu = Menu(Ventana)
Menu_Mas = Menu(Barra_Menu, tearoff=0)
Menu_Mas.add_command(label="Atajos", command=lambda: messagebox.showinfo("Atajos", "Presione en su teclado\n C --> Borrar Todo\n D --> Borrar un Digito\n Enter --> Mostar Resultado\n Numeros y (/ * - +) --> Para Escribir\n"))
Menu_Mas.add_command(label="Info", command=lambda: messagebox.showinfo("Informacio", " Creado por: Josue Aripez\n UABC - FIAD - Ing.Com."))
Menu_Mas.add_separator()
Menu_Mas.add_command(label="Salir", command=lambda: Ventana.destroy())
Barra_Menu.add_cascade(label="...",menu=Menu_Mas)
Ventana.config(menu=Barra_Menu)

Ent_Win = StringVar()
Win_res = Entry(Ventana, fg="black", font=("Verdana", 25), width=14, justify=RIGHT, textvariable=Ent_Win, borderwidth=2)
Win_res.place(x=10, y=20)
Win_res.insert(0, "Bonvenon")
Btn_Mc = Button(Ventana, text="MC", width=7, height=3, background="gray26", fg="gray63", command=lambda: Mc())
Btn_Mc.place(x=10, y=80)
Btn_Mr = Button(Ventana, text="MR", width=7, height=3, background="gray26", fg="gray63", command=lambda:Mr_Ms())
Btn_Mr.place(x=70, y=80)
Btn_Ms = Button(Ventana, text="MS", width=7, height=3, background="gray26", fg="gray63", command=lambda: Mr_Ms())
Btn_Ms.place(x=130, y=80)
Btn_Mmas = Button(Ventana, text="M+", width=7, height=3, background="gray26", fg="gray63", command=lambda: Mmas())
Btn_Mmas.place(x=190, y=80)
Btn_Mmenos = Button(Ventana, text="M-", width=7, height=3, background="gray26", fg="gray63", command=lambda: Mmenos())
Btn_Mmenos.place(x=250, y=80)

Btn_Pi = Button(Ventana, text="π", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Win_res.insert(0, "3.1416"))
Btn_Pi.place(x=10, y=138)
Btn_Mas_Menos = Button(Ventana, text="±", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Mas_Menos())
Btn_Mas_Menos.place(x=70, y=138)
Btn_Uno_x = Button(Ventana, text="1/X", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Uno_X())
Btn_Uno_x.place(x=130, y=138)
Btn_C = Button(Ventana, text="C", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: C_Borrar())
Btn_C.place(x=190, y=138)
Btn_Del = Button(Ventana, text="DEL", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Del())
Btn_Del.place(x=250, y=138)

Btn_Num7 = Button(Ventana, text="7", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("7"))
Btn_Num7.place(x=10, y=196)
Btn_Num8 = Button(Ventana, text="8", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("8"))
Btn_Num8.place(x=70, y=196)
Btn_Num9 = Button(Ventana, text="9", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("9"))
Btn_Num9.place(x=130, y=196)
Btn_Mas = Button(Ventana, text="+", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Ent_Valores("+"))
Btn_Mas.place(x=190, y=196)
Btn_Sqr = Button(Ventana, text="√", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Raiz_Cuadrada())
Btn_Sqr.place(x=250, y=196)

Btn_Num4 = Button(Ventana, text="4", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("4"))
Btn_Num4.place(x=10, y=254)
Btn_Num5 = Button(Ventana, text="5", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("5"))
Btn_Num5.place(x=70, y=254)
Btn_Num6 = Button(Ventana, text="6", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("6"))
Btn_Num6.place(x=130, y=254)
Btn_Menos = Button(Ventana, text="-", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Ent_Valores("-"))
Btn_Menos.place(x=190, y=254)
Btn_Porcen = Button(Ventana, text="%", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Porciento())
Btn_Porcen.place(x=250, y=254)

Btn_Num1 = Button(Ventana, text="1", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("1"))
Btn_Num1.place(x=10, y=312)
Btn_Num2 = Button(Ventana, text="2", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("2"))
Btn_Num2.place(x=70, y=312)
Btn_Num3 = Button(Ventana, text="3", width=7, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("3"))
Btn_Num3.place(x=130, y=312)
Btn_Mul = Button(Ventana, text="×", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Ent_Valores("*"))
Btn_Mul.place(x=190, y=312)
Btn_Igual = Button(Ventana, text="=", width=7, height=7, background="DodgerBlue3", fg="white", command=lambda: Mos_Res("="))
Btn_Igual.place(x=250, y=312)

Btn_Num0 = Button(Ventana, text="0", width=15, height=3, background="gray26", fg="white", command=lambda: Ent_Valores("0"))
Btn_Num0.place(x=10, y=370)
Btn_Punto = Button(Ventana, text=".", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Ent_Valores("."))
Btn_Punto.place(x=130, y=370)
Btn_Div = Button(Ventana, text="÷", width=7, height=3, background="gray26", fg="DodgerBlue3", command=lambda: Ent_Valores("/"))
Btn_Div.place(x=190, y=370)

# --- Extras ---

Ventana.bind("<Key>", Ent_Val_T)
Ventana.bind("<KeyPress-d>", Del)
Ventana.bind("<KeyPress-c>", C_Borrar)
Ventana.bind("<KeyPress-Return>", Mos_Res)

# --- Fin ---
Ventana.mainloop()

"""                                                                                                                                                                                                                                  
RRRRRRRRRRRRRRRRR                     jjjj                                                                           
R::::::::::::::::R                   j::::j                                                                          
R::::::RRRRRR:::::R                   jjjj                                                                           
RR:::::R     R:::::R                                                                                                 
  R::::R     R:::::R   ooooooooooo  jjjjjjj  aaaaaaaaaaaaa  ppppp   ppppppppp       eeeeeeeeeeee    zzzzzzzzzzzzzzzzz
  R::::R     R:::::R oo:::::::::::ooj:::::j  a::::::::::::a p::::ppp:::::::::p    ee::::::::::::ee  z:::::::::::::::z
  R::::RRRRRR:::::R o:::::::::::::::oj::::j  aaaaaaaaa:::::ap:::::::::::::::::p  e::::::eeeee:::::eez::::::::::::::z 
  R:::::::::::::RR  o:::::ooooo:::::oj::::j           a::::app::::::ppppp::::::pe::::::e     e:::::ezzzzzzzz::::::z  
  R::::RRRRRR:::::R o::::o     o::::oj::::j    aaaaaaa:::::a p:::::p     p:::::pe:::::::eeeee::::::e      z::::::z   
  R::::R     R:::::Ro::::o     o::::oj::::j  aa::::::::::::a p:::::p     p:::::pe:::::::::::::::::e      z::::::z    
  R::::R     R:::::Ro::::o     o::::oj::::j a::::aaaa::::::a p:::::p     p:::::pe::::::eeeeeeeeeee      z::::::z     
  R::::R     R:::::Ro::::o     o::::oj::::ja::::a    a:::::a p:::::p    p::::::pe:::::::e              z::::::z      
RR:::::R     R:::::Ro:::::ooooo:::::oj::::ja::::a    a:::::a p:::::ppppp:::::::pe::::::::e            z::::::zzzzzzzz
R::::::R     R:::::Ro:::::::::::::::oj::::ja:::::aaaa::::::a p::::::::::::::::p  e::::::::eeeeeeee   z::::::::::::::z
R::::::R     R:::::R oo:::::::::::oo j::::j a::::::::::aa:::ap::::::::::::::pp    ee:::::::::::::e  z:::::::::::::::z
RRRRRRRR     RRRRRRR   ooooooooooo   j::::j  aaaaaaaaaa  aaaap::::::pppppppp        eeeeeeeeeeeeee  zzzzzzzzzzzzzzzzz
                                     j::::j                  p:::::p                                                 
                           jjjj      j::::j                  p:::::p                                                 
                          j::::jj   j:::::j                 p:::::::p                                                
                          j::::::jjj::::::j                 p:::::::p                                                
                           jj::::::::::::j                  p:::::::p                                                
                             jjj::::::jjj                   ppppppppp                                                
                                jjjjjj                                                                               
"""