valores = input()
numeros = valores.split()

a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])

delta = b**2 - 4 * (a * c) 

print(a)
print(b)
print(c)

if delta <= 0.0 or a == 0.0:
    print('Impossivel calcular')
    exit
else:
    raiz_delta = delta ** (1/2)
    r1 = (-b + raiz_delta) / ( 2 * a )
    r2 = (-b - raiz_delta) / ( 2 * a )
    print('R1 = {}\nR2 = {}'.format(r1, r2))