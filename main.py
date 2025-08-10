participantes ={}

print("Menu principal")

def quic_sorter(lista):
    if len(lista) == 0:
        return lista

    pivot = lista[0]
    menor =[x for x in lista[:1] if x[1]["edad"] <= pivot[1]["edad"]]
    mayor =[x for x in lista[:1] if x[1]["edad"] > pivot[1]["edad"]]

    return quic_sorter(menor) + [pivot] + quic_sorter(mayor)

lista_participantes=list(participantes.items())
participantes_ordenados=quic_sorter(lista_participantes)


seleccion = ""
while seleccion != "0":
    print("\n1.Agregar participante")
    print("2.MOstrar particiapantes por edad")
    print("3.mostarr particiapantes por nombre")
    print("0. salir")
    seleccion = int(input())

    match seleccion:
        case 1:
            cantidad=int(input("\nIngrese la cantidad de participantes: "))
            for i in range(cantidad):
                print(f"\nIngrese la informacion del candidato: {i+1}")
                dorsal=int(input("Ingrese el numero dorsal: "))
                participantes[dorsal]={}
                participantes[dorsal]["nombre"]=int("Ingres el nombre: ")
                participantes[dorsal]["edad"]=int(input("Ingrese la edad: "))
                participantes[dorsal]["categoria"]=input("Ingrese la categoria: ")


            print("Participante registrada exitosamente")

        case "2":
            print("Participantes ordenados por nombre")
            for i,info in participantes_ordenados:
                print(f"Dorsal: {i}, Nombre: {info['nombre']}, Edad: {info['edad']}, Categoris: {info['categoria']}")




        case "3":
            print("Participantes ordenados por edad")





