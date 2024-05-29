from miToken import Token

class Lexer:
    def __init__(self):
        self.tokens = []

    def analizar(self, codigo):
        self.tokens = []
        posicion = 0
        longitud = len(codigo)

        while posicion < longitud:
            char = codigo[posicion]

            # Omitir espacios y saltos de línea
            if char.isspace():
                posicion += 1
                continue

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
            elif char in ['<', '#']:
                self.tokens.append(Token(char, 'Símbolo', 'Abrir', posicion))
                posicion += 1
                inicio = posicion
                # Identificar cadenas sin cerrar
                while posicion < longitud and codigo[posicion] not in ['>', '%']:
                    posicion += 1
                if posicion == longitud:
                    self.tokens.append(Token(codigo[inicio - 1:posicion], 'Error', 'Cadena sin cerrar', inicio - 1))
                    break
                # Llamar a la función analizar_contenido para procesar el contenido entre <>
                contenido_tokens, pos = self.analizar_contenido(codigo, inicio)
                self.tokens.extend(contenido_tokens)
                posicion = pos
            # Símbolos de cerrar
            elif char in ['>', '%']:
                self.tokens.append(Token(char, 'Símbolo', 'Cerrar', posicion))
                posicion += 1
            # Terminal y/o inicial
            elif char in ['¨', "'"]:
                self.tokens.append(Token(char, 'Símbolo', 'Terminal/Inicial', posicion))
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
            elif codigo[posicion:posicion + 2] == '$¡':
                if posicion + 3 <= longitud and codigo[posicion:posicion + 4] == '$¡!':
                    self.tokens.append(Token('$¡!', 'Palabra Reservada', 'Decisión', posicion))
                    posicion += 4
                elif posicion + 2 <= longitud and codigo[posicion:posicion + 3] == '$¡':
                    self.tokens.append(Token('$¡', 'Palabra Reservada', 'Decisión', posicion))
                    posicion += 3
                elif posicion + 1 <= longitud and codigo[posicion:posicion + 2] == '$!':
                    self.tokens.append(Token('$!', 'Palabra Reservada', 'Decisión', posicion))
                    posicion += 2
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
            # Valores de asignación - Caracteres
            elif char.isalpha():
                self.tokens.append(Token(char, 'Valor', 'Caracter', posicion))
                posicion += 1
            # Números enteros y decimales
            elif char.isdigit() or char == '.':
                start = posicion
                has_decimal = False
                while posicion < longitud:
                    if codigo[posicion] == '.':
                        if has_decimal:
                            break
                        has_decimal = True
                    elif not codigo[posicion].isdigit():
                        break
                    posicion += 1
                if has_decimal:
                    self.tokens.append(Token(codigo[start:posicion], 'Valor', 'Decimal', start))
                else:
                    self.tokens.append(Token(codigo[start:posicion], 'Valor', 'Entero', start))
            elif char == '<':
                cadena = ''
                posicion += 1
                inicio = posicion
                if posicion < longitud and codigo[posicion] == '<':
                    while posicion < longitud and codigo[posicion] != '>':
                        cadena += codigo[posicion]
                        posicion += 1
                    if posicion < longitud and codigo[posicion] == '>':
                        posicion += 1
                        self.tokens.append(Token(cadena, 'Valor', 'Cadena', inicio - 1))
                    else:
                        self.tokens.append(Token(cadena, 'Error', 'Cadena sin cerrar', inicio - 1))
                        break
                else:
                    self.tokens.append(Token('<', 'Símbolo', 'Abrir', posicion - 1))
                    break
            elif char == '#':
                cadena = ''
                posicion += 1
                inicio = posicion
                if posicion < longitud and codigo[posicion] == '#':
                    while posicion < longitud and codigo[posicion] != '%':
                        cadena += codigo[posicion]
                        posicion += 1
                    if posicion < longitud and codigo[posicion] == '%':
                        posicion += 1
                        self.tokens.append(Token(cadena, 'Valor', 'Cadena', inicio - 1))
                    else:
                        self.tokens.append(Token(cadena, 'Error', 'Cadena sin cerrar', inicio - 1))
                        break
                else:
                    self.tokens.append(Token('#', 'Símbolo', 'Abrir', posicion - 1))
                    break
            elif codigo[posicion] == '<' and codigo[posicion + 1] == 'd':
                self.tokens.append(Token('<', 'Símbolo', 'Abrir', posicion))
                posicion += 1
                for letra in 'abcdefghijklmnopqrstuvwxyz':
                    if posicion + 1 < longitud and codigo[posicion + 1] == letra:
                        self.tokens.append(Token(letra, 'Caracter', 'Especifico', posicion + 1))
                        posicion += 1
                for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if posicion + 1 < longitud and codigo[posicion + 1] == letra:
                        self.tokens.append(Token(letra, 'Caracter', 'Especifico', posicion + 1))
                        posicion += 1
                if posicion + 1 < longitud and codigo[posicion + 1] == 'w':
                    self.tokens.append(Token('w', 'Caracter', 'Especifico', posicion + 1))
                    posicion += 1
                self.tokens.append(Token('>', 'Símbolo', 'Cerrar', posicion + 1))
                posicion += 1
            else:
                self.tokens.append(Token(char, 'Error', 'Token no reconocido', posicion))
                posicion += 1

        return self.tokens

    def analizar_contenido(self, codigo, posicion):
        tokens = []
        longitud = len(codigo)
        while posicion < longitud:
            char = codigo[posicion]
            if char == '>':
                return tokens, posicion
            elif char.isdigit():
                start = posicion
                while posicion < longitud and codigo[posicion].isdigit():
                    posicion += 1
                lexema = codigo[start:posicion]
                tokens.append(Token(lexema, 'Valor', 'Entero', start))
            elif char.isalpha():
                start = posicion
                while posicion < longitud and (codigo[posicion].isalnum() or codigo[posicion] == '_'):
                    posicion += 1
                lexema = codigo[start:posicion]
                tokens.append(Token(lexema, 'Identificador', 'Variable', start))
            elif char.isspace():
                posicion += 1
            else:
                tokens.append(Token(char, 'Error', 'Caracter no reconocido', posicion))
                posicion += 1
        tokens.append(Token('', 'Error', 'Agrupación sin cerrar', posicion))
        return tokens, posicion