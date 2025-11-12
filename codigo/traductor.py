#!/usr/bin/env python3
# traductor.py — Implementación del ETDS para expresiones aritméticas
# Basado en el PDF "08.pdf", páginas 27–31

import sys

# --- Tabla de Símbolos ---
class TablaSimbolos:
    def __init__(self):
        self.tabla = {}
        self.offset = 0

    def agregar(self, nombre):
        if nombre not in self.tabla:
            self.tabla[nombre] = {"tipo": "desconocido", "direccion": self.offset}
            self.offset += 4  # 4 bytes por variable

    def imprimir(self):
        print("=== TABLA DE SÍMBOLOS ===")
        if not self.tabla:
            print("(No hay identificadores)")
        else:
            print(f"{'Nombre':<10} {'Tipo':<12} {'Dirección':<10}")
            print("-" * 35)
            for nombre, info in self.tabla.items():
                print(f"{nombre:<10} {info['tipo']:<12} {info['direccion']:<10}")
        print()

# --- Nodo del AST (mejorado para impresión clara) ---
class NodoAST:
    def __init__(self, etiqueta, hijos=None):
        self.etiqueta = etiqueta
        self.hijos = hijos or []

    def imprimir(self, prefijo="", es_ultimo=True):
        print(prefijo + ("└── " if es_ultimo else "├── ") + self.etiqueta)
        if self.hijos:
            for i, hijo in enumerate(self.hijos):
                es_ultimo_hijo = (i == len(self.hijos) - 1)
                nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
                hijo.imprimir(nuevo_prefijo, es_ultimo_hijo)
# --- Variables globales del analizador ---
tokens = []
pos = 0
lexema = ""
token = ""
tabla_simbolos = TablaSimbolos()

# --- Analizador léxico ---
def siguiente_token():
    global pos, lexema
    if pos < len(tokens):
        t = tokens[pos]
        if t in ['+', '-', '*', '/', '(', ')']:
            lexema = t
            pos += 1
            return t
        elif t.replace('.', '', 1).isdigit():
            lexema = t
            pos += 1
            return 'num'
        else:
            lexema = t
            pos += 1
            return 'id'
    return '$'

def emparejar(expected):
    global token
    if token == expected:
        token = siguiente_token()
    else:
        raise SyntaxError(f"Error: se esperaba '{expected}'")

# --- Reglas del analizador (gramática transformada del PDF, pág. 29) ---
def E():
    nodo_t = T()
    return E_prima(nodo_t)

def E_prima(nodo_izq):
    global token
    if token == '+':
        emparejar('+')
        nodo_der = T()
        nodo_op = NodoAST('suma', [nodo_izq, nodo_der])
        return E_prima(nodo_op)
    elif token == '-':
        emparejar('-')
        nodo_der = T()
        nodo_op = NodoAST('res', [nodo_izq, nodo_der])
        return E_prima(nodo_op)
    else:
        return nodo_izq  # ε

def T():
    nodo_f = F()
    return T_prima(nodo_f)

def T_prima(nodo_izq):
    global token
    if token == '*':
        emparejar('*')
        nodo_der = F()
        nodo_op = NodoAST('mul', [nodo_izq, nodo_der])
        return T_prima(nodo_op)
    elif token == '/':
        emparejar('/')
        nodo_der = F()
        nodo_op = NodoAST('div', [nodo_izq, nodo_der])
        return T_prima(nodo_op)
    else:
        return nodo_izq  # ε

def F():
    global token, lexema
    if token == '(':
        emparejar('(')
        nodo = E()
        emparejar(')')
        return nodo
    elif token == 'id':
        nombre = lexema
        tabla_simbolos.agregar(nombre)
        emparejar('id')
        return NodoAST(nombre)
    elif token == 'num':
        valor = lexema
        emparejar('num')
        return NodoAST(valor)
    else:
        raise SyntaxError("Error en F: se esperaba '(', id o num")

# --- Función principal ---
def main():
    expr = sys.argv[1] if len(sys.argv) > 1 else "a + b * c"
    print(f"Entrada: {expr}\n")

    global tokens, pos, token
    expr = expr.replace('(', ' ( ').replace(')', ' ) ')
    tokens = expr.split()
    pos = 0
    token = siguiente_token()

    try:
        ast = E()
        if token != '$':
            raise SyntaxError("Símbolos extra al final")

        print("=== AST DECORADO ===")
        ast.imprimir()
        print()

        tabla_simbolos.imprimir()

    except Exception as e:
        print(f"Error: {e}")


main()
