def razon(error):
    if error == 0:
        return "datos correctos"
    elif error == 1.1:
        return "valor ingresado en hora no válido"
    elif error == 1.2:
        return "valor ingresado en minutos no válido"
    elif error == 1.3:
        return "valor ingresado en segundos no válido"
    elif error == 1.4:
        return "valor ingresado en selección de color no válido"
    elif error == 1.5:
        return "error en color"
    elif error == 1.6: 
        return "error copiando el enlace al portapapeles"
    else:
        return "error no documentado. contactarse con Kaede159#0621 por discord."
