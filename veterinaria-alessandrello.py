import os
import platform
veterinaria_alessandrello = []

base_datos= [
        {'id': 1, 'nombre': 'Firulais', 'edad': 3, 'especie': 'Perro', 'raza': 'Labrador', 'sexo': 'M', 'atencion': 'Chequeo',  'dueño': 'Juan Pérez'},
        {'id': 2, 'nombre': 'Mishi', 'edad': 2, 'especie': 'Gato', 'raza': 'Siamés', 'sexo': 'H', 'atencion': 'Baño',  'dueño': 'María García'},
        {'id': 3, 'nombre': 'Loki', 'edad': 1, 'especie': 'Perro', 'raza': 'Husky', 'sexo': 'M', 'atencion': 'Internacion',  'dueño': 'Carlos López'},
        {'id': 4, 'nombre': 'Rex', 'edad': 5, 'especie': 'Perro', 'raza': 'Pastor Alemán', 'sexo': 'M', 'atencion': 'Cirugia', 'dueño': 'Ana Rodríguez'},
        {'id': 5, 'nombre': 'Nala', 'edad': 4, 'especie': 'Gato', 'raza': 'Persa', 'sexo': 'F', 'atencion': 'Chequeo', 'dueño': 'Pedro Sánchez'},
        {'id': 6, 'nombre': 'Bobby', 'edad': 2, 'especie': 'Perro', 'raza': 'Chihuahua', 'sexo': 'M', 'atencion': 'Baño', 'dueño': 'Laura Martínez'},
        {'id': 7, 'nombre': 'Luna', 'edad': 3, 'especie': 'Gato', 'raza': 'Angora', 'sexo':'F', 'atencion': 'Cirugia',  'dueño': 'David Torres'}
    ]

def limpiar_terminal():
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')

def agregar_base_datos():
    for mascota in base_datos:
        li = [mascota['id'], mascota['nombre'], mascota['edad'], mascota['especie'], mascota['raza'], mascota['sexo'], mascota['atencion'], mascota['dueño']]
        veterinaria_alessandrello.append(li)
    return veterinaria_alessandrello


def agregar_mascota():
    print("\n--- AGREGAR MASCOTA ---")
    id = int(input("Ingrese el codigo ID de la mascota: "))
    while id != 0:
        nombre = input("Ingrese el nombre de la mascota: ")
        edad = int(input("Ingrese la edad de la mascota: "))
        especie = input("Ingrese la especie de mascota: ")
        raza = input("Ingrese la raza de la mascota: ")
        sexo = input("Ingrese el sexo de la mascota (M/H): ")
        atencion = input("Ingrese el tipo de atencion (baño, cirugia, internacion, chequeo): ")
        dueño = input("Ingrese el nombre del dueño: ")
        li = [id, nombre, edad, especie, raza, sexo, atencion, dueño]
        veterinaria_alessandrello.append(li)
        id = int(input("Ingrese el codigo ID de la mascota (0 para terminar): "))
    return veterinaria_alessandrello

def listar_mascotas():
    print("\n" + "="*100)
    print("LISTA DE MASCOTAS - VETERINARIA ALESSANDRELLO")
    print("="*100)
    print(f"{'ID':<5} {'NOMBRE':<15} {'EDAD':<5} {'ESPECIE':<10} {'RAZA':<15} {'SEXO':<10} {'ATENCIÓN':<12} {'DUEÑO':<15}")
    print("-"*100)
    
    if not veterinaria_alessandrello:
        print("No hay mascotas registradas.")   
        return
    
    for mascota in veterinaria_alessandrello:
        sexo_str = 'Macho' if mascota[5] == 'M' else 'Hembra'
        print(f"{mascota[0]:<5} {mascota[1]:<15} {mascota[2]:<5} {mascota[3]:<10} {mascota[4]:<15} {sexo_str:<10} {mascota[6]:<12} {mascota[7]:<15}")


# Programa principal
limpiar_terminal()
agregar_base_datos()
print("Bienvenido a la veterinaria Alessandrello")
print("Base de datos cargada con exito.")

menu = """
****************************************************
1. Listar todas las mascotas
2. Agregar una nueva mascota
3. Mostrar historia clinica de una mascota
4. Mostrar los gatos que necesitan cirugia
5. Salir
***************************************************
"""

print(menu)
op = int(input("Opcion de menu: "))

while op != 5:
    if op == 1:
        listar_mascotas()  
    elif op == 2:
        agregar_mascota()
        print("Mascota(s) agregada(s) correctamente.")
    elif op == 3:
        codigo_buscar = int(input("Ingrese el codigo ID de la mascota a buscar: "))
        encontrado = False
        
        for mascota in veterinaria_alessandrello:
            if not encontrado and mascota[0] == codigo_buscar:
                print("\n--- HISTORIA CLÍNICA ---")
                print(f"ID: {mascota[0]}")
                print(f"Nombre: {mascota[1]}")
                print(f"Edad: {mascota[2]} años")
                print(f"Especie: {mascota[3]}")
                print(f"Raza: {mascota[4]}")
                print(f"Sexo: {'Macho' if mascota[5] == 'M' else 'Hembra'}")
                print(f"Atención: {mascota[6]}")
                print(f"Dueño: {mascota[7]}")
                encontrado = True
        if not encontrado:
            print("Mascota no encontrada.")

    elif op == 4:
        print("\n--- GATOS QUE NECESITAN CIRUGÍA ---")
        gatos_cirugia = []
        
        for mascota in veterinaria_alessandrello:
            if mascota[3].lower() == 'gato' and mascota[6].lower() == 'cirugia':
                gatos_cirugia.append(mascota)
        
        if gatos_cirugia:
            print(f"{'ID':<5} {'NOMBRE':<15} {'EDAD':<5} {'RAZA':<15} {'SEXO':<10} {'DUEÑO':<15}")
            print("-"*65)
            for gato in gatos_cirugia:
                sexo_str = 'Macho' if gato[5] == 'M' else 'Hembra'
                print(f"{gato[0]:<5} {gato[1]:<15} {gato[2]:<5} {gato[4]:<15} {sexo_str:<10} {gato[7]:<15}")
        else:
            print("No hay gatos que necesiten cirugía en este momento.")

    else:
        print("Opcion no valida.")
    
    print(menu)
    op = int(input("Opcion de menu:"))

print("¡Gracias por usar el sistema de la Veterinaria Alessandrello!")