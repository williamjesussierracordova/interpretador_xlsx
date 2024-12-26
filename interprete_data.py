

import pandas as pd 

def interpretador (path):

    # lee el archivo

    if path.endswith(".xlsx"):
        data = pd.read_excel(path)
    elif path.endswith(".csv"):
        data = pd.read_csv(path)
    else:
        raise ValueError("El archivo no es un excel o csv")
    
    # agregar columna NRO_IMPRESION

    data["NRO_IMPRESION"] = range(1, len(data) + 1)

    # agregar columna ORDEN_CLIENTE

    data["ORDEN_CLIENTE"] = data["NRO_IMPRESION"].apply(lambda x: str(x).zfill(7))

    # se convierte a string todos los datos

    data = data.astype(str)

    # limpiar todas las columnas de espacios en blanco al principio y al final

    data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # guardamos el archivo como un table con el mismo nombre que el archivo original

    data.to_csv(path.replace(".xlsx", ".csv"), index=False)


    # analisis de datos

    # maximo largo de cada columna

    max_len = data.apply(lambda x: x.str.len().max())

    # marcar las columnas con valores mayores a 50

    max_len = max_len.apply(lambda x: f"{x}*" if x > 50 else x)

    # numero de registros en el archivo

    num_registros = len(data)

    # numero de columnas en el archivo

    num_columnas = len(data.columns)

    # guardar los resultados en un archivo txt

    with open(path.replace(".xlsx", "_analisis.txt"), "w", encoding="utf-8") as file:
        file.write(f"Numero de registros: {num_registros}\n")
        file.write(f"Numero de columnas: {num_columnas}\n")
        file.write("\n")
        file.write("Maximo largo de cada columna:\n")
        file.write(max_len.to_string())
    

def comparar (path1, path2):

    # leer los archivos

    if path1.endswith(".xlsx"):
        data1 = pd.read_excel(path1)
    elif path1.endswith(".csv"):
        data1 = pd.read_csv(path1)
    else:
        raise ValueError("El archivo no es un excel o csv")

    if path2.endswith(".xlsx"):
        data2 = pd.read_excel(path2)
    elif path2.endswith(".csv"):
        data2 = pd.read_csv(path2)
    else:
        raise ValueError("El archivo no es un excel o csv")

    # comparar las columnas de ambos archivos

    # imprimir las columnas que se encuentran en el archivo 1 y no en el archivo 2

    columnas_1_no_2 = data1.columns.difference(data2.columns)

    # imprimir las columnas que se encuentran en el archivo 2 y no en el archivo 1

    columnas_2_no_1 = data2.columns.difference(data1.columns)

    # imprimir las columnas que se encuentran en ambos archivos

    columnas_ambos = data1.columns.intersection(data2.columns)

    # guardar los resultados en un archivo txt

    with open(path1.replace(".xlsx", "_comparacion.txt"), "w", encoding="utf-8") as file:
        file.write("Columnas que se encuentran en el archivo "+ path1 +" y no en el archivo "+path2+":\n")
        file.write(str(columnas_1_no_2.to_list()))
        file.write("\n\n")
        file.write("Columnas que se encuentran en el archivo "+ path2 +" y no en el archivo "+path1+":\n")
        file.write(str(columnas_2_no_1.to_list()))
        file.write("\n\n")
        file.write("Columnas que se encuentran en ambos archivos:\n")
        file.write(str(columnas_ambos.to_list()))

