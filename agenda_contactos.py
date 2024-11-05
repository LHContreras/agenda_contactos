


def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contactos")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor introduzca el teléfono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha agendado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Introduzca el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"¡Se ha eliminado el contacto {nombre} exitosamente!")
    else:
        print(f"No se ha encontrado el contacto {nombre} en la agenda.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que está buscando: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

def listar_contacto(agenda):
    if agenda:
        print("\nLista de contactos")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("-" * 10)
    else:
        print("La agenda está vacía")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción:")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos ¡Hasta luego!")
            break
        else:
            print("Por favor sellecione una opción válida")
            print("\n")

agenda_contactos()
