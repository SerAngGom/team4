# Creo las variables ik y m

ik = float(input('Indicame el interés nominal: '))

m = int(input('Indicame los meses: '))

k = 0
mk= 0
tae = 0
#Programa principal

k = 12/m

mk = 1+(ik/(100*k))

tae= 100*(mk**k-1)

#imprimo el resultado

print('El TAE calculado es: {:.2f}%'.format(tae))








              
