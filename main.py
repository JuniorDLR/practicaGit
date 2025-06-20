def mostrar_menu():
    print("=== Menú Principal ===")
    print("1. Saludar")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("Hola")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")