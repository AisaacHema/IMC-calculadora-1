def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos (kg)
    y la altura en metros (m).

    Fórmula: IMC = peso / altura^2
    """
    imc = peso / (altura ** 2)
    return imc

def main():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = calcular_imc(peso, altura)

    print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

if __name__ == "__main__":
    main()
