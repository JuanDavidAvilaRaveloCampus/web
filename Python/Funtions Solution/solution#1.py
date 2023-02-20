# 1. Campus requiere administrar algunos datos de sus Campers
# como por ejemplo, la creación, eliminación o búsqueda de los
# developers, entre otros, por tal razón, ha solicitado el diseño de
# un programa que cuente con el siguiente menú como panel de
# control:

print(f'\n------------------------MENU------------------------\n1.   CREAR GRUPO ARTEMIS:\n1.1  LISTAR CAMPERS DE ARTEMIS\n1.2  AGREGAR CAMPERS A ARTEMIS\n1.3  ELIMINAR CAMPERS DE ARTERMIS\n1.4  ORDENAR ALFABÉTICAMENTE EN UNA LISTA DE ARTEMIS\n1.5  BUSCAR CAMPER EN LISTA DE ARTEMIS\n2    CREAR GRUPO SPUTNIK:\n2.1  LISTAR CAMPERS DE CAMPERS DE SPUTNIK:\n2.2  AGREGAR CAMPSER A SPUTNIK\n2.3  ELIMINAR CAMPERS DE SPUTNIK\n2.4  ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n2.5  BUSCAR CAMPER EN LISTA DE SPUTNIK')

crear_grupo = int(input('Dijite la opción: ')) 


proseguir = 0
listar = 0
agregar = 0
eliminar = 0
ordenar_alpha = 0
buscar = 0

grupo_artemis = []
grupo_sputnik = []





if crear_grupo == 1:
    print(f'\nSe ha creado el grupo Artemis..')
    print(f'Si deasea listar el grupo Artemis, presione 1.\nSi desea agregar campers, presione 2.\nSi desea eliminar un camper, presione 3.\nSi desea ordenarlos presione 4 y si desea buscar un camper presione 5')
    proseguir = int(input('Dijite su respuesta: '))

    #LISTAR


    #if proseguir == 1:
    #AGREGAR
    while proseguir == 2:

        nombreUsuario = input('\nAgregue el nombre del camper: ')
        grupo_artemis.append(nombreUsuario)

        print('\nSi desea agregar otro camper a la lista dijite 2.\nSi desea salir, dijite 0')
        proseguir = int(input(f'Dijite la opción: '))

    #ELIMINAR
    #ORDENAR
    #BUSCAR

    #ToDO DEBE ESTAR DENTRO DE UN WHILE,
    #PARA CUANDO QUERRAMOS PREGUNTAR SI QUIERE SALIR, 
    #QUE PRESIONE 0 Y SI QUIERE ELEJIR OTRA OPCIÓN,
    #QUE PRESIONE 1 Y SE REINICIE EL BUCLE

