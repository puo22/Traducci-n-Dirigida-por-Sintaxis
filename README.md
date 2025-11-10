# Traducción Dirigida por la Sintaxis (ETDS)  
**Proyecto académico — Procesadores de Lenguaje**

Este proyecto implementa un **Esquema de Traducción Dirigido por la Sintaxis (ETDS)** para una **Gramática Independiente del Contexto (GIC)** que soporta expresiones aritméticas con los operadores:  
**suma (`+`), resta (`-`), multiplicación (`*`) y división (`/`)**.

La especificación sigue **estrictamente** la metodología, notación y ejemplos presentados en la presentación **`08.pdf`** (*Traducción Dirigida por la Sintaxis – TDS/SDT*).

---

## 📌 Gramática Independiente del Contexto (GIC)

La GIC utilizada es la siguiente (pág. 27 del `08.pdf`):

```bash
E → E + T
E → E - T
E → T
T → T * F
T → T / F
T → F
F → ( E )
F → id
F → num
```

- **`E`**: expresión
- **`T`**: término
- **`F`**: factor
- **`id`**: identificador (ej. `a`, `x`)
- **`num`**: número (ej. `4`, `3.14`)

Esta gramática:
- Tiene **recursividad izquierda** para respetar la **asociatividad izquierda** de los operadores.
- Establece **dos niveles de precedencia**: `*` y `/` > `+` y `-`.
- Es la base de los ejemplos del PDF:  
  `a + 4 * b → suma(a, mul(4, b))` (**págs. 4 y 28**).

---

## 📌 Base teórica (según `08.pdf`)

- **Gramática con recursividad izquierda**: usada para respetar la asociatividad izquierda de los operadores (`+`, `-`, `*`, `/`), tal como se muestra en la **página 27** del PDF.
- **Notación de traducción**:  
  - `a + 4 * b` → `suma(a, mul(4, b))`  
  - Ejemplo tomado directamente de la **página 4 y página 28**.
- **Atributos sintetizados**: como `.trad`, `.lexema` (págs. 4, 28).
- **ETDS**: acciones semánticas insertadas en la parte derecha de las reglas, en el momento exacto en que los atributos están disponibles (**págs. 6, 20, 29**).
- **AST decorado**: se genera implícitamente mediante el ETDS; se imprime como resultado de la traducción (**pág. 28**).
- **Tabla de símbolos**: mencionada en el contexto de definiciones dirigidas por la sintaxis (DDS), aunque **no se usa en expresiones puras** (**págs. 15–16, 18–20**).

---

## Archivos entregados

Cada archivo corresponde a un ítem del enunciado de la tarea:

1. **`Diseño_Gramatica.txt`**  
   Gramática con recursividad izquierda (pág. 27).

2. **`Definir_atributos.txt`**  
   Definición de atributos sintetizados (págs. 4, 28).

3. **`conjuntos.txt`**  
   Cálculo de conjuntos **First**, **Follow** y **Producciones**.

4. **`AST.txt`**  
   AST decorado impreso para la entrada `a + b * c` (pág. 28).

5. **`TablaSimbolos.txt`**  
   Estructura de la tabla de símbolos (pág. 15); se aclara que no se llena en expresiones puras.

6. **`GramaticaAtributos.txt`**  
   Gramática de atributos en formato DDS (pág. 4).

7. **`Generar_ETDS.txt`**  
   ETDS final con acciones semánticas en el lugar correcto (págs. 28–29).

---

---

## 🎓 Autor
- **Nombre**: Paula Ortiz Salon 
- **Curso**: Procesadores de Lenguaje  
- **Fecha**: Noviembre 2025
