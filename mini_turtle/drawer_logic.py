import turtle

tortuga = "t"
espacios = 0

def adelante(camina_adelante):
    global espacios
    print((" " * espacios) + "→" + ("-" * camina_adelante) + "↓")
    espacios += camina_adelante + 1

def abajo(camina_abajo):
    for _ in range(camina_abajo):
        print((" " * espacios) + "|")



def reiniciar():
    global posicion_x
    posicion_x = 0