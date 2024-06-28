import csv
import os
import datetime
opcion = ""
venta = False
if venta == False:
    venta = "Disponible"

def guardar():
    print("===== Guardar =====")
    patente = input("Patente: ")
    if len(patente.strip()) == 0:
        print("La patente no fue especificada")
        input("Presione enter para continuar...")
        return
    elif len(patente.strip()) > 6:
        print("La patente debe tener 6 caracteres")
        input("Presione enter para continuar...")
        return
    elif len(patente.strip()) < 6:
        print("La patente debe tener 6 caracteres")
        input("Presione enter para continuar...")
        return
    else:
        marca = input("Marca: ")
        if len(marca.strip()) == 0:
            print("La marca no fue especificada")
            input("Presione enter para continuar...")
            return
        elif len(marca.strip()) < 3:
            print("La marca debe tener por lo menos 3 caracteres")
            input("Presione enter para continuar...")
            return
        else:
            modelo = input("Modelo: ")
            if len(modelo.strip()) == 0:
                print("El modelo no fue especificado")
                input("Presione enter para continuar...")
                return
            elif len(modelo.strip()) < 3:
                print("El modelo debe tener por lo menos 3 caracteres")
                input("Presione enter para continuar...")
                return
            else:
                try:
                  anho = int(input("Año del vehículo: "))
                except:
                    print("Año no válido")
                    input("Presione enter para continuar...")
                    return
                if anho < 1980:
                     print("El año del vehículo tiene que ser superior a 1980")
                     input("Presione enter para continuar...")
                     return
                else:
                    try:
                        valor = int(input("Valor: "))
                    except:
                        print("El valor no es válido")
                        input("Presione enter para continuar...")
                        return
                    if valor < 500000:
                        print("El valor debe ser superior a 500.000")
                        input("Presione enter para continuar...")
                        return
                    else:
                        fila = [patente, marca, modelo, anho, valor, venta]

                        with open('Evaluacion3.csv', 'a', newline='') as doc:
                            escribir = csv.writer(doc)
                            escribir.writerow(fila)
                            print("Datos guardados correctamente")
                            input("Presione enter para continuar...")
                            return


def buscar():
    print("===== Buscar =====")
    filasDocumento = []
    with open('Evaluacion3.csv', 'r', newline='') as documento:
        datosDocumento = csv.reader(documento)
        for fila in datosDocumento:
            filasDocumento.append(fila)
    
    patente = input("Ingrese la patente: ")

    for fila in filasDocumento:
        if fila[0] == patente:
            print("-------------------------------")
            print("Patente         : ", fila[0])
            print("Marca           : ", fila[1])
            print("Modelo          : ", fila[2])
            print("Año del vehículo: ", fila[3])
            print("Valor           : ", fila[4])
            print("Disponibilidad  : ", fila[5])
            print("-------------------------------")
            fila[3] = int(fila[3])
            print("\nAños desde la fabricación: " ,2024- fila[3])
            input("Presione enter para continuar...")
            return


def listar():
    print("===== Listar =====")
    with open('Evaluacion3.csv', 'r', newline='') as documento:
     datosDocumento = csv.reader(documento)
     for fila in datosDocumento:
        print("Patente: ",fila[0],"Marca: ",fila[1],"Modelo: ",fila[2],"Año: ",fila[3],"Valor: ",fila[4],"Disponibilidad: ",fila[5])

    input("Presione enter para continuar...")
    return
    
def imprimir():
    print("===== Imprimir =====")
    fecha = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("Número de contrato: ",fecha)
    filasDocumento = []
    with open('Evaluacion3.csv', 'r', newline='') as documento:
        datosDocumento = csv.reader(documento)
        for fila in datosDocumento:
            filasDocumento.append(fila)
    
    patente = input("Ingrese la patente: ")

    for fila in filasDocumento:
        if fila[0] == patente:
            print("Patente: ",fila[0],"Marca: ",fila[1],"Modelo: ",fila[2],"Año: ",fila[3],"Valor: ",fila[4],"Disponibilidad: ",fila[5])
            if fila[5] == "Vendido":
                print("El vehículo no se encuentra disponible")
                input("Presione enter para continuar...")
                return
            else:
                fila[5]="Vendido"
                print("Compra exitosa")
                with open('Evaluacion3.csv', 'w', newline='') as documento: 
                   escribir = csv.writer(documento)
                   escribir.writerows(filasDocumento)
                
            input("Presione enter para continuar...")
            return


while opcion != "5":
    os.system("cls")
    print("===== Menú =====")
    print("1.-Guardar")
    print("2.-Buscar")
    print("3.-Listar")
    print("4.-Imprimir")
    print("5.-Salir")

    opcion = input("Ingrese una opción: ")

    if opcion not in ["1","2","3","4","5"]:
        print("Opción no válida")
        input("Presione enter para continuar...")
        continue
    elif opcion == "5":
        break
    elif opcion == "1":
        guardar()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        listar()
    else:
        imprimir()





