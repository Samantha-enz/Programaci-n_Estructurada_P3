def borrarPantalla():
    print("\033c")

def esperarTecla():
    input("... ¡Oprima cualquier tecla para continuar! ...")

def terminar():
    input(".... :::: !GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n vuelva pronto! ::::.... ")

def opcionInvalida():
    input("\n\t .... ¡Opcion invalidad oprima cualquier tecla para continuar !....")

def accionExitosa():
    input("\n\t...¡Accion Realizada con Exito!...")

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR PELICULAS :::... \n")
    peli=input("Escribir el nombre de la pelicula: ").upper().strip()
    pelis.append(peli)
    accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR PELICULAS :::... \n")
    if len(pelis)>0:
        print("\n\t\tCodigo\t\tPelicula\n")
        for i in range(0,len(pelis)):
          print(f"{i+1}\t\t{pelis[i]}")
    else:
        print("... ¡No hay peliculas que Mostrar, verifique! ... ")
    esperarTecla()

def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS PELICULAS :::... \n")
    opc=input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
    while opc!="si" and opc!="no":
        opc=input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
    if opc=="si":
        pelis=pelis.clear()
        accionExitosa()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR PELICULAS :::...")
    peli=input("Escribe la pelicula a buscar: ").upper().strip()
    if peli in pelis:
        if peli==pelis[i]:
            print("\n\t\tCodigo\t\tPelicula\n")
            for i in range(0,len(pelis)):
                print(f"{i+1}\t\t{pelis[i]}")
    else:
            input("\n\t\t... ¡No existe la pelicula a buscar, verifique! ...")


def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR PELICULA :::...")
    peli=input("Escribe la pelicula a borrar: ").upper().strip()
    if peli in pelis:

            opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)? ").lower().strip()
            while opc!="si" and opc!="no":
                opc=input("¿Estas seguro que deseas borrar la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis=pelis.remove(peli)
                accionExitosa()
    else:

       input("\n\t\t... ¡No existe la pelicula a borrar, verifique! ...")


def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR PELICULAS :::...")
    peli=input("Escribe la pelicula a modificar: ").upper().strip()
    if peli in pelis:
        for i in range(0,len(pelis)):
            if peli==pelis[i]:
               opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)? ").lower().strip()
               while opc!="si" and opc!="no":
                   opc=input("¿Estas seguro que deseas modificar la pelicula (Si/No)? ").lower().strip()
                   if opc=="si":
                        pelis[i]=input("Escribe el nuevo nombre").upper().strip()
                        accionExitosa()