# lexer.py

from token import Token


class Lexer:
    def __init__(self):
        self.tokens = []

    def analizar(self, codigo):
        self.tokens = []
        posicion = 0
        longitud = len(codigo)

        while posicion < longitud:
            char = codigo[posicion]

            # Operadores aritméticos
            if codigo[posicion:posicion + 3] == 'add':
                self.tokens.append(Token('add', 'Operador', 'Aritmético', posicion))
                posicion += 3
            elif char == '~':
                self.tokens.append(Token('~', 'Operador', 'Aritmético', posicion))
                posicion += 1
            elif char == '°':
                self.tokens.append(Token('°', 'Operador', 'Aritmético', posicion))
                posicion += 1
            elif char == ':':
                self.tokens.append(Token(':', 'Operador', 'Aritmético', posicion))
                posicion += 1
            elif char == '^':
                self.tokens.append(Token('^', 'Operador', 'Aritmético', posicion))
                posicion += 1
            elif char == '|':
                self.tokens.append(Token('|', 'Operador', 'Aritmético', posicion))
                posicion += 1
            # Operadores relacionales
            elif codigo[posicion:posicion + 2] == '/=':
                self.tokens.append(Token('/=', 'Operador', 'Relacional', posicion))
                posicion += 2
            elif codigo[posicion:posicion + 2] == 'm>':
                self.tokens.append(Token('m>', 'Operador', 'Relacional', posicion))
                posicion += 2
            elif codigo[posicion:posicion + 2] == 'i>':
                self.tokens.append(Token('i>', 'Operador', 'Relacional', posicion))
                posicion += 2
            elif codigo[posicion:posicion + 2] == 'm<':
                self.tokens.append(Token('m<', 'Operador', 'Relacional', posicion))
                posicion += 2
            elif codigo[posicion:posicion + 2] == 'i<':
                self.tokens.append(Token('i<', 'Operador', 'Relacional', posicion))
                posicion += 2
            # Operadores lógicos
            elif codigo[posicion:posicion + 2] == '^^':
                self.tokens.append(Token('^^', 'Operador', 'Lógico', posicion))
                posicion += 2
            elif codigo[posicion:posicion + 2] == 'vv':
                self.tokens.append(Token('vv', 'Operador', 'Lógico', posicion))
                posicion += 2
            elif char == '¬':
                self.tokens.append(Token('¬', 'Operador', 'Lógico', posicion))
                posicion += 1
            # Operadores de asignación
            elif codigo[posicion:posicion + 2] == '->':
                self.tokens.append(Token('->', 'Operador', 'Asignación', posicion))
                posicion += 2
            # Símbolos de abrir
            elif char == '<':
                self.tokens.append(Token('<', 'Símbolo', 'Abrir', posicion))
                posicion += 1
            elif char == '#':
                self.tokens.append(Token('#', 'Símbolo', 'Abrir', posicion))
                posicion += 1
            # Símbolos de cerrar
            elif char == '>':
                self.tokens.append(Token('>', 'Símbolo', 'Cerrar', posicion))
                posicion += 1
            elif char == '%':
                self.tokens.append(Token('%', 'Símbolo', 'Cerrar', posicion))
                posicion += 1
            # Terminal y/o inicial
            elif char == '¨':
                self.tokens.append(Token('¨', 'Símbolo', 'Terminal/Inicial', posicion))
                posicion += 1
            elif char == "'":
                self.tokens.append(Token("'", 'Símbolo', 'Terminal/Inicial', posicion))
                posicion += 1
            # Separadores de sentencias
            elif char == '_':
                self.tokens.append(Token('_', 'Separador', 'Sentencia', posicion))
                posicion += 1
            # Palabras reservadas para bucles y ciclos
            elif codigo[posicion:posicion + 2] == 'go':
                if posicion + 3 <= longitud and codigo[posicion + 2] == '!':
                    self.tokens.append(Token('go!', 'Palabra Reservada', 'Bucle', posicion))
                    posicion += 3
                else:
                    self.tokens.append(Token('go', 'Palabra Reservada', 'Bucle', posicion))
                    posicion += 2
            # Palabras reservadas para decisiones
            elif codigo[posicion:posicion + 2] == 'if':
                if posicion + 5 <= longitud and codigo[posicion + 2:posicion + 5] == ')$¡':
                    self.tokens.append(Token('if)$¡', 'Palabra Reservada', 'Decisión', posicion))
                    posicion += 5
                else:
                    self.tokens.append(Token('if', 'Palabra Reservada', 'Decisión', posicion))
                    posicion += 2
            elif codigo[posicion:posicion + 7] == '(elseif)':
                if posicion + 7 <= longitud and codigo[posicion + 7] == '$¡!':
                    self.tokens.append(Token('(elseif)$¡!', 'Palabra Reservada', 'Decisión', posicion))
                    posicion += 7
                else:
                    self.tokens.append(Token('(elseif)', 'Palabra Reservada', 'Decisión', posicion))
                    posicion += 7
            elif codigo[posicion:posicion + 4] == 'else':
                self.tokens.append(Token('else', 'Palabra Reservada', 'Decisión', posicion))
                posicion += 4
            # Palabras reservadas para clases
            elif codigo[posicion:posicion + 4] == 'tipe':
                self.tokens.append(Token('tipe', 'Palabra Reservada', 'Clase', posicion))
                posicion += 4
            elif codigo[posicion:posicion + 5] == 'iface':
                self.tokens.append(Token('iface', 'Palabra Reservada', 'Clase', posicion))
                posicion += 5
            # Identificadores
            elif codigo[posicion:posicion + 5] == 'gauss':
                self.tokens.append(Token('gauss', 'Identificador', 'Variable', posicion))
                posicion += 5
            elif codigo[posicion:posicion + 5] == 'gamma':
                self.tokens.append(Token('gamma', 'Identificador', 'Método', posicion))
                posicion += 5
            elif codigo[posicion:posicion + 3] == 'chi':
                self.tokens.append(Token('chi', 'Identificador', 'Clase', posicion))
                posicion += 3
            # Valores de asignación
            elif char.isdigit():
                numero = ''
                while posicion < longitud and codigo[posicion].isdigit():
                    numero += codigo[posicion]
                    posicion += 1
                self.tokens.append(Token(numero, 'Valor', 'Entero', posicion - len(numero)))
            # Agrega aquí más lógica para otros tokens, como reales, cadenas, caracteres, etc.
            else:
                # Token no reconocido
                self.tokens.append(Token(char, 'Error', 'Token no reconocido', posicion))
                posicion += 1

        return self.tokens