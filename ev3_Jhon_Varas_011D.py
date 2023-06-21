from datetime import datetime
import os
import random
import msvcrt
import time

#Variables
sw=1
Pacientes=[]
flag=True 
Blanqueamientos=[]
TratamientosConducto=[]
Implantesdentales=[]


def fecha(date): 
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"] 
    #["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    day = date.day 
    month = months[date.month - 1] 
    year = date.year 
    messsage = "{}/{}/{}".format(day, month, year,)
    return messsage
now = datetime.now() 

def IniciarPrograma():
    print("Presione para continuar...")
    msvcrt.getch()
    os.system("cls")

def menu():
    print(" ")
    print("****************************")
    print("   Bienvenido a DentaSalud! ")
    print("****************************")
    print("       *Clinica Dental*     ")
    print(" 1 - Registrar Paciente     ")
    print(" 2 - Buscar Paciente        ")
    print(" 3 - Listar Pacientes       ")
    print(" 4 - Listar Tratamientos    ")
    print(" 5 - Salir                  ")
    print("****************************")
    print("       ")

def RegistrarPaciente():
    i=0
    flag0=True
    flag=True
    flag2=True
    flag3=True
    flag4=True
    global Paciente
    print("     ****Registrar Paciente****")
    print("                      ")
    while flag0==True:
        while flag==True:
            print("--Rut del paciente--")
            print(" ")
            Rut=input("Ingrese aqui ==> ")
            if len(Rut) >= 8 and len(Rut) <=9:
                print("")
                print("-Rut Registrado-")
                print(" ")
                os.system("cls")
                flag=False
            else:
                print(" ")
                print("-Rut Invalido, intente nuevamente-")
                print(" ")
        while flag3 == True:
            print("--Nombre del paciente--")
            print(" ")
            nombreP=input("Ingrese aqui ==> ")
            if nombreP:
                nombreP=nombreP.capitalize()
                break
            else:
                print(" ")
                print("-Debe ingresar un nombre-")
                print(" ")
        print(" ")
        while flag4==True:
            print("--Edad del paciente--")
            print(" ")
            Edad=int(input("Ingrese aqui ==> "))
            if Edad < 12:
                print(" ")
                print("-Su edad esta fuera del limite de edad permitido-")
                for i in range(5,0,-1):
                    print(f"Saliendo en...{i}")
                    time.sleep(1)
                    os.system("cls")
                flag=True
                flag2=False
                flag0=False
                break
            elif Edad >= 12:
                os.system("cls")
                flag4=False
        while flag==False:
            print("                           ")
            print("                      Tipo de Tratamiento ")
            print("--------------------------------------------------------------")
            print(" (B)Blanqueamiento  (T)Tratamiento conducto (I)Implante dental")
            print("--------------------------------------------------------------")
            print("                             ")
            TipoT=input("Escoja tipo de tratamiento(B/T/I): ")
            TipoT=TipoT.capitalize()
            if TipoT =='B':
                TipoT="Blanqueamiento"
                Blanqueamientos.append(TipoT)
                os.system("cls")
                flag=True
            elif TipoT=='T':
                TipoT="Tratamiento conducto"
                TratamientosConducto.append(TipoT)
                os.system("cls")
                flag=True
            elif TipoT=='I':
                TipoT="Implante dental"
                Implantesdentales.append(TipoT)
                os.system("cls")
                flag=True
            else:
                print(" ")
                print("Ingrese Tratamiento valido valida")
                print(" ")
                flag==False
        while flag2==True:
            print("       ")
            Paciente={"Rut": Rut, "Nombre del Paciente": nombreP, "Edad": Edad, "Tipo de tratamiento": TipoT}
            Pacientes.append(Paciente)
            print("Paciente registrado")
            print("                  ")
            respuesta=input("Desea agregar otro Paciente?(si/no): ")
            respuesta=respuesta.lower()
            print(" ")
            if respuesta=='si':
                flag2=False
                flag=True
                flag4=True
                os.system("cls")
            elif respuesta=='no':
                flag=False
                flag0=False
                os.system("cls")
                break
            elif respuesta != 'si' or respuesta!='no':
                    print("  ")
                    print("Ingrese solo 'si' o 'no'")
                    print(" ")
                    flag=True
        flag2=True
    os.system("cls")

def BuscarPaciente():
    print("     ****Buscar Paciente****")
    print("                          ")
    Rut=input("Ingrese rut del paciente:")
    for Paciente in Pacientes:
        if Paciente['Rut'] == Rut:
            for i in range(0,110,30):
                print(f"Buscando...{i}%")
                time.sleep(1)
                os.system("cls") 
            print("Paciente encontrado!!!")
            print("                     ")
            print(f"Rut: {Paciente['Rut']} || Nombre del paciente: {Paciente['Nombre del Paciente']} || Edad: {Paciente['Edad']} || Tipo de tratamiento: {Paciente['Tipo de tratamiento']} ")
        elif Paciente['ID'] != Rut:
            print("Paciente no registrado")
    print(" ")
    print("Presione para continuar...")
    msvcrt.getch()
    os.system("cls")

def ListarPacientes():
    print("   ****Listar Pacientes****")
    for i in range(0,110,30):
        print(f"Espere un momento...{i}%")
        time.sleep(1)
        os.system("cls")
    for Paciente in Pacientes:
        print(f"Rut: {Paciente['Rut']} || Nombre del paciente: {Paciente['Nombre del Paciente']} || Edad: {Paciente['Edad']} || Tipo de tratamiento: {Paciente['Tipo de tratamiento']} ")

def ListarTratamientos():
    flag=False
    cantidadB=len(Blanqueamientos)
    cantidadT=len(TratamientosConducto)
    cantidadI=len(Implantesdentales)
    print("     ****Listado de tratamientos****")
    while flag==False:
        print("                           ")
        print("                      Tipo de Tratamiento ")
        print("--------------------------------------------------------------")
        print(" (B)Blanqueamiento  (T)Tratamiento conducto (I)Implante dental")
        print("--------------------------------------------------------------")
        print("                             ")
        TipoT=input("Escoja tipo de tratamiento(B/T/I): ")
        TipoT=TipoT.capitalize()
        if TipoT =='B':
            TipoT="Blanqueamiento"
            os.system("cls")
            flag=True
        elif TipoT=='T':
            TipoT="Tratamiento conducto"
            os.system("cls")
            flag=True
        elif TipoT=='I':
            TipoT="Implante dental"
            os.system("cls")
            flag=True
        else:
            print(" ")
            print("Ingrese Tratamiento valido valida")
            print(" ")
            flag==False
    if TipoT == 'Blanqueamiento':
        for Paciente in Pacientes:
            if Paciente['Tipo de tratamiento']== TipoT:
                print("***********************************")
                print(f"Sr/Sra {Paciente['Nombre del Paciente']}")
                print(f"Rut:{Paciente['Rut']}")
                print("    ")
                print(f"Para su {Paciente['Tipo de tratamiento']}")
                print(f"le faltan {random.randrange(1,5)} sesiones por completar")
                print("")
                print("***********************************")
                print("          ")
        print(f"Se generaron {cantidadB} reportes de {Paciente['Tipo de tratamiento']} ")
    if TipoT == 'Tratamiento conducto':
        for Paciente in Pacientes:
            if Paciente['Tipo de tratamiento']== TipoT:
                print("***********************************")
                print(f"Sr/Sra {Paciente['Nombre del Paciente']}")
                print(f"Rut:{Paciente['Rut']}")
                print("    ")
                print(f"Para su {Paciente['Tipo de tratamiento']}")
                print(f"le faltan {random.randrange(1,5)} sesiones por completar")
                print("")
                print("***********************************")
                print("          ")
        print(f"Se generaron {cantidadT} reportes de {Paciente['Tipo de tratamiento']} ")
    if TipoT == 'Implante dental':
        for Paciente in Pacientes:
            if Paciente['Tipo de tratamiento']== TipoT:
                print("***********************************")
                print(f"Sr/Sra {Paciente['Nombre del Paciente']}")
                print(f"Rut:{Paciente['Rut']}")
                print("    ")
                print(f"Para su {Paciente['Tipo de tratamiento']}")
                print(f"le faltan {random.randrange(1,5)} sesiones por completar")
                print("")
                print("***********************************")
                print("          ")
        print(f"Se generaron {cantidadI} reportes de {Paciente['Tipo de tratamiento']} ")
    print("Presione para continuar...")
    msvcrt.getch()
    os.system("cls")





IniciarPrograma()
while sw==1:
    try:
        menu()
        opcion=int(input("Seleccione opcion:"))
        os.system("cls")
        print("                       ")
        if opcion==1:
            RegistrarPaciente()
        if opcion==2:
            BuscarPaciente()
        if opcion==3:
            ListarPacientes()
        if opcion==4:
            ListarTratamientos()
        if opcion==5:
            print("                                                  ")
            for i in range(5,0,-1):
                print(f"Saliendo en...{i}")
                time.sleep(1)
                os.system("cls")
            print(f"Jhon Varas    Fecha: {fecha(now)}")
            sw=0
    except:
        print("Error, Intente nuevamente")