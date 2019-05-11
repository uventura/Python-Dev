'''------------------|         INFLAÇÃO         |---------------------
Regras:
    Dado um valor inicial v0, diz-se que ocorre inflação quando ao passar
do tempo há um aumento desse valor, e deflação um descrecimento.
    Práticas de uso:
       => Variação Percentual:
            Sabendo que ocorreu uma inflação de v0, tornando-se v1, quanto foi essa
        inflação em porcentagem?
            v0 -------- 1(ou 100%, mas operar com 1 facilita)
            v1-v0 -------- j1(porcentagem da inflação)
            j1 = v1-v0/v0
            j1 = v1/v0 - v0/v0
            [ j1 = v1/v0 - 1 ]---> Regra que representa a variação percentual
            Não vou obter em porcentagem mesmo, mas basta multiplicar por 100.
            
        => Multiplas Variações Percentuais:
            Sabendo que ocorreram 5 inflações sucessivas de v0, de que maneira ocorre?
                Entendendo como se define uma única variação percentual é possível determinar
            várias, basta ter o valor inicial, se o que ocorre é:
                    v0 -> v1 -> v2 -> v3 -> v4 -> v5
                O que poderia ser obtido é o valor obtido durante uma inflação; modo:
                    j2 = v2/v1 - 1
                    Mas:
                    j1 = v1/v0 - 1
                    v1 = v0(j1+1)
                    Então:
                    j2 = v2/v0(j1+1) - 1
                    v2 = v0(j1+1)(j2+1)

                    Caso seja v3:
                    v3 = v0(j1+1)(j2+1)(j3+1)

                    Ou seja:
                        --[ Vn = V0(j1+1)(j2+1)(j3+1)...(jn+1) ]--
            É possivel determinar a porcentagem de variação do estado final para o estado inicial, ou seja:
                    [ jn = Vn/V0 - 1 ] (O quanto que variou percentualmente do estado inicial pro final)
                    jn = V0(j1+1)(j2+1)(j3+1)...(jn+1)/V0 - 1
                    [jn = (j1+1)(j2+1)(j3+1)...(jn+1) - 1 ] ---> Outra forma utilizando sucessivos percentuais de mudança
'''

print('Regras:\n')
print('Quando indicar a quantidade de itens, dê um número natural. Quando indicar um valor\n\
pode ser escrito um número inteiro positivo ou um número decimal(adotando o . como separaçao das\n\
casas decimais).\n')
print('-'*50)

nItens = int(input("Número de itens: "))
c = 0
listItens = []
valor = 0
while c<nItens:
    listItens.append([])
    listItens[c].append(float(input("Valor Inicial do item("+str(c+1)+"): ")))
    valor+=listItens[c][0]
    c+=1

print('[ Inicial ]: A somatória dos valores iniciais é '+str(valor)+'\n')

nVar = int(input('Quantas variações de preços serão observadas dos itens? '))
c1 = 0
c2 = 0
listVar = []
while c1<nItens:
    listVar.append([])
    print('\nVariações do item '+str(c1+1)+': ')
    while c2<nVar:
        listItens[c1].append(float(input('  {}° variação: '.format(c2+1,c1+1))))
        listVar[c1].append('{:.2f}'.format((listItens[c1][c2+1]/listItens[c1][c2])-1))
        c2+=1  
    c2=0
    c1+=1

#Variações Percentuais
print('-'*50+'\nCaso a variação seja negativa, então é chamado de deflação.')
a = 0
b = 0
while a<nItens:
    print('\n=> Variações percentuais do {}° item: '.format(a+1))
    while b<len(listVar[a]):
        print('  {}° Variação = {:.2f}%'.format(b+1,float(listVar[a][b])*100))
        b+=1
    b = 0
    a+=1
