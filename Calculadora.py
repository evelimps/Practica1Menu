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
        suma = 0
        for i in range(1, n + 1):
            suma += float(input(f"Ingrese el número {i}: "))
        print(f"\nLa suma total es: {suma}")
    except ValueError: print("Error: Entrada inválida.")
def producto_n_numeros():
    print("\n--- PRODUCTO DE 'N' NÚMEROS ---")
    try:
        n = int(input("¿Cuántos números desea multiplicar?: "))
        producto = 1
        for i in range(1, n + 1):
            producto *= float(input(f"Ingrese el número {i}: "))
        print(f"\nEl resultado del producto es: {producto}")
    except ValueError: print("Error: Entrada inválida.")

def division():
    try:
        n1 = float(input("Ingrese el dividendo: "))
        n2 = float(input("Ingrese el divisor: "))
        if n2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print(f"Resultado: {n1 / n2}")
    except ValueError: print("Error: Entrada inválida.")
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-9): ")
        
        if opcion == '1': suma_n_numeros()
        elif opcion == '2': producto_n_numeros()
        elif opcion == '3': division()
        elif opcion == '4': calcular_factorial()
        elif opcion == '5': tablas_multiplicar()
        elif opcion == '6': cuadrado_cubo()
        elif opcion == '7': promedio_serie()
        elif opcion == '8': maximo_minimo()
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
def calcular_factorial():
    try:
        num = int(input("Ingrese un número entero para calcular su factorial: "))
        if num < 0:
            print("No existe el factorial de números negativos.")
        else:
            print(f"El factorial de {num}! es: {math.factorial(num)}")
    except ValueError: print("Error: Debe ser un número entero.")

def tablas_multiplicar():
    try:
        tabla = int(input("¿Qué tabla desea ver? (Seleccione el número): "))
        print(f"\n--- Tabla del {tabla} ---")
        for i in range(1, 11):
            print(f"{tabla} x {i} = {tabla * i}")
    except ValueError: print("Error: Ingrese un número válido.")
