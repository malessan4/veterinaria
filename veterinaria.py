veterinaria_lazaro = []  

def agregar_mascota():
    id = int(input("Ingrese el codigo ID de la mascota: "))
    while id != 0:
        nombre = input("Ingrese el nombre de la mascota: ")
        edad = int(input("Ingrese la edad de la mascota: "))
        tipo = input("Ingrese el tipo de mascota: ")
        raza = input("Ingrese la raza de la mascota: ")
        sexo = input("Ingrese el sexo de la mascota (M/H): ")
        atencion = input("Ingrese el tipo de atencion (baño, cirugia, internacion, chequeo): ")
        li = [id, nombre, edad, tipo, raza, sexo, atencion]
        veterinaria_lazaro.append(li)
        id = int(input("Ingrese el codigo ID de la mascota (0 para terminar): "))
    return veterinaria_lazaro 

# Programa principal
        

menu = """
****************************************************
1. Listar todas las mascotas
2. Agregar una nueva mascota
3. Mostar historia clinica de una mascota
4. Salir

***************************************************
"""
print(menu)
op = int(input("Opcion de menu: "))

while op != 4:
    if op == 1:
        print(veterinaria_lazaro)  
    elif op == 2:
        nueva_mascota = agregar_mascota()
        veterinaria_lazaro.append(nueva_mascota)  
    elif op == 3:
        codigo_buscar = int(input("Ingrese el codigo ID de la mascota a buscar: "))
        for mascota in veterinaria_lazaro:
            if mascota[0] == codigo_buscar:
                print("Historia clinica de la mascota:", mascota)
                break
        else:
            print("Mascota no encontrada.")
    else:
        print("Opcion no valida.")
    
    print(menu)
    op = int(input("Opcion de menu:"))