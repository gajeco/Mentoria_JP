valor = int(input())
resultado = 0

print(valor)

resultado = valor//100
print('{} nota(s) de R$ {}'.format(resultado,'100,00'))
valor = valor % 100

resultado = valor // 50
print('{} nota(s) de R$ {}'.format(resultado,'50,00'))
valor = valor % 50

resultado = valor // 20
print('{} nota(s) de R$ {}'.format(resultado,'20,00'))
valor = valor % 20

resultado = valor // 10
print('{} nota(s) de R$ {}'.format(resultado,'10,00'))
valor = valor % 10

resultado = valor // 5
print('{} nota(s) de R$ {:2}'.format(resultado,'5,00'))
valor = valor % 5

resultado = valor // 2
print('{} nota(s) de R$ {:2}'.format(resultado,'2,00'))
valor = valor % 2

resultado = valor // 1
print('{} nota(s) de R$ {:2}'.format(resultado,'1,00'))
valor = valor % 1