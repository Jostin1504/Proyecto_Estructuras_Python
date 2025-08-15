import tkinter as tk
inicio=tk.Tk()
inicio.title("Sistema de compra")
inicio.geometry("400x300")
label=tk.Label(inicio,text="Hola bienvenido",font=("Arial",15))
label.pack(pady=20)

def saludo():
    label.config(text="Que quiere comprar")

boton=tk.Button(inicio,text="Entrar",command=saludo)
boton.pack(pady=10)    


inicio.mainloop()