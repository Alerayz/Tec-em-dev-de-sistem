from os import system as sy
import time
sy('cls')

import tkinter as tk
from tkinter import messagebox

produtos = [
    {"nome": "Pastel", "preco": 8.00},
    {"nome": "Caldo de cana", "preco": 8.00},
    {"nome": "Suco Caixinha", "preco": 2.50},
    {"nome": "Salgados Diversos", "preco": 3.00},
    {"nome": "Coca-Cola", "preco": 3.50},
]

class Loja:
    def __init__(self, root):
        self.root = root
        self.root.title("Lojinha Virtual")
        
        self.carrinho = []
        self.total = 0.0

        self.criar_interface()

    def criar_interface(self):
        tk.Label(self.root, text="Catálogo de Produtos", font=("Arial", 16)).pack(pady=10)

        for produto in produtos:
            frame_produto = tk.Frame(self.root)
            frame_produto.pack(pady=5)

            tk.Label(frame_produto, text=produto["nome"]).pack(side=tk.LEFT, padx=5)
            tk.Label(frame_produto, text=f"R$ {produto['preco']:.2f}").pack(side=tk.LEFT, padx=5)
            tk.Button(frame_produto, text="Adicionar ao Carrinho", command=lambda p=produto: self.adicionar_ao_carrinho(p)).pack(side=tk.LEFT, padx=5)

        tk.Label(self.root, text="Carrinho", font=("Arial", 16)).pack(pady=10)
        self.lista_carrinho = tk.Listbox(self.root, width=50)
        self.lista_carrinho.pack(pady=5)

        self.label_total = tk.Label(self.root, text="Total: R$ 0.00", font=("Arial", 14))
        self.label_total.pack(pady=5)

        tk.Button(self.root, text="Finalizar Compra", command=self.finalizar_compra).pack(pady=10)

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.append(produto)
        self.total += produto["preco"]
        self.atualizar_carrinho()

    def atualizar_carrinho(self):
        self.lista_carrinho.delete(0, tk.END)  # Limpa a lista
        for item in self.carrinho:
            self.lista_carrinho.insert(tk.END, f"{item['nome']} - R$ {item['preco']:.2f}")
        self.label_total.config(text=f"Total: R$ {self.total:.2f}")

    def finalizar_compra(self):
        if self.carrinho:
            messagebox.showinfo("Compra Finalizada", f"Total: R$ {self.total:.2f}")
            self.carrinho.clear()
            self.total = 0.0
            self.atualizar_carrinho()
        else:
            messagebox.showwarning("Carrinho Vazio", "Adicione produtos ao carrinho antes de finalizar a compra.")

if __name__ == "__main__":
    root = tk.Tk()
    loja = Loja(root)
    root.mainloop()