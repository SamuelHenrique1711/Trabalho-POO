class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

    def get_numero(self):
        return self.numero
    
    def get_saldo(self):
        return self.saldo
    
    def creditar(self, valor):
        """Credita um valor na conta"""
        self.saldo += valor
        print(f"Crédito de {valor:.2f} realizado na conta bancária {self.numero}.")
    
    def debitar(self, valor):
        """Debita um valor da conta"""
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Débito de {valor:.2f} realizado na conta bancária {self.numero}.")
        else:
            print(f"Saldo insuficiente na conta {self.numero}.")
