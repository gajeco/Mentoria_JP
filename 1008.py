employee = int(input('Número do funiconário: '))
hours = int(input('horas trabalhadas: '))
receive = float(input('Recebe por hora trabalhada: R$ '))

print('NUMBER = {} \nSALARY = U$ {:.2f}'.format(employee, hours * receive))