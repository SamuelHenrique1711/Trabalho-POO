from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)
    
    def render_juros(self, taxa):
        """Aplica os juros sobre o saldo da conta."""
        juros = self.get_saldo() * taxa
        self.creditar(juros)  # Credita os juros na conta
        print(f"Juros de {taxa*100:.2f}% aplicados na conta poupança {self.numero}.")
