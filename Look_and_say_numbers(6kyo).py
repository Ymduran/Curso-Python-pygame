def look_and_say(data='1', maxlen=5):
    """
    Genera la secuencia 'look-and-say' a partir de un valor inicial.

    Parámetros:
    data (str): Valor inicial de la secuencia, como cadena de dígitos.
    maxlen (int): Número máximo de iteraciones (longitud de la secuencia).

    Retorna:
    list: Lista con cada elemento de la secuencia generada.
    """
    resultado = [data]  # Lista donde se guarda la secuencia completa

    for _ in range(maxlen - 1):  # Con la primera
        actual = resultado[-1]  # Último elemento que se genera
        nuevo = ''
        contador = 1

        for i in range(1, len(actual)):
            if actual[i] == actual[i - 1]:
                contador += 1
            else:
                nuevo += str(contador) + actual[i - 1]
                contador = 1
        nuevo += str(contador) + actual[-1]  # Agregar el último grupo
        resultado.append(nuevo)

    return resultado


if __name__ == '__main__':
    print(look_and_say('12211', 15))
    print(look_and_say('1259', 5))
    print(look_and_say('1', 10))
