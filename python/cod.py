#exercicio 1

numero = float(input('digite um numero: '))
def nume():
    if numero <= 0:
        return 'negativo'
    elif numero >= 1:
        return 'positivo'
num = nume()
print(num)

#exercicio 2


t = float(input('digite a taxa de imposto: '))
c = float(input('digite o custo do produto: '))

def somaimposto(taxaimposto, custo):
    return (1 + taxaimposto / 100) * custo

print('valor com imposto: ', somaimposto(t,c))