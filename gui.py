import tkinter as tk
from tkinter import ttk
from lexer import Lexer
from token import Token


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
        self.text_area = tk.Text(self.input_frame, height=1, width=20)
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
