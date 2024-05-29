import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from lexer import Lexer
from miToken import Token
import graphviz
import os
import re

class LexerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")

        # Frame para contener el Label y el Text
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=20)

        # Label para el campo de texto
        self.label = tk.Label(self.input_frame, text="Expresión Regular:")
        self.label.grid(row=0, column=0, padx=5)

        # Área de texto
        self.text_area = tk.Text(self.input_frame, height=10, width=30)
        self.text_area.grid(row=0, column=1, padx=5)

        # Tabla para mostrar los tokens
        self.tree = ttk.Treeview(root, columns=("Lexema", "Categoría", "Subcategoría", "Posición"), show="headings")
        self.tree.heading("Lexema", text="Lexema")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Subcategoría", text="Subcategoría")
        self.tree.heading("Posición", text="Posición")
        self.tree.pack()

        # Botón para realizar el análisis léxico
        self.analyze_button = tk.Button(root, text="Analizar", command=self.analizar_codigo)
        self.analyze_button.pack(pady=10)

        # Botón para mostrar el autómata
        self.automata_button = tk.Button(root, text="Autómata", command=self.mostrar_automata)
        self.automata_button.pack(pady=10)

        self.lexer = Lexer()

    def analizar_codigo(self):
        codigo = self.text_area.get("1.0", tk.END).strip()
        tokens = self.lexer.analizar(codigo)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for token in tokens:
            self.tree.insert("", tk.END, values=(token.lexema, token.categoria, token.subcategoria, token.posicion))

    def mostrar_automata(self):
        selected_item = self.tree.selection()
        if selected_item:
            token = self.tree.item(selected_item)['values']
            ventana = tk.Toplevel(self.root)
            ventana.title("Autómata para el Token")

            label = tk.Label(ventana, text=f"Autómata para el token: {token[0]}")
            label.pack(pady=20)

            # Generar el gráfico del autómata usando graphviz
            dot = graphviz.Digraph(comment=f'Autómata para {token[0]}')
            dot.node('A', 'Inicio')
            dot.node('B', 'Estado B')
            dot.node('C', 'Estado C')
            dot.edges(['AB', 'BC'])
            dot.node('D', 'Final')
            dot.edge('C', 'D', label='Transición')
            # Limpiar el nombre del token y eliminar cualquier carácter no deseado al final
            cleaned_token_name = re.sub(r'[^\w]', '_', token[0].strip())
            filename = f'automata_{cleaned_token_name}.png'
            dot.render(filename, format='png', cleanup=True)

            # Mostrar la imagen en la ventana de Tkinter
            image = PhotoImage(file=filename)
            image_label = tk.Label(ventana, image=image)
            image_label.image = image  # Mantener una referencia para evitar que la imagen sea recolectada por el garbage collector
            image_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = LexerGUI(root)
    root.mainloop()