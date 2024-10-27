import random

num1 = random.randint(2, 10)
num2 = random.randint(2, 10)
resultado_correcto = num1 * num2

respuesta = int(input(f"¿Cuánto es {num1} * {num2}? "))
if respuesta == resultado_correcto:
    print("¡Correcto!")
else:
    print(f"Incorrecto. La respuesta correcta es {resultado_correcto}.")
