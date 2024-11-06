from calculadora import Calculadora


def get_valor(allow_zero=True):
    while True:
        try:
            valor = float(input("Valor: "))
            if (allow_zero and valor >= 0) or (valor > 0):
                return valor
            print("Valor inválido")
        except:
            print("Valor inválido, insira um número válido")


def main():
    calc = Calculadora()

    while True:
        print(calc)
        op = input("Operação: ").lower()
        if op == "q":
            print("Desligando...")
            break

        match op:
            case "+":
                valor = get_valor()
                calc.adicionar(valor)
            case "-":
                valor = get_valor()
                calc.subtrair(valor)
            case "*":
                valor = get_valor()
                calc.multiplicar(valor)
            case "/":
                valor = get_valor(allow_zero=False)
                calc.dividir(valor)
            case "r":
                calc.reset()
            case "d":
                calc.undo()
            case _:
                print("Operação desconhecida")


if __name__ == "__main__":
    main()
