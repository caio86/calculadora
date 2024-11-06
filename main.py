from time import sleep

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
    mensagem = "Ligando..."

    while True:
        calc.exibe(mensagem)
        op = input("Operação: ").lower()

        if op == "q":
            mensagem = "Desligando..."
            calc.exibe(mensagem)
            sleep(0.5)
            break

        match op:
            case "+":
                valor = get_valor()
                calc.adicionar(valor)
                mensagem = f"Adicionado {valor}"
            case "-":
                valor = get_valor()
                calc.subtrair(valor)
                mensagem = f"Subtraido {valor}"
            case "*":
                valor = get_valor()
                calc.multiplicar(valor)
                mensagem = f"Multiplicado por {valor}"
            case "/":
                valor = get_valor(allow_zero=False)
                calc.dividir(valor)
                mensagem = f"Dividido por {valor}"
            case "r":
                calc.reset()
                mensagem = "Calculadora reiniciada"
            case "d":
                calc.undo()
                mensagem = "Operação revertida"
            case _:
                mensagem = "Operação desconhecida"


if __name__ == "__main__":
    main()
