'''
Verificação de Maior Número:
Peça ao usuário para inserir dois números e 
escreva um programa para verificar qual é o 
maior número e imprimir na tela.
'''

#solicita o imput dos usuarios
number1 = input("insert the first number:")
number2 = input("insert the second number:")

#converte a entrada para numeros
number1 = float (number1)
number2 = float (number2)

#compara os numeros e imprime o maior
if number1 > number2:
    print( number1, "is grater than", number2)
elif number2 > number1:
    print( number2, "is grater than", number1)
else:
    print("the number are identical")



'''
Classificação de Idade:
Solicite ao usuário que insira sua idade e,
 em seguida, 
escreva um programa para classificar a idade e<


como criança, adolescente, adulto, etc.
'''
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("ghost")
elif idade >= 0 and idade <= 13:
    print("Criança")
elif idade > 13 and idade <= 20:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
elif idade >= 65 and idade < 100:
    print("idoso")
elif idade == 100:
    print("ya esta")
else: 
    print("matusalem")



'''
Verificação de Número Positivo ou Negativo:
Peça ao usuário para inserir um número
 e escreva um programa para verificar
 se o número é positivo, negativo ou zero.
'''
years = int(input("qual a sua idade?"))
if years > 0:
    print("positivo")
elif years < 0:
    print("negativo")
else:
    print("zero")



'''
Verificação de Número Primo:
Peça ao usuário para inserir um número 
e escreva um programa para verificar 
se o número é primo ou não.


Claro, aqui está um algoritmo passo a passo
 para encontrar números primos sem código:

1. **Escolha um número**: Comece com um 
número natural maior que 1, pois os 
números primos começam a partir de 2.

2. **Verifique se é divisível**: Verifique
 se o número escolhido é divisível por 
 qualquer número natural entre 2 e a raiz 
 quadrada do próprio número. Se for divisível 
 por algum desses números, então não é primo.

3. **Itere para o próximo número**: Se 
o número passado no passo 2 for divisível por
 algum número entre 2 e a raiz quadrada do próprio número,
  passe para o próximo número e repita o passo 2.

4. **Repita até encontrar um primo**: Continue
 repetindo os passos 2 e 3 até encontrar um número
  que não seja divisível por nenhum outro número 
  além de 1 e ele mesmo. Esse número é um número primo.

Por exemplo, para encontrar o próximo número primo após 2:
- Começamos com 3.
- Verificamos se é divisível por 2. Não é.
- Avançamos para 4 (pois 3 é ímpar e o próximo número ímpar é 5).
- Verificamos se 5 é divisível por 2 ou 3. Não é.
- Assim, 5 é um número primo.

Esse é um método básico para encontrar 
números primos sem utilizar código.
'''
def primo(n):
    for val in range(2, int(n**0.5)+1):
        if n % val == 0:
            return False
    return True

numero = int(input("digite um numemero"))
if primo(numero) :
    print(f"{numero} é um primo.")
else:
    print(f"{numero} não é um primo.")


'''
Calculadora Simples:
Escreva um programa que solicite ao usuário
 que insira dois números e uma operação 
 (adição, subtração, multiplicação ou divisão) 
 e, em seguida, execute a operação selecionada.
'''

valor1 = float(input("para calcular digite um numero "))
valor2 = float(input("para calcular digite mais um numero "))
operador = input("selecione um operador valido: adição (+), subtração (-), divisão (/), multiplicação (*) " )

if operador == "+":
    resultado = valor1 + valor2 
    print("resultado ", round(resultado))
elif operador == "-":
    resultado = valor1 - valor2
    print("resultado ", round(resultado))
elif operador == "/":
    resultado = valor1 / valor2
    print("resultado ", round(resultado))
elif operador == "*":
    resultado = valor1 * valor2
    print("resultado ", round(resultado))
else:
    print("operador não é valido")
#esse aqui eu fiz com as vozes cabeça da minha!


'''
Conversor de Unidades:
Crie um programa que peça ao usuário para 
inserir uma medida em metros e ofereça opções
 para converter essa medida em centímetros, 
 quilômetros ou milhas.
'''
#aqui eu pesso pro usuario escolher a medida e a unidade de metragem
metro = float(input("insira uma medida em metros "))
unidade = input("escolha a unidade para conversão, (centimetros (cm), quilometros (km) ou milhas (mi)) " )

#criei a variavel medida pra armazenar os resultados
if unidade == "cm":
    medida = metro * 100
    print ("medida é igual a ", medida)


elif unidade == "km":
    medida = metro / 1000
    print("medida é igual a ", medida)

elif unidade == "mi":
    medida = metro / 1609.344
    print("medida é igual a ", medida)

else:
    print ("incomensuravel")

""" eu queria fazer mais completo com mas preciso de mais conhecimento, pq vejo um monte de coisa
pra deixar perfeito, mas ainda nao sei como fazer, por exemplo, antecipar 
uns bugs com mais if e elses e incluir uns loops"""
#...

'''
Verificação de Triângulo:
Solicite ao usuário que insira os comprimentos 
dos três lados de um triângulo e escreva um 
programa para verificar se é um triângulo válido
 (ou seja, se a soma de quaisquer dois lados é maior que o terceiro lado).
'''

A = float(input("medida do lado A ", ))
B = float(input("medida do lado B ", ))
C = float(input("medida do lado C ", ))

if A + B < C:
    tamanho = A + B
    print("não é um triangulo! " )

elif A + C < B:
    tamanho = A + C 
    print("não é um triangulo! " )

elif B + C < A:
    tamanho = B + C 
    print("não é um triangulo! " )

 #...   

elif A + B > C and A != B != C:
    tamanho = A + B
    print("triangulo escaleno ")

elif A + B > C and A == B != C:
    tamanho = A + B 
    print("triangulo isósceles")

elif A + B > C and A!= B == C:
    tamanho = A + B
    print("triangulo isósceles ") 

elif A + B > C and A == B == C:
    tamanho = A + B
    print("triangulo equilatero ") 

#...

elif A + C > B and A != B != C:
    tamanho = A + C
    print("triangulo escaleno ")

elif A + C > B and A == B != C:
    tamanho = A + C 
    print("triangulo isósceles")

elif A + C > B and A!= B == C:
    tamanho = A + C
    print("triangulo isósceles ") 

elif A + C > B and A == B == C:
    tamanho = A + C
    print("triangulo equilatero ") 

#...
elif B + C > A and A != B != C:
    tamanho = B + C
    print("triangulo escaleno ")

elif B + C > A and A == B != C:
    tamanho = B + C 
    print("triangulo isósceles")

elif B + C > A and A!= B == C:
    tamanho = B + C
    print("triangulo isósceles ") 

elif B + C > A and A == B == C:
    tamanho = B + C
    print("triangulo equilatero ") 

else: 
    print("não é valido")

# esse foi o mais massa!
#quando eu souber simplificar, vou fazer um com adicional dos angulos
#vozes cabeça da minha tambem

#...


"""Jogo de Adivinhação:
Crie um programa que gere um número aleatório e 
peça ao usuário para adivinhá-lo. O programa deve
 fornecer dicas (maior, menor) até que o usuário
  adivinhe corretamente."""

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while True:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Maior! Tente novamente.")
        elif palpite > numero_secreto:
            print("Menor! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            break

jogo_adivinhacao()


"""Verificação de Vogal ou Consoante:
Peça ao usuário para inserir uma letra e
 escreva um programa para verificar se é 
 uma vogal ou uma consoante."""

letra = input("digite uma letra " )
vogais = ["a", "e", "i", "o", "u",]

if letra in vogais:
    print("a letra " + letra + " é uma vogal")
else:
    print("a letra " + letra + " é uma consoante")
#aqui tambem faltam ifs, mas ficaria mais interessante com comandos
#especificos que eu nao sei ainda

'''
Validação de Nome de Usuário:
Peça ao usuário para inserir um nome de 
usuário e verifique se ele atende aos 
critérios de validade (por exemplo, 
deve ter pelo menos 6 caracteres e conter apenas letras e números).
'''

def validar_nome_usuario(nome_usuario):
    if len(nome_usuario) < 6:
        return False
    if len(nome_usuario) > 12:
        return False
    for caractere in nome_usuario:
        if not (caractere.isalpha() or caractere.isdigit()):
            return False
    return True
nome = input("digite o nome do usuario, contendo 6 caracteres entre eles letras e numeros ")
if validar_nome_usuario(nome):
    print("nome do usuario valido ")
else:
    print("nome do usuario invalido, deve ter pelo menos 6 caracteres e conter apenas letras e numeros ")

#esse eu fiz com a juda, mas anotei o passo a passo e aprendi umas funçoes e comandos diferentes
#adorei fazer esses exercicios :D
