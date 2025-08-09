participantes ={}

print("Menu principal")
cantidad=int(input("Ingrese la cantidad de participantes: "))
for i in range(cantidad):
    print(f"\nIngrese los datos de participante: {i+1}")
    numeroDorsal=int(input("Ingrese el numero de dorsal: "))
    participantes[numeroDorsal] = {}

    participantes[numeroDorsal]["nombre"]=input("Ingrese el nombre del dorsal: ")
    participantes[numeroDorsal]["edad"]=int(input("Ingrese el edad: "))
    participantes[numeroDorsal]["categoria"]=input("Ingrese el categoria: ")

