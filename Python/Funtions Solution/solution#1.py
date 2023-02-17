# 1. Campus requiere administrar algunos datos de sus Campers
# como por ejemplo, la creación, eliminación o búsqueda de los
# developers, entre otros, por tal razón, ha solicitado el diseño de
# un programa que cuente con el siguiente menú como panel de
# control:

menuPrincipal = int(input("Menu: \n 1. CREAR GRUPO ARTEMIS:\n 2. CREAR GRUPO SPUTNIK:\n"))
crearGrupoArtemis =  int(input(f"\n 1.1 LISTAR CAMPERS DE ARTEMIS\n 1.2 AGREGAR CAMPERS A ARTEMIS \n 1.3 ELIMINAR CAMPERRS DE ARTEMIS \n 1.4 ORDENAR ALFABÉTICAMENTE EN LISTA DE ARTEMIS \n 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS\n"))

while menuPrincipal != 0:
    if menuPrincipal == 1:
        print(f"\n 1.1 LISTAR CAMPERS DE ARTEMIS\n 1.2 AGREGAR CAMPERS A ARTEMIS \n 1.3 ELIMINAR CAMPERRS DE ARTEMIS \n 1.4 ORDENAR ALFABÉTICAMENTE EN LISTA DE ARTEMIS \n 1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS\n")
        if crearGrupoArtemis == 1:
            print(f"LISTADO CAMPERS ARTEMIS\n")
        if crearGrupoArtemis == 2:
            print(f"AGREGAR CAMPER AL GRUPO ARTEMIS\n")
        if crearGrupoArtemis == 3:
            print(f"ELIMINAR CAMPER ARTEMIS\n")
        if crearGrupoArtemis == 4:
            print(f"ORDENAR ALFABÉTICAMENTE EN LISTA ARTEMIS\n")
        if crearGrupoArtemis == 5:
            print(f"BUSCAR EN CAMPERS ARTEMIS\n")
    elif menuPrincipal == 2:
        print(f"\n 2.1 LISTAR CAMPERS SPUTNIK \n 2.2 AGREGAR CAMPERS A SPUTNIK \n 2.3 ELIMINAR CAMPERS SPUTNIK \n 2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK \n 2.5 BUSCAR CAMPER EN LA LISTA DE SPUTNIK\n")
        if crearGrupoArtemis == 1:
            print(f"LISTADO CAMPERS SPUTNIK\n")
        if crearGrupoArtemis == 2:
            print(f"AGREGAR CAMPER AL GRUPO SPUTNIK\n")
        if crearGrupoArtemis == 3:
            print(f"ELIMINAR CAMPER SPUTNIK\n")
        if crearGrupoArtemis == 4:
            print(f"ORDENAR ALFABÉTICAMENTE EN LISTA SPUTNIK\n")
        if crearGrupoArtemis == 5:
            print(f"BUSCAR EN CAMPERS SPUTNIK\n")
    else:
        print(f"Por favor digita un numero disponible")
    menuPrincipal = int(input("Menu: \n 1. CREAR GRUPO ARTEMIS:\n 2. CREAR GRUPO SPUTNIK:\n"))        