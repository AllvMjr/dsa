# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

#Import
import random
from os import system, name

# Função para limar a tela de cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _= system('cls')
        
    # Mac ou Linux
    else:
        _= system('clear')
        
# Função
def game():
    
    limpa_tela()
    
    
    print('\nBem vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo!\n')
    
    #Lista de palavras
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    #Escolhe randomicamente a uma pavra
    palavra = random.choice(palavras)
    
    # na palavra selecionada , preence com undescore
    letras_descobertas = ['_' for letra in palavra]
    
    # Numero de chances
    chances = 6
    
    # Lista para as letras erradas
    letras_erradas = []