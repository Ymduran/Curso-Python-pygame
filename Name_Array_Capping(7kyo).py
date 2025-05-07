def cap_me(arr):
    """
    Recibe una lista de nombres y devuelve una nueva lista con cada nombre
    capitalizado (primera letra en mayúscula, el resto en minúscula).
    
    Parámetros:
    arr (list): Lista de nombres como cadenas.
    
    Retorna:
    list: Lista con los nombres capitalizados.
    """
    nueva_lista = []

    for nombre in arr:
        if nombre:
            primera = nombre[0].upper()
            resto = nombre[1:].lower()
            nombre_nuevo = primera + resto
            nueva_lista.append(nombre_nuevo)
        else:
            nueva_lista.append("")  # Por si hay cadenas vacías

    return nueva_lista


if __name__ == '__main__':
    print(cap_me(["jo", "nelson", "jurie"]))
