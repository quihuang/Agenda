# **PROYECTO AGENDA DE CITAS**

## **Contexto**

implementar un programa que permita agendar citas a usuarios registrados.

## **Identificación del problema**

**Objetivo**

crear de una agenda de citas virtual en donde las personas se pueden registrar y solicitar una cita en una fecha y hora dada 

**Interesados**

Empresa - Cliente
Recepcionista - Usuario.

**Restriciones**

**Registro de personas**

Las personas se deben almacenar en una lista, la cual va a ir creciendo por cada registro.

En cada posición de la lista existe los datos de la persona.  Al registrar una persona debe validar los campos de acuerdo con lo siguiente: 

* Tipo de documento –, Texto, máximo dos caracteres, solo se acepta:  CC,
CE, TI, PA. 
* Número de documento – Texto, solo se permiten números, sin puntos ni
comas, tamaño máximo 12 caracteres. 
* Nombre, Texto máximo 30 caracteres.
* Apellido, Texto máximo 30 caracteres.
* Fecha de nacimiento, Texto, máximo 10 caracteres, formato de fecha 
AAAA-MM-DD.
* RH y grupo sanguíneo, texto, dos caracteres, el primer carácter solo se 
permite O, A, B, el segundo carácter permite + o -.
* Correo electrónico, texto de máximo 50 caracteres, debe existir solamente 
un símbolo @, después del símbolo @ debe existir mínimo 3 caracteres de
texto, después debe existir un símbolo punto (.), después deben existir
entre 2 a 3 caracteres de texto. 
* Número telefónico, texto de máximo 10 caracteres, solo se permiten
números, sin puntos, ni comas.

**Visualizar listado**

Se debe visualizar el listado de las personas en orden registro. Adicionalmente se debe calcular la edad de la persona y mostrar la fecha/hora de la cita en caso de tener una cita asociada, formato de la fecha de cita debe ser AAAA-MM-DD HH:MM. 

* Posición de registro
* Tipo de documento
* Número de documento
* Nombres y apellidos
* Edad
* Fecha/hora cita asignada 

**Asignar cita** 

Las citas solo se pueden asignar a personas que se encuentren registradas. Las citas se deben almacenar en una lista. Se debe validar que la fecha y hora de la cita no sea inferior a la fecha actual. Luego de que una cita se asigna no debe ser posible modificar los datos asociados a la misma.

Finalmente se debe mostrar un mensaje en pantalla como se indica a continuación: 

“Estimado xxxxx, su cita fue asignada correctamente para el día xxxxxx a las xxxxx horas ” 


## **Definir el problema**

**Información que conozco**

El sistema debe contar con las siguientes opciónes :

**Registrar una persona en el sistema :**

solo puede existir una persona con el mismo número de documento de identidad. Como requisito de calidad se deben validar todos los campos del formulario de registro. Las personas a registrar tienen asociados los siguientes datos: 

* Tipo de documento.
* Número de documento.
* Nombre.
* Apellido.
* Fecha de nacimiento.
* RH y grupo sanguíneo.
* Correo electrónico.
* Número telefónico.

**Visualizar un listado de las personas registradas donde se pueda visualizar :**

* Posición de registro
* Tipo de documento
* Número de documento
* Nombres y apellidos
* Edad
* Fecha/hora cita asignada 

**Asignar una cita a una persona :** 

Para poder asignar una cita la persona debe estar registrada, se debe solicitar su documento de identidad y luego de validado se debe solicitar una fecha y hora de la cita tentativa. El sistema debe validar que solo asignen fecha y hora superior a la fecha actual, nunca en el pasado. Luego de creada la cita no es posible modificar ningún dato. 

**Salir de la aplicación**

## **Explorar**

Se realizara un programa en python donde como estrategia se implementaran los conocimientos obtenidos en clases junto a buenas practicas aprendidas a lo largo del programa.


## **Actuar**

Se realiza la logica del programa analizando el problema y ejecutando el paso a paso del metodo ideal para poder saber con claridad lo que se desarrollo.

se aplican conocimientos de condicionales, ciclos ,operadores, funciones, diccionarios, tuplas y librerias.

## **Lograr**

Se desarrolla el reto de manera exitosa cumpliento con los requerimientos del mismo.
