def calcular_factorial(numero):
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo."
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es: {calcular_factorial(numero)}")  # Resultado: 120