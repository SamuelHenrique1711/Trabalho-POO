from conta import Conta
from conta_poupanca import ContaPoupanca

class Banco:
    def __init__(self, nome, taxa_juros):
        self.nome = nome
        self.contas = []  # Lista de contas do banco
        self.taxa_juros = taxa_juros  # Taxa de juros do banco (em decimal, ex: 0.05 para 5%)
    
    def adicionar_conta(self, conta):
        """Adiciona uma conta ao banco."""
        self.contas.append(conta)
    
    def procurar_conta(self, numero):
        """Procura uma conta pelo número da conta."""
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
        return None
    
    def render_juros(self, numero, taxa_juros_percentual):
        """Aplica os juros na conta poupança do banco com base no número da conta."""
        conta = self.procurar_conta(numero)
        if conta and isinstance(conta, ContaPoupanca):
            # Calcula o valor dos juros com a taxa em percentual
            conta.render_juros(taxa_juros_percentual / 100)  # Convertendo de % para decimal
            print(f"Juros de {taxa_juros_percentual}% aplicados na conta poupança {numero}.")
        else:
            print(f"Conta bancária {numero} não encontrada ou não é uma conta poupança.")
