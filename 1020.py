idade = int(input())
mes = 0

anos = idade // 365
print('{} ano(s)'.format(anos))

if idade // 365 == 0:
    mes = idade / 30
    print('{} mes(es)'.format(int(mes)))
else:
    mes = (idade % 365) // 30
    mes = print('{} mes(es)'.format(mes))

dias = (idade % 365) % 30
print('{} dia(s)'.format(dias))