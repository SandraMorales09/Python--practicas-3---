def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

# Ejemplo de uso
frase = "Este es un ejemplo de Python"
print(f"Cantidad de palabras: {contar_palabras(frase)}")  # Resultado: 6