# Creating a list of integers
colors = ["azul", "amarelo", "vermelho", "verde", "laranja", ]
print(colors[2])
#ages = [10, 20, 30, 40, 50]
#        0  1   2   3   4
# Accessing the list element
#print(ages[0])

# Adding an element to the list
colors.append("turquesa")
print (colors)
#print(ages)

# Modifying an element
#ages[0] = 100
#print(ages)

colors[1] = "dourado"

print(colors)

''' Crie uma lista de strings contendo os nomes de algumas 
cores e imprima a terceira cor da lista.'''

print(".")
print (".")
print ("new exercise")

basictools = ["Screwdriver", "Pliers", "Wrench",
"multimeter", "torque wrench",]
print(basictools)
print(basictools[2])
#troquei os tema tudo rsrsrsrsr

'''Adicione uma nova cor à lista que você criou
 no exercício anterior e, em seguida,
 imprima a lista atualizada.'''

basictools.append("hammer")
print(basictools)

''' Crie uma lista de números inteiros e calcule
 a soma de todos os elementos da lista.'''

numeroInteiro = [12, 29, 36, 48, 77, 45, 128,]
soma_dos_numeros = sum(numeroInteiro)
print(soma_dos_numeros)
#aqui, aprendi sobre a função sum

'''Crie uma lista de frutas e substitua
 a terceira fruta por "Banana"'''

frutas = ["pessego", "mamão", "pera", "uva", "mimosa",]
print(frutas)
frutas.append("abacaxi")
print(frutas)
frutas [2] = "banana"
print(frutas)
#fiz um append ali so pra treinar o comando de cabeça

'''Dada a lista de números: [5, 10, 15, 20, 25], 
multiplique cada número por 2 e imprima a 
lista resultante.'''
#eu nao estou conseguindo fugir do FOR
#vou explicar como eu entendi

#criei a variavel contendo esses numeros
lista = [5, 10, 15, 20, 25,]
print(lista)
#criei uma variavel vazia que vai conter o resultado final
listafinal = []
'''aqui uso o for pelo que eu entendi vai iniciar 
um loop pra percorrer todas as variaveis presentes 
na variavel LISTA'''

for numero in lista:

    ''' pelo que eu entendi eu posso colocar qualquer nome 
nas variaveis que eu tenho na lista, entao cada nomeei 
os numeros, que estao separados por virgulas
de NUMEROS pra facilitar o entendimento, mas poderia colocar
o nome de sei la, saturno... certo?''' 
    listafinal.append(numero* 2)
#aqui entendi que o tab serve pra deixar a linha 
#IDENTADA com o loop FOR
print("resultado da multiplicação")
print(listafinal)
    


