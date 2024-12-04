from os import system as sy
import time
sy('cls')

import tkinter as tk
from tkinter import messagebox

def dividir_conta():
    try:
        num_clientes = int(entry_num_clientes.get())
        valor_conta = float(entry_valor_conta.get())
        
        if num_clientes > 0:
            valor_por_cliente = valor_conta / num_clientes
            resultado = f'Cada cliente deve pagar: R$ {valor_por_cliente:.2f}'
            messagebox.showinfo("Resultado", resultado)
        else:
            messagebox.showwarning("Atenção", "Por favor, insira um número válido de clientes.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

root = tk.Tk()
root.title("Dividir Conta")

label_num_clientes = tk.Label(root, text="Número de Clientes:")
label_num_clientes.pack()

entry_num_clientes = tk.Entry(root)
entry_num_clientes.pack()

label_valor_conta = tk.Label(root, text="Valor Total da Conta (R$):")
label_valor_conta.pack()

entry_valor_conta = tk.Entry(root)
entry_valor_conta.pack()

button_calcular = tk.Button(root, text="Calcular", command=dividir_conta)
button_calcular.pack()

root.mainloop()