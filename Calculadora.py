def mostrar_menu():
    print("\n" + "="*50)
    print("         PROGRAMA DE OPERACIONES MATEMÁTICAS")
    print("="*50)
    print("1. Suma de 'n' números (positivos y negativos)")
    print("2. Producto entre 'n' números")
    print("3. División entre 2 números")
    print("4. Calcular factorial (n!)")
    print("5. Tablas de multiplicar (del 1 al 10)")
    print("6. Calcular cuadrado y cubo de un número")
    print("7. Calcular promedio de una serie de números")
    print("8. Encontrar máximo y mínimo de 'n' números")
    print("9. Salir del programa")
    print("="*50)

def suma_n_numeros():
    print("\n--- SUMA DE 'N' NÚMEROS ---")
    try:
        n = int(input("¿Cuántos números desea sumar?: "))
        if n <= 0:
            print("Debe ingresar un número positivo mayor que cero.")
            return
        suma = 0
        for i in range(1, n + 1):
            numero = float(input(f"Ingrese el número {i}: "))
            suma += numero
        print(f"\nLa suma de los {n} números es: {suma}")
    except ValueError:
     print("Error: Debe ingresar un número válido.")
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-9): ")
        if opcion == '1':
            suma_n_numeros()
        elif opcion == '9':
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()