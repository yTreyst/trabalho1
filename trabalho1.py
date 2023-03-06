nome = input('Digite seu nome: ')
sobrenome =input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')
altura =input('Digite sua altura: ')
peso = input('Digite seu peso: ')

print("nome: ", nome)
print("sobrenome: ", sobrenome)
print("idade: ", idade)
print("altura: ", altura)
print("peso: ", peso)

if int(idade) >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')