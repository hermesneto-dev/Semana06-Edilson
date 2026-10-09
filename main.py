# Este módulo modela um pequeno banco para demonstrar os principais conceitos de POO.
# As classes protegem seus atributos, validam entradas e compartilham um contrato abstrato.

"""Semana 06 - Sistema bancário orientado a objetos."""

from abc import ABC, abstractmethod
import re


# Conta define o contrato comum; não pode ser instanciada diretamente.
class Conta(ABC):
    """Classe abstrata que define o contrato comum das contas."""

    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not str(valor).strip():
            raise ValueError("O número da conta é obrigatório.")
        self._numero = str(valor)

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if len(str(valor).strip()) < 3:
            raise ValueError("O titular deve ter pelo menos três caracteres.")
        self._titular = str(valor).strip()

    # A propriedade controla o acesso ao saldo e impede valores negativos.
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        valor = float(valor)
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O depósito deve ser positivo.")
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        """Realiza um saque conforme a regra da conta."""

    def __str__(self):
        return f"{self.__class__.__name__} {self.numero} — {self.titular} — R$ {self.saldo:.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}(numero={self.numero!r}, titular={self.titular!r}, saldo={self.saldo!r})"

    def __eq__(self, outro):
        return isinstance(outro, Conta) and self.numero == outro.numero


# A conta corrente aplica tarifa no saque.
class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0.0):
        super().__init__(numero, titular, saldo)

    def sacar(self, valor):
        tarifa = 2.50
        if valor <= 0 or valor + tarifa > self.saldo:
            raise ValueError("Saldo insuficiente para saque e tarifa.")
        self._saldo -= valor + tarifa


# A poupança não cobra tarifa e possui rendimento.
class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0.0):
        super().__init__(numero, titular, saldo)

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self._saldo -= valor

    def render(self, taxa=0.01):
        self._saldo *= 1 + taxa


# Cliente valida o e-mail antes de armazená-lo.
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not re.fullmatch(r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$", valor):
            raise ValueError("E-mail inválido.")
        self._email = valor

    def __str__(self):
        return f"{self.nome} <{self.email}>"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"


# Banco usa composição: ele mantém uma coleção de objetos Conta.
class Banco:
    def __init__(self, nome, contas=None):
        self.nome = nome
        self.contas = [] if contas is None else list(contas)

    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("É necessário fornecer uma conta válida.")
        self.contas.append(conta)

    def __str__(self):
        return f"Banco {self.nome} — {len(self.contas)} contas"

    def __repr__(self):
        return f"Banco(nome={self.nome!r}, contas={self.contas!r})"


# Demonstra a criação de objetos, o polimorfismo e o tratamento de erros.
def main():
    clientes = [Cliente(f"Cliente {i}", f"cliente{i}@email.com") for i in range(1, 6)]
    contas = []
    for indice, cliente in enumerate(clientes, start=1):
        classe = ContaCorrente if indice % 2 else ContaPoupanca
        contas.append(classe(f"{1000 + indice}", cliente.nome, 100 * indice))
    contas.extend([
        ContaCorrente("2001", "Ana", 500), ContaPoupanca("2002", "Bia", 600),
        ContaCorrente("2003", "Caio", 700), ContaPoupanca("2004", "Duda", 800),
        ContaCorrente("2005", "Enzo", 900),
    ])
    banco = Banco("Banco Python", contas)
    print(banco)
    print("\nDemonstração de polimorfismo:")
    for conta in banco.contas:
        try:
            conta.sacar(10)
            print(f"{conta} | saque realizado")
        except ValueError as erro:
            print(f"{conta} | erro: {erro}")
    try:
        Cliente("Inválido", "email-sem-arroba")
    except ValueError as erro:
        print(f"\nValidação demonstrada: {erro}")


if __name__ == "__main__":
    main()
