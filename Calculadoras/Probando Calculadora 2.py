# --- Importando ---

from tkinter import *
from tkinter import messagebox

# --- Ventana ---

Ventana = Tk()
Ventana.title("Kalkulilo de Bazaj Operacioj")
Ventana.iconbitmap("Calculadoras\imagenes\icono-Calculadora.ico")
Ventana.resizable(0,0)
Ventana.configure(background="black")
Ventana.geometry("445x300")
Ventana.geometry("+10+10")  # +186+63
Ventana.config(cursor="plus")
lbl_nom =Label(Ventana, text="@Rojapez 2023", fg="white", bg="black", font=("Verdana", 10))
lbl_nom.place(x=330, y=270)

# --- Funciones ---

def Sumar():
   
   try:
        Num_1 = Ent_Val1.get()
        Num_2 = Ent_Val2.get()
    
        if Num_1 == "" or Num_2 == "":
            lbl_Res["text"] = "¿?"
            messagebox.showinfo("ERROR", "FALTAN VALORES")
        else:
            Resultado = int(Num_1) + int(Num_2)
            lbl_Res["text"] = Resultado
   except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        
def Restar():
   
   try:
        Num_1 = Ent_Val1.get()
        Num_2 = Ent_Val2.get()
    
        if Num_1 == "" or Num_2 == "":
            lbl_Res["text"] = "¿?"
            messagebox.showinfo("ERROR", "FALTAN VALORES")
        else:
            Resultado = int(Num_1) - int(Num_2)
            lbl_Res["text"] = Resultado
   except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        
def Mul():
   
   try:
        Num_1 = Ent_Val1.get()
        Num_2 = Ent_Val2.get()
    
        if Num_1 == "" or Num_2 == "":
            lbl_Res["text"] = "¿?"
            messagebox.showinfo("ERROR", "FALTAN VALORES")
        else:
            Resultado = int(Num_1) * int(Num_2)
            lbl_Res["text"] = Resultado
   except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")
        
def Div():
   
   try:
        Num_1 = Ent_Val1.get()
        Num_2 = Ent_Val2.get()
    
        if Num_1 == "" or Num_2 == "":
            lbl_Res["text"] = "¿?"
            messagebox.showinfo("ERROR", "FALTAN VALORES")
        else:
            Resultado = int(Num_1) / int(Num_2)
            lbl_Res["text"] = Resultado
   except:
        messagebox.showerror("ERROR", "VALORES NO VALIDOS")

# --- Sub-Ventana 1 (Operaciones) ---

Operaciones = LabelFrame(Ventana, text="Operaciones", width=428, height=102, background="black", fg="white", font=("Verdana", 10))
Operaciones.place(x=10, y=20)

lbl_num1 = Label(Ventana, text="Numero 1", fg="white", bg="black", font=("Verdana", 10))
lbl_num1.place(x=30, y=40)

lbl_num2 = Label(Ventana, text="Numero 2",fg="white", bg="black", font=("Verdana", 10))
lbl_num2.place(x=190, y=40)

lbl_res = Label(Ventana, text="Resultado", fg="white", bg="black", font=("Verdana", 10))
lbl_res.place(x=340, y=40)

Ent_Val1 = Entry(Ventana, fg="black", font=("Verdana", 10), width=8, justify=RIGHT,)
Ent_Val1.place(x=30, y=70)
Ent_Val1.insert(0, "7")

lbl_signo = Label(Ventana, text="(+ - × ÷)", fg="white", bg="black", font=("Verdana", 10))
lbl_signo.place(x=110, y=70)

Ent_Val2 = Entry(Ventana, fg="black", font=("Verdana", 10), width=8, justify=RIGHT,)
Ent_Val2.place(x=190, y=70)
Ent_Val2.insert(0, "2")

lbl_igual = Label(Ventana, text="=", fg="white", bg="black", font=("Verdana", 10))
lbl_igual.place(x=290, y=70)

lbl_Res = Label(Ventana, text="", fg="black", bg="white", font=("Verdana", 10), width=8)
lbl_Res.place(x=340, y=70)

# --- Sub-Ventana 2 (Operadores Aritmeticos) ---

Oper_Ari = LabelFrame(Ventana, text="Operadores Aritmeticos", width=428, height=102, background="black", fg="white", font=("Verdana", 10))
Oper_Ari.place(x=10, y=160)

Btn_Suma = Button(Ventana, text="+", width=10, height=4, background="DodgerBlue3", fg="white", command=Sumar)
Btn_Suma.place(x=25, y=180)

Btn_Resta = Button(Ventana, text="-", width=10, height=4, background="DodgerBlue3", fg="white", command=Restar)
Btn_Resta.place(x=130, y=180)

Btn_Mul = Button(Ventana, text="×", width=10, height=4, background="DodgerBlue3", fg="white", command=Mul)
Btn_Mul.place(x=235, y=180)

Btn_Div = Button(Ventana, text="÷", width=10, height=4, background="DodgerBlue3", fg="white", command=Div)
Btn_Div.place(x=340, y=180)

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