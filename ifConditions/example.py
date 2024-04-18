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
Peça ao usuário para inserir um número e escreva um programa para verificar se o número é primo ou não.


Claro, aqui está um algoritmo passo a passo para encontrar números primos sem código:

1. **Escolha um número**: Comece com um número natural maior que 1, pois os números primos começam a partir de 2.

2. **Verifique se é divisível**: Verifique se o número escolhido é divisível por qualquer número natural entre 2 e a raiz quadrada do próprio número. Se for divisível por algum desses números, então não é primo.

3. **Itere para o próximo número**: Se o número passado no passo 2 for divisível por algum número entre 2 e a raiz quadrada do próprio número, passe para o próximo número e repita o passo 2.

4. **Repita até encontrar um primo**: Continue repetindo os passos 2 e 3 até encontrar um número que não seja divisível por nenhum outro número além de 1 e ele mesmo. Esse número é um número primo.

Por exemplo, para encontrar o próximo número primo após 2:
- Começamos com 3.
- Verificamos se é divisível por 2. Não é.
- Avançamos para 4 (pois 3 é ímpar e o próximo número ímpar é 5).
- Verificamos se 5 é divisível por 2 ou 3. Não é.
- Assim, 5 é um número primo.

Esse é um método básico para encontrar números primos sem utilizar código.
'''
'''
Calculadora Simples:
Escreva um programa que solicite ao usuário que insira dois números e uma operação (adição, subtração, multiplicação ou divisão) e, em seguida, execute a operação selecionada.
'''
'''
Conversor de Unidades:
Crie um programa que peça ao usuário para inserir uma medida em metros e ofereça opções para converter essa medida em centímetros, quilômetros ou milhas.
'''
'''
Verificação de Triângulo:
Solicite ao usuário que insira os comprimentos dos três lados de um triângulo e escreva um programa para verificar se é um triângulo válido (ou seja, se a soma de quaisquer dois lados é maior que o terceiro lado).
'''
'''
Jogo de Adivinhação:
Crie um programa que gere um número aleatório e peça ao usuário para adivinhá-lo. O programa deve fornecer dicas (maior, menor) até que o usuário adivinhe corretamente.
'''

'''
Verificação de Vogal ou Consoante:
Peça ao usuário para inserir uma letra e escreva um programa para verificar se é uma vogal ou uma consoante.
'''
'''
Validação de Nome de Usuário:
Peça ao usuário para inserir um nome de usuário e verifique se ele atende aos critérios de validade (por exemplo, deve ter pelo menos 6 caracteres e conter apenas letras e números).
'''
