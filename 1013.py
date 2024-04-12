valores = input()
numeros = valores.split()

a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])

maiorAB = int((a + b + abs(a-b)) / 2)

if maiorAB < c:
    print('{} eh o maior'.format(c))
else:
    print('{} eh o maior'.format(maiorAB))