#'''-----------------------------------------------------------------------------
# LISTA DE EXERCICIOS – PARADIGMAS E LINGUAGEM DE PROGRAMAÇÃO – 2020/2
# CURSO: Engenharia Computação – CAMPUS: Bacelar
# PROFESSOR: Vinicius Heltai - DATA: outubro/2020
# ALUNO: Gustavo Silva Pimenta RA: D6251F-0 – SEMESTRE: 6º Semestre
# ENUNCIADO: 03 – Desenvolva um programa que receba nome, idade e salário digitados 
# pelo usuário e apresente no final quantas dessas idades estão entre 15 e 17 anos, 
# quantas são maiores de 21 anos, quantos salários estão entre R$1.500,00 e 
# R$2.000,00, quantos estão acima de R$3.500,00 e qual é o maior e o menor salário 
# digitado. (utilizar laço de repetição com opção de saída do sistema).
#-----------------------------------------------------------------------------
#'''

class Pessoa: # classe que define o objeto pessoa

    # recebe e define as informações
    def __init__(self, nome, idade, sal): 

        self.nome = nome 
        self.idade = idade 
        self.sal= sal

        def setNome(self, nome): 
            self.nome = nome 

        def setIdade(self, idade): 
            self.idade = idade 

        def setSalario(self, sal): 
            self.sal = sal

        def getNome(self): 
            return self.nome 

        def getIdade(self): 
            return self.idade
        
        def getSalario(self): 
            return self.sal

pessoas =[] # lista de pessoas inicialmente vazia

while True:

    opt = int(input('[1] Inserir uma Pessoa\n[2] Terminado\nENTRE COM UM VALOR: '))

    if (opt==1):
        nome = input('Insira o nome: ')
        idade = input('Insira a idade: ')
        sal = input('Insira o salario: ')

        # cria um objeto Pessoa e insere na lista pessoas
        pessoas.append(Pessoa(nome, idade, sal)) 

    elif (opt==2):
        break

    else:
        pass

idades_selecionadas = [] # idades entre 15 e 17 anos
maiores = [] # maiores de 21 anos

for i in pessoas: # le todas as pessoas da lista

    idade = int(i.idade)  # le todas as idades 

    if (15 <= idade <= 17): 
        idades_selecionadas.append(idade)
    if (21 <= idade): 
        maiores.append(idade)

print('Foram encontradas', len(idades_selecionadas), 'idades entre 15 e 17 anos.')
print('Foram encontradas', len(maiores), 'idades maiores de 21 anos.')

salarios_selecionados = [] # salarios entre R$1.500,00 e R$2.000,00
salario_acima_3500 = [] # salarios acima de R$3.500,00
maior_sal = 0 # maior salario
menor_sal = 0 # menor salario

for i in pessoas: # le todas as pessoas da lista

    sal = int(i.sal)  # le todos os salarios

    if (1500 <= sal <= 2000): 
        salarios_selecionados.append(sal)
    if (3500 <= sal): 
        salario_acima_3500.append(sal)
    if (sal > maior_sal):
        maior_sal = sal
    if (sal < menor_sal):
        menor_sal = sal
    if (menor_sal == 0):
        menor_sal = sal
    
print('Foram encontrados', len(salarios_selecionados), 'salarios entre R$1.500,00 e R$2.000,00.')
print('Foram encontrados', len(salario_acima_3500), 'salarios acima de R$3.500,00.')
print('O maior salario encontrado foi: ', maior_sal)
print('O menor salario encontrado foi: ', menor_sal)
