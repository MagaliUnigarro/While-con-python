import math

# Función para calcular el factorial
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


while True:
    print("\nSeleccione la operación a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Factorial")
    print("7. Raíz cuadrada")
    print("8. Cambiar números")
    print("9. Salir")

    opcion = int(input("Ingrese su opción: "))

    # Suma
    if opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print("El resultado es:", resultado)

    # Resta
    elif opcion == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print("El resultado es:", resultado)

    # Multiplicación
    elif opcion == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print("El resultado es:", resultado)

    # División
    elif opcion == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número (distinto de cero): "))
        if num2 == 0:
            print("No se puede dividir por cero.")
        else:
            resultado = num1 / num2
            print("El resultado es:", resultado)

    # Potenciación
    elif opcion == 5:
        num1 = float(input("Ingrese la base: "))
        num2 = float(input("Ingrese el exponente: "))
        resultado = num1 ** num2
        print("El resultado es:", resultado)

    # Factorial
    elif opcion == 6:
        num = int(input("Ingrese un número entero positivo: "))
        resultado = factorial(num)
        print("El factorial de", num, "es:", resultado)

    # Raíz cuadrada
    elif opcion == 7:
        num = int(input("Ingrese un número entero positivo: "))
        resultado = math.sqrt(num)
        print("La raíz cuadrada de", num, "es:", resultado)

    # Cambiar número
    elif opcion == 8:
        continue

    # Salir
    elif opcion == 9:
        print("Chao!")
        break

    # Opción inválida
    else:
        print("Opción Errada, intente de nuevo.")
