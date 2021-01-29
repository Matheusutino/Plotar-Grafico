'''
    Autor : Matheus Yasuo Ribeiro Utino

    Esse programa tem como objetivo plotar um função e exibi-la, com opção de salvar a imagem, ele é bem simples e novo parâmetros poderiam ser utilizados,todavia
    como seria para casos mais específicos ou apenas questão de customização descidi não implementar.
    Bons estudos a todos!!!
'''

import matplotlib.pyplot as plt
import numpy

#Altere apenas essas variáveis
LIMITE_INFERIOR = -1000
LIMITE_SUPERIOR = 1000
PASSO = 1
#Caso deseje não colocar algum desses parâmetros apenas deixe apenas ""
TITULO = "Gráfico"
LABEL_X = "Eixo x"
LABEL_Y = "Eixo Y"

def function(x): #Função que o usuário deseja plotar
    return x*x*x

def main():
    x = numpy.arange(LIMITE_INFERIOR,LIMITE_SUPERIOR,PASSO) #Criando um array no intervalo [LIMITE_SUPERIOR,LIMITE_SUPERIOR] indo ao ritmo do passo
    plt.plot(x,function(x)); #Função para criar o gráfico
    plt.title(TITULO) #Declarando um título ao gráfico
    plt.xlabel(LABEL_X, size=16) #Declarando um título para a label do eixo x
    plt.ylabel(LABEL_Y, size=16) #Declarando um título para a label do eixo y
    plt.show() #Exibindo o gráfico


if __name__ == '__main__':
    main()

