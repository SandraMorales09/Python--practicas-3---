def encontrar_mayor(lista):
    if not lista:
        return "La lista está vacía."
    return max(lista)

# Ejemplo de uso
numeros = [23, 89, 45, 12, 67]
print(f"El número mayor es: {encontrar_mayor(numeros)}")  # Resultado: 89