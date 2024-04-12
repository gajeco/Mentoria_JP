valoresx1 = input()
valoresy2 = input()

numerosx1 = valoresx1.split()
numerosy2 = valoresy2.split()

x1 = float(numerosx1[0])
y1 = float(numerosx1[1])

x2 = float(numerosy2[0])
y2 = float(numerosy2[1])

raiz = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
raiz = raiz ** (1/2)
print('{:.4f}'.format(raiz))


