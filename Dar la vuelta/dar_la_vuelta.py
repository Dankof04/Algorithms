def dar_la_vuelta(cambio, valores_monedas):
    """
    Se recibe una cantidad de dinero y una lista de monedas. Se devuelve un generador de las monedas que se necesitan para dar ese cambio de forma que se minimice el número de monedas.

    Se han de devolver las monedas de mayor a menor valor.

    Nota: Para evitar el problema de los decimales en python se puede usar la función round() para redondear a dos decimales.
    """
    # Ordenamos los valores de menor a mayor (por defecto) y le damos la vuelta (para que sea de mayor a menor)
    valores_monedas = sorted(valores_monedas, reverse=True)

    # Redondeamos a dos decimales
    cambio = round(cambio, 2)

    # Mientras que el cambio sea mayor a 0
    while cambio > 0:

        # Por cada valor en la lista de monedas a devolver
        for element in valores_monedas:

            # Si el cambio restante a devolver es mayor o igual al valor de la moneda
            if cambio >= element:

                # Devolvemos la moneda (en un generador)
                yield element

                # Restamos el valor de la moneda al cambio restante a devolver (redondeando)
                cambio = round(cambio - element, 2)

                # Reiniciamos el bucle para contemplar aquellos casos que requieran utilizar varias veces una moneda
                break