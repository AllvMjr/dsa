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
        
# Função para desenho da forca
def display_hangman(chences):
    
    # Lista de Estagios da forca
    stages = [ # Estagio 6 (final)
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
              """,
              # Estagio 5
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
              """,
              # Estagio 4
              """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
              """,
              # Estagio 3
              """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
              """,
              # Estagio 2
              """
                --------
                |      |
                |      O
                |      |
                |
                |
                -
              """,
              # Estagio 1
              """
                --------
                |      |
                |      O
                |      
                |
                |
                -
              """,
              # Estagio 0
              """
                --------
                |      |
                |
                |
                |
                |
                -
              """        
    ]

        
# Função
def game():
    
    limpa_tela()
    
    
    print('\nBem vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo!\n')
    
    #Lista de palavras
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    #Escolhe randomicamente a uma pavra
    palavra = random.choice(palavras)
    
    # Lista de Letras da palavra
    lista_letras_palavras = [letra for letra in palavra]
    
    # Cria tabuleiro com o cartacter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)
    
    # Número de Chances
    chances = 6
    
    # Lista para as letras digitadas
    letras_tentativas = []
    
    # Loop enquanto o número de chances for maior que 0
    while chances > 0:
        print(display_hangman)
        print("Palavra: ", tabuleiro)
        print('\n')
        
        # Tentativa
        tentativa = input('\nDigite uma letra: ')
        
        #Condicional
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue
    
        # Lista de tentativas letras
        letras_tentativas.append(tentativa)
        
        #Condicional
        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")
            
            #loop
            for indice in range(len(lista_letras_palavras)):
                #conficional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa