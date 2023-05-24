class ContaBancaria:
    def __init__(self, nomeTitular,saldoInicial):
        self.nomeTitular = nomeTitular
        self.saldo = saldoInicial
        self.extrato = []
        self.saqueTotal = 0

    def saldoAtual(self):
        print (f"Saldo atual: R${self.saldo}")
    
    def depositar (self,valorDeposito):
        self.saldo += valorDeposito
        self.extrato.append("+ R$ " + str(valorDeposito))
        print(f"Valor R$ {valorDeposito} foi depositado!")
        self.saldoAtual()
    
    def sacar(self,valorSaque):
        taxa = 5
        if (valorSaque+(taxa/100)) > self.saldo:
            print ("Saldo insuficiente!")
        else:
            limite = 1000
            self.saqueTotal += (valorSaque + (taxa/100))
            if((self.saqueTotal+(taxa/100)) > limite):
                print ("Limite atingido!")
            else:
                self.extrato.append("- R$ " + str(valorSaque+(taxa/100)))
                self.saldo -= valorSaque + (taxa/100)
                print (f"Valor R$ {valorSaque} foi sacado!")
                print (f"Taxa de R$ {taxa/100}")
                self.saldoAtual()

    def exibirExtrato(self):
        print (f"Extrato:\n")
        for i in self.extrato:
            print (i)

    def transferir(self,valorTransferido,contaDestino):
        self.saldo -= valorTransferido
        contaDestino.depositar(valorTransferido)
        print(f"Transferendia de R$ {valorTransferido} realizada!")
        self.extrato.append("- R$ " + str(valorTransferido))


