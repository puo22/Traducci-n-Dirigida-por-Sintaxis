#!/usr/bin/env python3
import subprocess
import sys

casos = [
    "a + b * c",
    "a - b / c",
    "(a + b) * c",
    "x * y + z - w",
    "5",
    "valor",
    "a * (b + c) / d",
    "a + b + c",
    "a * b * c"
]

print("🧪 EJECUTANDO PRUEBAS AUTOMÁTICAS\n")
print("=" * 60)

for expr in casos:
    print(f"\n🧪 PRUEBA: {expr}")
    print("-" * 40)
    try:
        resultado = subprocess.run(
            [sys.executable, "traductor.py", expr],
            capture_output=True,
            text=True,
            timeout=5
        )
        if resultado.returncode == 0:
            print(resultado.stdout)
        else:
            print("❌ ERROR:", resultado.stderr)
    except Exception as e:
        print(f"💥 FALLO DE EJECUCIÓN: {e}")
    print("=" * 60)
