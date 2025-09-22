# Imports de las funciones de los otros archivos
from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

# Función del menú interactivo
def menu():
    while True:
        print("\n--- Calculadora Open Source ---")
        print("1. Sumar 2 números")
        print("2. Restar 2 números")
        print("3. Multiplicar 2 números")
        print("4. Dividir 2 números")
        print("5. Suma avanzada (N números)")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", sumar(a, b))

        elif opcion == "2":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", restar(a, b))

        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", multiplicar(a, b))

        elif opcion == "4":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", dividir(a, b))

        elif opcion == "5":
            numeros = input("Escribe los números separados por espacio: ")
            lista = [float(n) for n in numeros.split()]
            print("Resultado:", suma_avanzada(*lista))

        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

# Ejecutar el menú si se corre este archivo directamente
if __name__ == "__main__":
    menu()