import tkinter as tk
from tkinter import ttk
from lexer import Lexer
from token import Token


class LexerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico - MyFirst")

        # Área de texto
        self.text_area = tk.Text(root, height=20, width=80)
        self.text_area.pack(pady=20)

        # Botón para realizar el análisis léxico
        self.analyze_button = tk.Button(root, text="Analizar", command=self.analizar_codigo)
        self.analyze_button.pack(pady=10)

        # Tabla para mostrar los tokens
        self.tree = ttk.Treeview(root, columns=("Lexema", "Categoría", "Subcategoría", "Posición"), show="headings")
        self.tree.heading("Lexema", text="Lexema")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Subcategoría", text="Subcategoría")
        self.tree.heading("Posición", text="Posición")
        self.tree.pack()

        self.lexer = Lexer()

    def analizar_codigo(self):
        codigo = self.text_area.get("1.0", tk.END).strip()
        tokens = self.lexer.analizar(codigo)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for token in tokens:
            self.tree.insert("", tk.END, values=(token.lexema, token.categoria, token.subcategoria, token.posicion))


if __name__ == "__main__":
    root = tk.Tk()
    app = LexerGUI(root)
    root.mainloop()