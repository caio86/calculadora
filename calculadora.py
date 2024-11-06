from errors import HistoricoVazioError


class Calculadora:
    def __init__(self) -> None:
        self.__registrador: float = 0.0
        self.__historico: list[float] = []

    def adicionar(self, valor: float):
        self.__historico.append(self.__registrador)
        self.__registrador += valor

    def subtrair(self, valor: float):
        self.__historico.append(self.__registrador)
        self.__registrador -= valor

    def multiplicar(self, valor: float):
        self.__historico.append(self.__registrador)
        self.__registrador *= valor

    def dividir(self, valor: float):
        self.__historico.append(self.__registrador)
        self.__registrador /= valor

    def undo(self):
        if not self.__historico:
            raise HistoricoVazioError("Histórico vazio")
        self.__registrador = self.__historico.pop()

    def reset(self):
        self.__registrador = 0
        self.__historico = []

    def exibe(self) -> str:
        tela = ""
        tela += "+---------------+\n"
        tela += f"| {self.__registrador:13.2f} |\n"
        tela += "+---------------+\n"
        tela += "|(+) somar\t|\n"
        tela += "|(-) subtrair\t|\n"
        tela += "|(/) dividir\t|\n"
        tela += "|(*) multiplicar|\n"
        tela += "|(r) resetar\t|\n"
        tela += "|(d) desfazer\t|\n"
        tela += "|(q) desligar\t|\n"
        tela += "+---------------+\n"

        return tela

    def get_registrador(self) -> float:
        return self.__registrador

    def __str__(self) -> str:
        return self.exibe()
