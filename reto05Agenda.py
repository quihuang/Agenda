
import os
import re
from datetime import datetime

def validateTypeDocument (typeDoc: str) -> str:

    """
    Función encargada de validar si el tipo de documento ingresado es correcto.

    Parameters
    ------------------
    typeDoc : str
        Numero de la opcion del documento.

    Returns
    ------------------
    validateTypeDoc : str
        Retorna el tipo de documento, de lo contrario devuelve un INVALID
    """

    validateTypeDoc = ""

    if(typeDoc == "1"):
        validateTypeDoc = "CC"
    elif(typeDoc == "2"):
         validateTypeDoc = "CE"
    elif(typeDoc == "3"): 
         validateTypeDoc = "TI"
    elif(typeDoc == "4"):
         validateTypeDoc = "PA"
    else:
        validateTypeDoc = "INVALID"
 
    return validateTypeDoc

def validateDocumentNumber (numberDoc: str) -> bool:

    """
    Función encargada de validar si el numero de documento ingresado es correcto.

    Parameters
    ------------------
    numberDoc : str
        Numero de documento.

    Returns
    ------------------
    valNumDoc : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNumDoc = False
    NumDoc = bool(re.search(r'^\d+$', numberDoc))
    lenNumDoc = len(numberDoc)

    if(NumDoc and lenNumDoc <= 12):
        valNumDoc = True

    return valNumDoc 

def validateNameAndLastName (namesOrLastName: str) -> bool:
    
    """
    Función encargada de validar si nombre o el apellido ingresado es correcto.

    Parameters
    ------------------
    namesOrLastName : str
        Nombre o apellido del suario.

    Returns
    ------------------
    valNumDoc : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNamesDig = bool(re.search(r'\d', namesOrLastName))
    valNames = False

    if(namesOrLastName != "" and valNamesDig !=True and len(namesOrLastName) <= 30):
        valNames = True
    return valNames

def validateBirthDate (date: str) -> bool:

    """
    Función encargada de validar la fecha de nacimiento ingresada es correcto.

    Parameters
    ------------------
    date : str
        fecha de nacimiento.

    Returns
    ------------------
    valDate : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """
    
    valDate = False
    try:
        datetime.strptime(date, '%Y-%m-%d')
        valDate = True
    except:
        valDate = False

    return valDate

def calculateAge (birthDate: str) -> int:

    """
    Función encargada de calcular la edad del usuario.

    Parameters
    ------------------
    birthDate : str
        fecha de nacimiento.

    Returns
    ------------------
    age : int
        Retorna la edad actual del usuario
    """

    daybirthDate = datetime.strptime(birthDate, '%Y-%m-%d')
    currentDate = datetime.now()

    age = currentDate.year - daybirthDate.year

    return age

def validateBloodType (bloodType: str) -> bool:

    """
    Función encargada de validar el tipo de sangre del usuario.

    Parameters
    ------------------
    bloodType : str
        Grupo sanguineo del usuario.

    Returns
    ------------------
    valBloodType : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    letter = ["O","A","B"]
    sign = ["+","-"]
    
    valBloodType = False
    if(len(bloodType) == 2):
        for l in letter :
            if(bloodType[0].upper() == l):
                for s in sign :
                    if(bloodType[1].upper() == s):
                         valBloodType = True

    return valBloodType
        
def validateEmail (email: str) -> bool:

    """
    Función encargada de validar el correo electronico del usuario.

    Parameters
    ------------------
    email : str
        correo electronico del usuario.

    Returns
    ------------------
    valEmail : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valEmailRex = bool(re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email))
    valEmail = False

    if(valEmailRex and len(email) <=50):
        valEmail = True

    return valEmail

def validatePhoneNumber(phoneNumber: str) -> bool:

    """
    Función encargada de validar si el numero de telefono ingresado es correcto.

    Parameters
    ------------------
    phoneNumber : str
        Numero de telefono.

    Returns
    ------------------
    valNumPhone : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNumPhone = False
    NumPhone = bool(re.search(r'^\d+$', phoneNumber))
    lenNumphone = len(phoneNumber)

    if(NumPhone and lenNumphone <= 10):
        valNumPhone = True

    return valNumPhone 

def inputUserDatabase(typeDoc: str,numDoc: str,name: str,lastName: str,birthDate: str,typeBlood: str,email: str,phoneNumber: str,table: list): 

    """
    Función encargada insertar los diccionarios al array de usuarios.

    Parameters
    ------------------
    typeDoc : str
        Tipo Documento.
    numDoc : str
        Numero Documento.
    name : str
        Nombres del usaurio.
    lastName : str
        Apellidos del usaurio.
    birthDate : str
        Fecha de nacimiento del usaurio.
    typeBlood : str
        Grupo de sangre.
    email : str
        correo electronico.
    phoneNumber : str
        Numero de telefoono.
    table : list
        Array donde se van a guardar los diccionarios de los usuarios creados. 

    Returns
    ------------------
    No retorna parametros
    """

    user = {
            "Tipo Documento":typeDoc,
            "Numero Documento":numDoc,
            "Nombres":name,
            "Apellidos":lastName,
            "Fecha de nacimiento":birthDate,
            "RH":typeBlood,
            "Correo":email,
            "Numero de telefono":phoneNumber
            }

    table.append(user)

def validateExistUser(numDoc: str,table: str) -> bool:

    """
    Función encargada de validar si un usuario ya se encuentra registrado.

    Parameters
    ------------------
    numDoc : str
        Numero de documento.
    table : str
        Array donde se guardan los usuarios 

    Returns
    ------------------
    valNumDoc : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNumDoc = False
    for doc in table:
        if doc["Numero Documento"] == numDoc:
            valNumDoc = True
    
    return valNumDoc

def validateDate (date: str) ->bool:

    """
    Función encargada de validar la fecha de la cita ingresada es correcta.

    Parameters
    ------------------
    date : str
        fecha de la cita.

    Returns
    ------------------
    valDate : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """
    
    valDate = False
    try:
        datetime.strptime(date, '%Y-%m-%d %H:%M')
        valDate = True
    except:
        valDate = False

    return valDate

def validarteDateCurrent (date: str) -> bool:

    """
    Función encargada de validar la fecha de la cita ingresada no sea inferior a la actual.

    Parameters
    ------------------
    date : str
        fecha de la cita.

    Returns
    ------------------
    valDate : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """
    valDate = False
    dateCurrent = datetime.now()
    dateUser =  datetime.strptime(date, '%Y-%m-%d %H:%M')
    
    if(dateUser >= dateCurrent):
        valDate = True

    return valDate

def createDataAppointment (numDoc: str,date: str,tableSearch: list,tableInsert: list) -> str:

    """
    Función encargada registar una cita.

    Parameters
    ------------------
    numDoc : str
        Numero de documento del usuario.
    date : str
        Fecha de agendamiendo de la cita.
    tableSearch : list
        Array de busqueda de usuarios registrados.
    tableInsert : list
        Array donde se guarda la informacion de las citas creadas.

    Returns
    ------------------
    messageConfirm : str
        retorna el mensaje de confirmación de la creación de la cita en el siguiente formato : 
        "Estimado xxxxx, su cita fue asignada correctamente para el día xxxxxx a las xxxxx horas"
    """

    DataAppointment = ()
    messageConfirm = ""

    for idUser, carro in enumerate(tableSearch):
        if carro["Numero Documento"] == numDoc:
            controler = idUser
            
    typeDoc = tableSearch[controler].get("Tipo Documento")
    numDoc = tableSearch[controler].get("Numero Documento") 
    name = tableSearch[controler].get("Nombres")
    lastName = tableSearch[controler].get("Apellidos")
    age = calculateAge(tableSearch[controler].get("Fecha de nacimiento"))
    asigDate = date
    
    DataAppointment = (typeDoc,numDoc,name,lastName,age,asigDate)

    tableInsert.append(DataAppointment)

    dateTemp = asigDate.split(' ')

    messageConfirm = f"\nEstimado {name} {lastName}, su cita fue asignada correctamente para el día {dateTemp[0]} a las {dateTemp[1]} horas"

    return messageConfirm

def displayAppointment(tableAppointment: list) -> str:

    """
    Función de mostrar los usuarios que tienen citas agendadas.

    Parameters
    ------------------
    tableAppointment : list
        Array de usuarios que tienen una cita agendada.

    Returns
    ------------------
    displayAppointment : str
        retorna en caso de que la lista tenga registros muestra los usuarios con
        citas agendadas en el caso q no, muestra el siguiente mensaje: (NO HAY CITAS AGENDADAS)
    """

    if(len(tableAppointment) > 0):
        displayAppointment = "\n======================================\n"
        displayAppointment += "    LISTADO DE DE CITAS AGENDADAS     \n"
        displayAppointment += "======================================\n"

        for id, users in enumerate(tableAppointment):

            displayAppointment += f"\nid : {str(id+1)}\n"
            displayAppointment += f"Tipo Documento : {str(users[0])}\n"
            displayAppointment += f"Numero Documento : {str(users[1])}\n"
            displayAppointment += f"Nombres : {str(users[2])}\n"
            displayAppointment += f"Apellidos : {str(users[3])}\n"
            displayAppointment += f"Edad : {str(users[4])}\n"
            displayAppointment += f"Fecha de cita : {str(users[5])}\n"

            displayAppointment += "\n---------------------------------------\n"
    else:

        displayAppointment = "\n---------------------------------------\n"
        displayAppointment += "         NO HAY CITAS AGENDADAS         \n"
        displayAppointment += "---------------------------------------\n"
    
    return displayAppointment

def displayUsersRegisters(tableUserRegisters: list)-> str:

    """
    Función se encarga de mostrar los usuarios que estan registrados en el sistema.

    Parameters
    ------------------
    tableUserRegisters : list
        Array de usuarios que estan registrados.

    Returns
    ------------------
    displayUsersRegisters : str
        retorna en caso de que la lista tenga registros muestra los usuarios registado en 
        el sistema en el caso q no, muestra el siguiente mensaje: (NO HAY USUARIOS REGISTRADOS)
    """

    if(len(tableUserRegisters) > 0):
        displayUsersRegisters = "\n======================================\n"
        displayUsersRegisters += "  LISTADO DE DE USUARIOS REGISTRADOS   \n"
        displayUsersRegisters += "======================================\n"

        for id, users in enumerate(tableUserRegisters):
            displayUsersRegisters += f"\nid : {str(id+1)}\n"
            for user in users:
                displayUsersRegisters += f"{user} : {str(users[user])}\n"
            displayUsersRegisters += "\n---------------------------------------\n"

        displayUsersRegisters += "======================================\n"
    else:

        displayUsersRegisters = "\n---------------------------------------\n"
        displayUsersRegisters += "      NO HAY USUARIOS REGISTRADOS      \n"
        displayUsersRegisters += "---------------------------------------\n"
    
    return displayUsersRegisters

messageExit = "\nSaliendo del programa..."
messageDataInvalid = "\nEl valor ingresado no es valido."
messageOptionInvalid = "\nLa opción ingresada no es valida."
messageNameInvalid = "\nEl nombre ingresado es invalido.No debe contener numeros o sobre pasar los 30 caracteres."
messageLastNameInvalid = "\nEl apellido ingresado es invalido.No debe contener numeros o sobre pasar los 30 caracteres."
messageUserNotExist = "\nEl usuario ingresado no se encuentra registrado en el sistema."
messageUserRegister = "\nEl usuario se a registrado correctamente."
messageUserExist = "\nEl usuario ya se encuentra registrado en el sistema."
messageDateInvalid = "\nLa fecha no puede ser inferior a la actual."
option = ""
dbUsers = []
dbDataAsig = []

#Datos quemados de usuarios, Descomentar en caso de querer hacer la prueba de agendamiento de citas sin necesidadad de ingresar usuarios.
"""
dbUsers = [
    {
     "Tipo Documento":"CC",
     "Numero Documento":"1144213155",
     "Nombres":"Franklin German",
     "Apellidos":"Quihuang Garzon",
     "Fecha de nacimiento":"1999-12-08",
     "RH":"O+",
     "Correo":"quihuang2017@gmail.com",
     "Numero de telefono":"3205282231"
    },
    {
     "Tipo Documento":"TI",
     "Numero Documento":"94417272",
     "Nombres":"Pepito",
     "Apellidos":"Perez",
     "Fecha de nacimiento":"2011-02-02",
     "RH":"O+",
     "Correo":"pepitopez@hotmail.es",
     "Numero de telefono":"454323234"
    },
    {
     "Tipo Documento":"PA",
     "Numero Documento":"0332423123",
     "Nombres":"Victor Alfonso",
     "Apellidos":"Zapata Ocampo",
     "Fecha de nacimiento":"2002-08-30",
     "RH":"A+",
     "Correo":"victor@gmail.com",
     "Numero de telefono":"123434254"
    },
    {
     "Tipo Documento":"CC",
     "Numero Documento":"96754321",
     "Nombres":"Juan Carlos",
     "Apellidos":"Zambrano Montealegre",
     "Fecha de nacimiento":"1992-05-12",
     "RH":"O+",
     "Correo":"juanzambrano.tic@ucaldas.edu.co",
     "Numero de telefono":"3176415522"
    }
]
"""

while option !="5":

    print("\n================================================")
    print(" Bienvenido al software de Agendamiento virtual ")
    print("================================================")
    print("1. Registrarse.")
    print("2. Asignar una cita.")
    print("3. Visualizar citas agendadas.")
    print("4. Visualizar usuarios registrados")
    print("5. Salir.")
    print("================================================")

    option = input("\nPorfavor ingrese una opción : ")

    if(option == "1"):
        os.system("clear")

        print("\nDiligencie el siguiente formulario para el registro del usuario : ")

        typeDoc = "INVALID"
        numberDoc = False
        name = False
        lastName = False
        birthDate = False
        typeBlood = False
        email = False
        numerPhone = False
        validateDoc = True

        while typeDoc == "INVALID":

            typeDocument = input("\nTipo de documento: \n\n1. CC \n2. CE \n3. TI \n4. PA \n\nIngrese una opción : \n» ")
            typeDoc = validateTypeDocument(typeDocument)

            if(typeDoc == "INVALID"):
                os.system("clear")
                print(messageOptionInvalid)

        while numberDoc != True :

            numberDocuments = input("\nIngrese su numero de documento (solo se permiten números, sin puntos ni comas) : \n» ")
            numberDoc = validateDocumentNumber(numberDocuments)

            if(numberDoc == False):
                os.system("clear")
                print(messageDataInvalid)

            while validateDoc == True :

                validateDoc = validateExistUser(numberDocuments,dbUsers)

                if(validateDoc == True):
                    os.system("clear")
                    print(messageUserExist)
                    validateDoc = False
                    numberDoc = False

            validateDoc = True

        while name != True:

            inputName = input("\nIngrese su nombre : \n» ")
            name = validateNameAndLastName(inputName)

            if(name == False):
                os.system("clear")
                print(messageNameInvalid)

        while lastName !=True:

            inputLastName = input("\nIngrese su apellido : \n» ")
            lastName = validateNameAndLastName(inputLastName)

            if(lastName == False):
                os.system("clear")
                print(messageLastNameInvalid)

        while birthDate != True:

            inputBirthDate = input("\nDigite su fecha de nacimiento en el formato AAAA-MM-DD: \n» ")
            birthDate = validateBirthDate(inputBirthDate)

            if(birthDate == False):
                os.system("clear")
                print(messageDataInvalid)

        while typeBlood != True:

            inputBloodType =  input("\nDigite su tipo de sangre (O+, O-, A-, A+, B-, B+) : \n» ").upper()
            typeBlood = validateBloodType(inputBloodType)

            if(typeBlood == False):
                os.system("clear")
                print(messageDataInvalid)

        while email != True:

            inputEmail = input("\nIngrese su correo electronico : \n» ")
            email = validateEmail(inputEmail)

            if(email == False):
                os.system("clear")
                print(messageDataInvalid)

        while numerPhone != True:

            inputPhoneNumber = input("\nIngrese su numero de telefono : \n» ")
            numerPhone = validatePhoneNumber(inputPhoneNumber)

            if(numerPhone == False):
                os.system("clear")
                print(messageDataInvalid)

        os.system("clear")


        inputUserDatabase(typeDoc,numberDocuments,inputName,inputLastName,inputBirthDate,inputBloodType,inputEmail,inputPhoneNumber,dbUsers) 
        
        print(f"\nEl usuario {inputName} {inputLastName} con Identificacion {typeDoc} {numberDocuments} ha sido registro Exitosamente!")

    elif(option == "2"):
        os.system("clear")
        
        validateDoc = False
        numberDoc = False
        date = False
        validDataCurrent = False
        
        while numberDoc != True :

            numberDocuments = input("\nIngrese el numero de documento solo se permiten números, sin puntos ni comas: \n» ")
            numberDoc = validateDocumentNumber(numberDocuments)

            if(numberDoc == False):
                os.system("clear")
                print(messageDataInvalid)
                validateDoc = True

            while validateDoc == False :

                validateDoc = validateExistUser(numberDocuments,dbUsers)

                if(validateDoc == False):
                    os.system("clear")
                    print(messageUserNotExist)
                    validateDoc = True
                    numberDoc = False

            validateDoc = False

        while date != True:
            inputDate = input("\nDigite su fecha de nacimiento en el formato AAAA-MM-DD HH:MM : \n» ")
            date = validateDate(inputDate)

            if(date == False):
                os.system("clear")
                print(messageDataInvalid)
                validDataCurrent = True
        
            while validDataCurrent != True :

                validDataCurrent = validarteDateCurrent(inputDate)

                if(validDataCurrent == False):
                    os.system("clear")
                    print(messageDateInvalid)
                    validDataCurrent = True
                    date = False

            validDataCurrent = False

        messageConfirm = createDataAppointment(numberDocuments,inputDate,dbUsers,dbDataAsig)

        print(messageConfirm)
    elif(option == "3"):
        os.system("clear")
        
        displayAppointments = displayAppointment(dbDataAsig)

        print(displayAppointments)

    elif(option == "4"):
        os.system("clear")
        
        displayUsersRegister = displayUsersRegisters(dbUsers)

        print(displayUsersRegister)
         
    elif(option == "5"):
         os.system("clear")
         print(messageExit)
    else:
        os.system("clear")
        print(messageOptionInvalid)