def calculadora (pnum, snum, operacao):
   
    if (operacao == 1):
        return pnum + snum
    elif (operacao == 2):
        return pnum - snum
    elif (operacao == 3):
        return pnum * snum
    elif (operacao == 4):
        return pnum / snum
    else:
        return 0
    
executar = True
while (executar == True):
        print("Escolha o tipo de operação que deseja fazer, sendo 1 = soma, 2 = subitração 3 = multiplicação e 4 = divisão ou 0 para sair")
        operacao = int(input())
        if(operacao< 0) or (operacao > 4):
             print("Essa não é uma opção valida")
        elif(operacao == 0):
             executar = False
        else:
            print("Escolha o primeiro número")
            pnum = int(input())
            print("Escolha o segundo número")
            snum = int(input())
        
       
        

            resultado = calculadora(pnum, snum, operacao)    
            print("o Resultado é " + resultado)