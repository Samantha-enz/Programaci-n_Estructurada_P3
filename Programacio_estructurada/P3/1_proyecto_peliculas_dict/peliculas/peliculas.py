import funciones

#pelis={
#    "Nombre": "",
#    "Duración":"",
#    "Idioma":"",
#    "Clasificacion":"",
#   "Genero":""
#    }
      
def menuPrincipal():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    caracteristica=input("Introducir el nombre de la caracteristica: ").lower().strip()
    valor=input("Introducir el valor de la caracteristica: ").upper().strip()
    pelis[caracteristica]=valor
    opc=""
    while opc != "si" and opc != "no":
        opc=input("¿Deseas agregar otra caracteristica? si/no").lower().strip()
        funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis)>0:
        print("\tCaracteristica\t\tValor\n")

        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")

        
    else:
        input("...¡No existe la caracteristica de la pelicula que estas buscando, verifique!...")
        funciones.espereTecla()

def limpiarPeliculas(pelis):
    print("\n\t\t...:::: LIMPIAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis)>0:
        opc=""
        while opc!="si" and opc!="no":
            opc=input("¿Deseas limpiar los valores de las caracteristicas (Si/No)? ").lower().strip()
        if opc=="si":
            pelis=pelis.clear()
            funciones.accionExitosa()
    else:
        input("...¡No hay caracteristicas para borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").lower().strip()
    noencontre=True #Es una bandera que si se cumple true, es porque no se encontro
    for i in pelis:
        if i == caracteristica:
            print(f"La caracteristica es: {peli} y su valor es: {pelis[caracteristica]}")
            funciones.espereTecla()
            noencontre=False #Se cambia el valor desde la primera vez que entre

    if noencontre:
        input("...¡No existe la caracteristica de la pelicula que estas buscando, verifique!...")

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    peli=input("Escribir el nombre de la caracteristica que desea borar: ").upper().strip()
    noencontre=True
    for i in pelis:
        if peli==i:
            noencontre=False
            opc=""            
            while opc!="si" and opc!="no":
              opc=input("¿Estas seguro que deseas borrar el valor de la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                caracteristica=peli
    if noencontre:
        input("\n\t... ¡No existe la caracteristica de  la pelicula a borrar, verifique! ...")

    else:
        pelis.pop(caracteristica)  #pop o puede estar dentro de un ciclo, necesita estar al final del ciclo 
        funciones.accionExitosa()
               
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE LA CARACTERISTICA ::::...\n")
    peli=input("Escribir el nombre de la caracteristica que desea modificar: ").upper().strip()
    noencontre=True
    for i in pelis:
        if peli==i:
            noencontre=False
            print(f"La caracteristica es {peli} y su valor actual es {pelis[peli]}")
            opc=""            
            while opc!="si" and opc!="no":
              opc=input("¿Estas seguro que deseas modificar el valor de la pelicula (Si/No)? ").lower().strip()
            if opc=="si":
                pelis[peli]=input("Escribe el nuevo valor de la caracteristica").upper().strip()
                funciones.accionExitosa()
            
    if noencontre:
        input("\n\t... ¡No existe la caracteristica de la pelicula que desea modificar, verifique! ...")



