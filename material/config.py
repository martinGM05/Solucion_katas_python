def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("No se pudo encontrar el archivo config.txt")
        elif err.errno == 13:
            print("Encontré config.txt pero no pude leerlo")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("Encontré config.txt pero es un directorio, no pude leerlo")
    except PermissionError:
        print("No tengo permisos para leer el archivo config.txt")
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivos con mucha carga, no se puede completar la lectura del archivo de configuración")

if __name__ == '__main__':
    main()  
