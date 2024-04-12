numero_inteiro = int(input())
hora = 0
minutos = 0
segundos = 0

hora = numero_inteiro // 3600
 
min = (numero_inteiro / 60) % 60

segundos = numero_inteiro % 60  

print('{}:{}:{}'.format(int(hora), int(min), segundos))