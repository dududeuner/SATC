numero = 123
titular = 'Eduardo'
saldo = 200.0
limite = 1500.0


conta1 = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}

print(conta1)
print(conta1['numero'])
print(conta1['titular'])
print(conta1['saldo'])
print(conta1['limite'])

def criar_conta(numero, titular, saldo, limite):
  conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
  return conta


conta1 = criar_conta(333,'tetapreta',9999.0, 777.0)

print(conta1)


def deposita(conta, valor):
  conta['saldo'] += valor

deposita(conta1, 50.0)
conta1['saldo']

def sacar(conta, valor):
  conta['saldo'] -= valor

sacar(conta1, 10.0)
conta1['saldo']

def extrato(conta):
  print('saldo {}'.format(conta['saldo']))

extrato(conta1)

class ContaCorrente:
  pass

conta1 = ContaCorrente()
conta1

print(hex(id(conta1)))

class ContaCorrente:
  def __init__(self):
    print('construindo o objeto {}'.format(self))

    self.numero = 123
    self.titular = 'batatinha'
    self.saldo = 100.0
    self.limite = 1000.0

  def extrato(self):
    print('Saldo {} do titular {}'.format(self.saldo,self.titular))

  def deposita(self,valor):
    self.saldo += valor

  def sacar(self,valor):
    self.saldo -= valor

conta1 = ContaCorrente()
conta1.extrato()

conta1.deposita(100)
conta1.extrato()

conta1.sacar(50)
conta1.extrato()