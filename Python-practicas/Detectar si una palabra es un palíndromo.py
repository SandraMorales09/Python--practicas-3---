def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# Ejemplo de uso
palabra = "anita lava la tina"
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")  # Resultado: 'anita lava la tina' es un palíndromo.
else:
    print(f"'{palabra}' no es un palíndromo.")