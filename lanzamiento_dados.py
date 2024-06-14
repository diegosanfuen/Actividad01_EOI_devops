import dice
import sys
import time

def main():
    """
    Funcion principal que es ejecutada con los parámetros recibidos por consola
    Ejecuta la libreria dice para simular el lanzamiento de datos un número ammount de veces
    con un número side de caras
    :return: None
    """
    if len(sys.argv) != 3:
        print("Error: Se requieren exactamente dos argumentos. ")
        print("Uso: python lanzamiento_dados.py <ammount> <sides>")
        sys.exit(1)

    ammount = sys.argv[1]
    sides = sys.argv[2]

    try:
        ammount_i = int(ammount)
        sides_i = int(sides)
    except:
        print(f"El parámetro {ammount} y/o {sides} debe de ser un número entero")

    # Lanzamos el dado ammount veces de sides caras
    print(f"Lanzamos el dado de {sides} caras {ammount} veces")
    for i in range(ammount_i):
        print(f"Lanzamiento número {i}")
        resultado = dice.roll(f'1d{sides_i}')
        print(f"Resultado {resultado}")
        time.sleep(5)

if __name__ == "__main__":
    main()
