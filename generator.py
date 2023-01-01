import errores
#inicialización de variables
hours = int()
minutes = int()
seconds = int()
title = str()
color = str()
col = ""
color = ""
colour = ""
error = 0
reason = errores.razon(error)
#Funcion para verificar si el input es un numero o no.
def verificar_input(a):
    if a.isnumeric():
    # el input del usuario es un número
        return
    else:
    # el input del usuario no es un número, se genera excepción
        raise ValueError("value error")
#solicita información para generar el titulo del timer en el enlace.
title = str(input("titulo del timer?\t(oprima enter para dejar titulo vacio...)\n\t"))
#solicita información para las horas que se requieren en el enlace.
hora = input("cuantas horas? \n\t")
#si no se ingresa un valor, se genera un valor por defecto
if hora =="":
    seconds = 0
else:
    try:
        #se verifica la hora.
        verificar_input(hora)
        hours = hora
    except ValueError:
     # manejamos el error aquí y se le asigna el codigo de error
        error = 1.1
        reason = errores.razon(error)
    except:
     # si ocurre cualquier otro tipo de error, el estado de error es -1
        error = -1
        reason = errores.razon(error)
#solicita información para los minutos que se requieren en el enlace.
minutos = input("cuantos minutos?\n\t")
#si no se ingresa un valor, se genera un valor por defecto
if minutos =="":
    minutos = 0
else:
    try:
        #se verifican la validez del input
        verificar_input(minutos)
        minutes = minutos
    except ValueError:
     # manejamos el error aquí y se le asigna el codigo de error
        error = 1.2
        reason = errores.razon(error)
    except:
     # si ocurre cualquier otro tipo de error, el estado de error es -1
        error = -1
        reason = errores.razon(error)
segundos = input("cuantos segundos?\n\t")
#si no se ingresa un valor, se genera un valor por defecto
if segundos =="":
    seconds = 0
else:
    try:
        #se verifica la validez del input
        verificar_input(segundos)
        seconds = segundos
    except ValueError:
     # manejamos el error aquí y se le asigna el codigo de error 1.3
        error = 1.3
        reason = errores.razon(error)
    except:
     # si ocurre cualquier otro tipo de error, el estado de error es -1
        error = -1
        reason = errores.razon(error)
#se solicita información para el color
print("seleccione el color: \t")
print("0 = negro; 1 = blanco; 2 = rosa claro; 3 = rosa fuerte; 4 = morado twitch")
color = input("\n\ncolor:\t")
print(color)
#si no se ingresa un valor, se genera un valor por defecto
if color =="":
    col = 1
else:
    try:
        #se verifica que el input sea valido
        verificar_input(color)
        col = color
        #biblioteca de colores
        if col == "0" or col == 0:
            colpur  = "000" 
        elif col == "1" or col == 1:
            colour  = "fff"
        elif col == "2" or col == 2:
            colour  ="FDA1FF"
        elif col == "3" or col == 3:
            colour  = "FA28FF"
        elif col == "4" or col == 4:
            colour = "653294"
    except ValueError:
     # manejamos el error aquí y se le asigna el valor de error 1.4
        error = 1.4
        reason = errores.razon(error)
    except:
     # si ocurre cualquier otro tipo de error, el estado de error es -1
        error = -1
        reason = errores.razon(error)
if error != 0:
    print("error!\n")
    print("codigo de error: \n",error)
    print(f"error reason: \n {reason}")
    input("oprima enter para continuar...")
else:
    if colour != 0 or colour != 1 or colour != 2 or colour != 3 or colour != 4:
        try:
            base = f"https://cd.twitch-countdown.com/countdown.html?title={title}&hours={hours}&minutes={minutes}&seconds={seconds}&color={colour}&font=Open%20Sans"
            print(str(base),"\n\nenlace generado")
            input("oprima enter para continuar...")
        except:
            error = -1
            reason = errores.razon(error)
            print("error!\n")
            print("codigo de error: \n",error)
            print(f"error reason: \n ",reason)
            print("variables resultantes: ",str(hours,minutes,seconds,col))
            input("oprima enter para continuar...")
    else:        
        error = 1.5
        reason = "error en color"
        print("error!\n")
        print("codigo de error: \n",error)
        print(f"error reason: \n",reason = errores.razon(error))
        print("variables resultantes: ",str(hours,minutes,seconds,col))
        input("oprima enter para continuar...")