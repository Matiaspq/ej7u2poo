def menu(viajero,numviajero):
    while True:
        print("a. Consultar cantidad de millas")
        print("b. Acumular millas")
        print("c. Canjear millas")
        opcion=input("Seleccione opcion: ")
        if opcion=="a":
            print(f"La cantidad total de millas acumuladas del viajero numero {numviajero} es de {viajero.cantidadTotalMillas()}")
        elif opcion=="b":
            millas=int(input("Ingrese millas"))
            print(f"Las millas acumuladas son: {viajero.acumularMillas(millas)}")
        elif opcion=="c":
            millas=int(input("Ingresa cantidad de millas a canjear"))
            viajero.canjearMillas(millas)
            print(f"Las millas restantes son: {viajero.cantidadTotalMillas()}")
        else: break