# miToken.py

class Token:
    def __init__(self, lexema, categoria, subcategoria, posicion):
        self.lexema = lexema
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.posicion = posicion

    def __repr__(self):
        return f"Token(lexema='{self.lexema}', categoria='{self.categoria}', subcategoria='{self.subcategoria}', posicion={self.posicion})"
