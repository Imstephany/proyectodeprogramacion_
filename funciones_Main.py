
#Funcion para comprobar la entrada en el tema 1
def comprobarEntrada(consumo_energia):
    n = 0
    planta = ""
    ciudad = ""
    while n == 0:
        planta = input("\nIngrese el nombre de la planta: ")
        ciudad = input("Ingrese el nombre de la ciudad: ")
        if planta in list(consumo_energia.keys()) and ciudad in list(consumo_energia[planta].keys()):
            n = 1
    return planta,ciudad


#Funcion Tema 1
def tota_Megavatios(planta,ciudad,dic_consumo):
    total = sum(list(dic_consumo[planta][ciudad]["consumos"]))
    return total


#Funcion para imprimir en el tema 1
def imprimirTema1(planta,ciudad,totalConsumo):
    print(f"\nEl total de megavatios de consumo de la planta {planta} en la ciudad {ciudad} es: {totalConsumo}\n")

#Funcion para comprobar la entrada en el tema 2
def comprobarEntrada2(informacion):
    n = 0
    ciudad = ""
    listaCiudades = []
    for region, tuplaCiudades in informacion.items():
        listaCiudades.extend(tuplaCiudades)
    while n == 0:
        ciudad = input("Ingrese el nombre de una ciudad para construir el diccionario: ")
        if ciudad in listaCiudades:
            n += 1
    return ciudad

#Funcion Tema 2
def dic_plantasEnCiudad(dic_consumo,ciudad):
    dic={}
    claves = []
    for planta,dicCiudad in dic_consumo.items():
        ciudades = list(dicCiudad.keys())
        if ciudad in ciudades:
            claves.append(planta)
    for planta in claves:
        totalConsumo = tota_Megavatios(planta,ciudad,dic_consumo)
        dic[planta]=totalConsumo
    return dic



#Funcion imprimir tema 2
def imprimirDicTema2(ciudad,dicPLantaConsumo):
    print(f"\nEl diccionario para la ciudad de {ciudad} es:\n{dicPLantaConsumo}")
    print()


#Tema 3
def recaudado_en_region(dic_Consumo,dic_info):
    regiones = list(dic_info.keys())
    region = 0
    n=0
    dineroRecaudado = 0
    while n == 0:
        region = input("Ingrese una region para ver el dinero recaudado: ")
        if region in regiones:
            n+=1
    ciudades = list(dic_info[region])
    for ciudad in ciudades:
        dicPlantaConsumo = dic_plantasEnCiudad(dic_Consumo,ciudad)
        for planta,consumo in dicPlantaConsumo.items():
            tarifa = dic_Consumo[planta][ciudad]["tarifa"]
            valor = consumo*tarifa
            dineroRecaudado+=valor
    print(f"\nEl dinero recaudado en la región solicitada es: ${dineroRecaudado}\n")

#Tema 4
def consumoPorMes(dicConsumo):
    indMes = int(input("Ingrese el numero del mes: "))
    listaTuplas = []
    indice = indMes - 1
    for planta,dicCiudad in dicConsumo.items():
        consumoxMes = [0,0,0,0,0,0,0,0,0,0,0,0]
        for ciudad,dicConsumoTarifa in dicCiudad.items():
            listaConsumo = list(dicConsumoTarifa["consumos"])
            for i in range(len(listaConsumo)):
                consumoxMes[i]+=listaConsumo[i]
        consumoMes = consumoxMes[indice]
        tupla= (planta,consumoMes)
        listaTuplas.append(tupla)

    print(f"\nEl consumo del {indMes}° mes del año es:\n ")
    for tupla in listaTuplas:
        print(f"Para la planta {tupla[0]}: {tupla[1]}")






