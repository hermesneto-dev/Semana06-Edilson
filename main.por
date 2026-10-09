// Semana 06: modelagem orientada a objetos em Portugol.
// O arquivo é uma representação didática das classes usadas no Python.
programa {
    // Classe base abstrata: define atributos e a operação sacar.
    classe Conta {
        cadeia numero
        cadeia titular
        real saldo

        construtor(cadeia numero, cadeia titular, real saldo) {
            // Validações equivalentes aos setters com @property.
            se (saldo < 0) lance "Saldo não pode ser negativo"
            este.numero = numero
            este.titular = titular
            este.saldo = saldo
        }

        funcao depositar(real valor) {
            se (valor <= 0) lance "Depósito inválido"
            saldo = saldo + valor
        }

        funcao sacar(real valor) {
            // Método pensado para ser sobrescrito pelas classes filhas.
            se (valor > saldo) lance "Saldo insuficiente"
            saldo = saldo - valor
        }
    }

    classe ContaCorrente herda Conta {
        funcao sacar(real valor) {
            // Polimorfismo: corrente cobra uma tarifa adicional.
            real tarifa = 2.50
            se (valor + tarifa > saldo) lance "Saldo insuficiente"
            saldo = saldo - valor - tarifa
        }
    }

    classe ContaPoupanca herda Conta {
        funcao sacar(real valor) {
            // Polimorfismo: poupança não cobra tarifa.
            se (valor > saldo) lance "Saldo insuficiente"
            saldo = saldo - valor
        }
    }

    funcao inicio() {
        // Criação de objetos de classes diferentes para demonstrar polimorfismo.
        ContaCorrente corrente = novo ContaCorrente("1001", "Ana", 500)
        ContaPoupanca poupanca = novo ContaPoupanca("1002", "Bia", 500)
        tente {
            corrente.sacar(100)
            poupanca.sacar(100)
            escreva("Corrente: ", corrente.saldo, "\n")
            escreva("Poupança: ", poupanca.saldo, "\n")
        } capture (cadeia erro) {
            escreva("Erro tratado: ", erro, "\n")
        }
    }
}
