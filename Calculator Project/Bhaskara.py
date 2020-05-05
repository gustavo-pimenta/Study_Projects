def main():

    print('CALCULADORA DE EQUAÇÕES DE 2° GRAU'+ '\n\nInsira os termos da equação:')
    
    var = 0
    while (var == 0):
        try:

            a = int(input('\nDigite o Termo A = ')) 
            b = int(input('Digite o Termo B = '))
            c = int(input('Digite o Termo C = '))

            print('\nEQUAÇÃO = ', a, 'X² + ', b,'X + ', c)
        
            delta = (b**2)-(4*a*c)
            print ('\nDelta = ', int(delta))

            if (a == 0):
                print ("O TERMO A NÃO PODE SER ZERO, ISSO É FUNÇÃO DE SEGUNDO GRAU")
            
            else:
            
                if (delta < 0):
                    print ('\nNÃO HÁ RAIZES REAIS'),
                elif (delta == 0):
                    print('\nHÁ 1 RAIZ REAL')  
                    X = (-b + (delta**0.5))/(2*a)           
                    print ('\nRAIZ 1 = ', X)   
                else:
                    print('\nHÁ DUAS RAIZES REAIS') 
                    X1 = (-b + (delta**0.5))/(2*a)
                    X2 = (-b - (delta**0.5))/(2*a)
                    print ('\nRAIZ 1 = ', X1)
                    print ('\nRAIZ 2 = ', X2)

            ask = str(input('\nDeseja Inserir Outra Equação? [DIGITE S/N]: '))
            if (ask == 'N'):
                var+=1

        except ValueError:
            print('\nSOMENTE NÚMEROS SÃO ACEITOS, TENTE NOVAMENTE') 

main()