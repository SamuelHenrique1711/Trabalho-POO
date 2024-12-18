from conta import Conta
from conta_poupanca import ContaPoupanca

class BancoLista:
    def __init__(self, taxa_juros=0.05):
        """Inicializa o banco com uma taxa de juros e uma lista vazia de contas."""
        self.contas = []  # Usando list para armazenar as contas bancárias
        self.taxa_juros = taxa_juros  # Taxa de juros para poupança
    
    def adicionar_conta(self, conta):
        """Adiciona uma conta à lista de contas, se não existir já uma conta com o mesmo número."""
        if not self.conta_existe(conta.get_numero()):
            self.contas.append(conta)
            print(f"Conta {conta.get_numero()} adicionada com sucesso.")
        else:
            print(f"Conta {conta.get_numero()} já existe.")
    
    def conta_existe(self, numero_conta):
        """Verifica se uma conta com o número fornecido existe na lista."""
        return any(conta.get_numero() == numero_conta for conta in self.contas)
    
    def procurar_conta(self, numero_conta):
        """Busca uma conta pelo número na lista de contas."""
        for conta in self.contas:
            if conta.get_numero() == numero_conta:
                return conta
        return None
    
    def debitar(self, numero_conta, valor):
        """Debita um valor de uma conta específica."""
        conta = self.procurar_conta(numero_conta)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta não encontrada.")
    
    def creditar(self, numero_conta, valor):
        """Credita um valor em uma conta específica."""
        conta = self.procurar_conta(numero_conta)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta não encontrada.")
    
    def transferir(self, numero_conta_origem, numero_conta_destino, valor):
        """Realiza uma transferência entre duas contas."""
        conta_origem = self.procurar_conta(numero_conta_origem)
        conta_destino = self.procurar_conta(numero_conta_destino)
        
        if conta_origem and conta_destino:
            conta_origem.transferir(valor, conta_destino)
        else:
            print("Uma ou ambas as contas não foram encontradas.")
    
    def render_juros(self, numero_conta):
        """Aplica os juros na conta poupança especificada."""
        conta = self.procurar_conta(numero_conta)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(self.taxa_juros)
            print(f"Juros de {self.taxa_juros*100}% aplicados na conta poupança {numero_conta}.")
        else:
            print("Conta não encontrada ou não é uma conta poupança.")
    
    def listar_contas(self):
        """Lista todas as contas registradas no banco."""
        if not self.contas:
            print("Não há contas cadastradas.")
        else:
            print("Contas cadastradas:")
            for conta in self.contas:
                print(f"Conta {conta.get_numero()}")
