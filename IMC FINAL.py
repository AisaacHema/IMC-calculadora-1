def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    imc = peso / (altura ** 2)
    return imc

def determinar_categoria(imc):
    """Determina la categoría del IMC según los valores estándar."""
    if imc < 18.5:
        return "Peso bajo"
    elif 18.5 <= imc < 24.9:
        return "Peso saludable"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def obtener_dato_numerico(mensaje):
    """Obtiene un dato numérico del usuario con verificación."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valor debe ser mayor que 0. Inténtalo de nuevo.")
            else:
                return valor
        except ValueError:
            print("El dato ingresado no es válido. Por favor, ingresa un número.")

def obtener_dato_texto(mensaje):
    """Obtiene un dato textual del usuario con verificación."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        else:
            print("El dato ingresado no es válido. Por favor, ingresa un texto.")

def main():
    print("¡Hola! Bienvenido a la calculadora de IMC.")

    nombre = obtener_dato_texto("Por favor, ingresa tu nombre: ")
    edad = obtener_dato_numerico("Ahora, ingresa tu edad: ")

    print(f"\nGracias {nombre}! Vamos a calcular tu IMC.")
    
    peso = obtener_dato_numerico("Ingresa tu peso en kilogramos (kg): ")
    altura = obtener_dato_numerico("Ingresa tu altura en metros (m): ")

    imc = calcular_imc(peso, altura)
    categoria = determinar_categoria(imc)

    print(f"\nTu IMC es: {imc:.2f}")
    print(f"Categoría: {categoria}")

if __name__ == "__main__":
    main()
def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    imc = peso / (altura ** 2)
    return imc 

def determinar_categoria(imc):
    """Determina la categoría del IMC según los valores estándar."""
    if imc < 18.5:
        return "Peso bajo"
    elif 18.5 <= imc < 24.9:
        return "Peso saludable"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def obtener_dato_numerico(mensaje):
    """Obtiene un dato numérico del usuario con verificación."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valor debe ser mayor que 0. Inténtalo de nuevo.")
            else:
                return valor
        except ValueError:
            print("El dato ingresado no es válido. Por favor, ingresa un número.")

def obtener_dato_texto(mensaje):
    """Obtiene un dato textual del usuario con verificación."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        else:
            print("El dato ingresado no es válido. Por favor, ingresa un texto.")

def main():
    print("¡Hola! Bienvenido a la calculadora de IMC.")

    nombre = obtener_dato_texto("Por favor, ingresa tu nombre: ")
    edad = obtener_dato_numerico("Ahora, ingresa tu edad: ")

    print(f"\nGracias {nombre}! Vamos a calcular tu IMC.")
    
    peso = obtener_dato_numerico("Ingresa tu peso en kilogramos (kg): ")
    altura = obtener_dato_numerico("Ingresa tu altura en metros (m): ")

    imc = calcular_imc(peso, altura)
    categoria = determinar_categoria(imc)

    print(f"\nTu IMC es: {imc:.2f}")
    print(f"Categoría: {categoria}")

if __name__ == "__main__":
    main()
