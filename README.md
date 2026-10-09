# Semana 06 — Sistema bancário orientado a objetos

Execute com `python3 main.py`.

## Modelagem

```mermaid
classDiagram
    Conta <|-- ContaCorrente
    Conta <|-- ContaPoupanca
    Banco o-- Conta
    class Conta { <<abstract>>\n+numero\n+titular\n+saldo\n+sacar() }
    class ContaCorrente { +sacar() }
    class ContaPoupanca { +sacar()\n+render() }
    class Cliente { +nome\n+email }
    class Banco { +contas\n+adicionar_conta() }
```

O projeto possui classe abstrata, herança com `super()` implícito pelo construtor herdado, encapsulamento com `@property`, polimorfismo em `sacar`, métodos `__str__`, `__repr__` e `__eq__`, dez instâncias de contas e tratamento de entradas inválidas. `Banco` usa composição para manter suas contas.

Também há uma versão comentada em `main.por`, representando classes, herança e polimorfismo em Portugol.
