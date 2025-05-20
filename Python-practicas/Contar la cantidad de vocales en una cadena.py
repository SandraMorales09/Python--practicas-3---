def contar_vocales(cadena):
    vocales = "aeiou"
    contador = 0
    for letra in cadena.lower():
        if letra in vocales:
            contador += 1
    return contador

# Ejemplo de uso
cadena = "Hola Mundo"
print(f"Número de vocales: {contar_vocales(cadena)}")  # Resultado: 4