from banco_lista import BancoLista
from conta import Conta
from conta_poupanca import ContaPoupanca

def main():
    # Criando três bancos com diferentes taxas de juros
    banco_a = BancoLista(taxa_juros=0.05)  # Banco A com 5% de juros
    banco_b = BancoLista(taxa_juros=0.07)  # Banco B com 7% de juros
    banco_c = BancoLista(taxa_juros=0.10)  # Banco C com 10% de juros

    # Adicionando contas nos bancos

    # Banco A: conta bancária e conta poupança
    conta_a = Conta("12345-7")
    poupanca_a = ContaPoupanca("23456-7")
    banco_a.adicionar_conta(conta_a)
    banco_a.adicionar_conta(poupanca_a)

    # Banco B: conta bancária e conta poupança
    conta_b = Conta("34567-8")
    poupanca_b = ContaPoupanca("45678-8")
    banco_b.adicionar_conta(conta_b)
    banco_b.adicionar_conta(poupanca_b)

    # Banco C: conta bancária e conta poupança
    conta_c = Conta("56789-9")
    poupanca_c = ContaPoupanca("67890-9")
    banco_c.adicionar_conta(conta_c)
    banco_c.adicionar_conta(poupanca_c)

    # Realizando operações

    # Banco A: crédito e débito
    banco_a.creditar("12345-7", 500)
    banco_a.creditar("23456-7", 1000)
    banco_a.debitar("12345-7", 100)

    # Aplicando juros no Banco A
    banco_a.render_juros("23456-7")

    # Banco B: crédito e débito
    banco_b.creditar("34567-8", 1000)
    banco_b.creditar("45678-8", 1500)
    banco_b.debitar("34567-8", 500)

    # Aplicando juros no Banco B
    banco_b.render_juros("45678-8")

    # Banco C: crédito e débito
    banco_c.creditar("56789-9", 1500)
    banco_c.creditar("67890-9", 2000)
    banco_c.debitar("56789-9", 200)

    # Aplicando juros no Banco C
    banco_c.render_juros("67890-9")

    # Listando todas as contas em todos os bancos
    print("\nListando contas de todos os bancos:")
    banco_a.listar_contas()
    banco_b.listar_contas()
    banco_c.listar_contas()

if __name__ == "__main__":
    main()
