#'''-----------------------------------------------------------------------------
# LISTA DE EXERCICIOS – PARADIGMAS E LINGUAGEM DE PROGRAMAÇÃO – 2020/2
# CURSO: Engenharia Computação – CAMPUS: Bacelar
# PROFESSOR: Vinicius Heltai - DATA: outubro/2020
# ALUNO: Gustavo Silva Pimenta RA: D6251F-0 – SEMESTRE: 6º Semestre
# ENUNCIADO: 04 – Desenvolva um programa que receba nome e salário de um funcionário 
# e calcule o valor do salário líquido desse funcionário, utilizando função, descontando 
# os impostos INSS e Imposto de Renda (IR) conforme tabela oficial vigente. 
# (utilizar laço de repetição com opção de saída do sistema).
#-----------------------------------------------------------------------------
#'''

while True:
    nome = input("Entre com o nome do funcionario: ")
    salarioBruto = float (input("Entre com o salario bruto [R$]: "))

    #DESCONTO DO IRRF:

    if (salarioBruto <= 1903.98):
        taxaIR = 0.0
        descontoIR = 0.00
    if (salarioBruto >= 1903.99 and salarioBruto <= 2826.65):
        taxaIR = 7.5
        descontoIR = 142.80
    if (salarioBruto >= 2826.66 and salarioBruto <= 3751.05):
        taxaIR = 15.0
        descontoIR = 354.80
    if (salarioBruto >= 3751.06 and salarioBruto <= 4664.68):
        taxaIR = 22.5
        descontoIR = 636.13
    if (salarioBruto > 4664.68):
        taxaIR = 27.5
        descontoIR = 869.36

    # DESCONTO DO INSS:
    if (salarioBruto <= 1045.00):
        descontoINSS = salarioBruto*7.5/100

    elif (salarioBruto >= 1045.01 and salarioBruto <= 2089.60):
        descontoINSS1 = 1045.00*7.5/100
        descontoINSS2 = (salarioBruto-1045.00)*9.0/100
        descontoINSS = descontoINSS1 + descontoINSS2

    elif (salarioBruto >= 2089.61 and salarioBruto <= 3134.40):
        descontoINSS1 = 1045.00*7.5/100
        descontoINSS2 = 1044.60*9.0/100
        descontoINSS3 = (salarioBruto-1045.00-1044.60)*12/100
        descontoINSS = descontoINSS1 + descontoINSS2 + descontoINSS3

    elif (salarioBruto >= 3134.41 and salarioBruto <= 6101.06):
        descontoINSS1 = 1045.00*7.5/100
        descontoINSS2 = 1044.60*9.0/100
        descontoINSS3 = 1044.80*12.0/100
        descontoINSS4 = (salarioBruto-1045.00-1044.60-1044.80)*14/100
        descontoINSS = descontoINSS1 + descontoINSS2 + descontoINSS3 + descontoINSS4

    elif (salarioBruto > 6101.06):
        descontoINSS1 = 1045.00*7.5/100
        descontoINSS2 = 1044.60*9.0/100
        descontoINSS3 = 1044.80*12.0/100
        descontoINSS4 = 2966.66*14/100
        descontoINSS = descontoINSS1 + descontoINSS2 + descontoINSS3 + descontoINSS4

    salarioLiquido = salarioBruto - descontoINSS - descontoIR
    totalDescontos = descontoINSS + descontoIR

    print (f"Salario Bruto : R$ {salarioBruto:5.2f}")
    print (f"Desconto de INSS : R$ {descontoINSS:5.2f}")
    print (f"Desconto de IRRF : R$ {descontoIR:5.2f} - {taxaIR:.1f}%")
    print (f"Total de descontos : R$ {totalDescontos:.2f}")
    print (f"Salario Liquido : RS {salarioLiquido:5.2f}")

    sair = input("Deseja sair: S para sim ou qualquer tecla para continuar: ")
    if (sair == "S" or sair == "s"):
        break





    
 
