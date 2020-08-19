from sklearn import tree
import pygame
import time
import sys
import random
from random import randint
import csv

# INICIAR E VERIFICAR SE PYGAME ESTA FUNCIONANDO
try:
    pygame.init()
    print("O Pygame foi Inicializado com sucesso!")
except:
    print("O Sistema Apresentou Dificuldade para Inicializar o Pygame, Aguarde...")
    check_errors = pygame.init()
    if check_errors[1] > 0:
        print("Ops, {0} o Pygame iniciou com algum problema..." . format(check_errors[1]))
        sys.exit(-1)
    else:
        print("O Pygame foi inicializado com sucesso!")
    pygame.init()

# CARREGA AS IMAGENS DO JOGO
try:
    background = pygame.image.load('background.png')
    print('\nSucesso ao carregar a imagem background.png')
except:
    print('\nERRO')
    print('Falha ao carregar a background.png')
try:
    X = pygame.image.load('X.png')
    print('\nSucesso ao carregar a imagem X.png')
except:
    print('\nERRO')
    print('Falha ao carregar X.png')
try:
    O = pygame.image.load('O.png')
    print('\nSucesso ao carregar a imagem O.png')
except:
    print('\nERRO')
    print('Falha ao carregar O.png')

# PREDEFINIR CORES
color_list=[]
preto = (0,0,0)
branco = (255,255,255)
cinza = (195,195,195)
vermelho = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
amarelo = (255,255,0)
rosa = (255,15,192)
roxo = (148,0,211)
laranja = (255,127,0)
salmao = (250,127,117)
azul_claro=(173,216,230)
marrom = (150,75,0)
vinho = (94,33,41)

color_list.append(preto)
color_list.append(branco)
color_list.append(vermelho)
color_list.append(azul)
color_list.append(verde)
color_list.append(amarelo)
color_list.append(rosa)
color_list.append(roxo)
color_list.append(laranja)
color_list.append(salmao)
color_list.append(azul_claro)
color_list.append(marrom)
color_list.append(vinho)

# DEFINE INTERFACE GRAFICA
width = 400
height = 480
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe ML")
# pygame.display.set_icon(uni_right)

# INICIALIZA E DEFINE A FONTE DE TEXTO DO JOGO
pygame.font.init()
font_padrao = pygame.font.get_default_font()
fonte50 = pygame.font.SysFont(font_padrao, 50)
fonte20 = pygame.font.SysFont(font_padrao, 20)
fonte100 = pygame.font.SysFont(font_padrao, 100)
fonte30 = pygame.font.SysFont(font_padrao, 30)
fonte70 = pygame.font.SysFont(font_padrao, 70)

def blackout(): # turn the screen black
    blackout = pygame.Surface((400,480))
    blackout.fill(preto)
    screen.blit(blackout,(0,0))
    pygame.display.update()

def board(): # print the buttons and the game board
    screen.blit(background,(0,0))
    pygame.display.update()
    
def cpu_play(): 
    global A,B,C,D,E,F,G,H,I, game_mode, playing

    empty_spaces = []

    if A=='': empty_spaces.append('A')
    if B=='': empty_spaces.append('B')
    if C=='': empty_spaces.append('C')
    if D=='': empty_spaces.append('D')
    if E=='': empty_spaces.append('E')
    if F=='': empty_spaces.append('F')
    if G=='': empty_spaces.append('G')
    if H=='': empty_spaces.append('H')
    if I=='': empty_spaces.append('I')

    if empty_spaces==[]:
        playing=False
    
    if game_mode==1: # ramdom mode
        try:
            play = random.choice(empty_spaces)

            if play=='A': A='O' 
            if play=='B': B='O' 
            if play=='C': C='O' 
            if play=='D': D='O' 
            if play=='E': E='O' 
            if play=='F': F='O' 
            if play=='G': G='O' 
            if play=='H': H='O' 
            if play=='I': I='O' 
        except:
            pass
    
    if game_mode==2: # machine learning mode
        
        board=[]
        if A=='': board.append(0)
        if A=='O': board.append(1)
        if A=='X': board.append(2)
        if B=='': board.append(0)
        if B=='O': board.append(1)
        if B=='X': board.append(2)
        if C=='': board.append(0)
        if C=='O': board.append(1)
        if C=='X': board.append(2)
        if D=='': board.append(0)
        if D=='O': board.append(1)
        if D=='X': board.append(2)
        if E=='': board.append(0)
        if E=='O': board.append(1)
        if E=='X': board.append(2)
        if F=='': board.append(0)
        if F=='O': board.append(1)
        if F=='X': board.append(2)
        if G=='': board.append(0)
        if G=='O': board.append(1)
        if G=='X': board.append(2)
        if H=='': board.append(0)
        if H=='O': board.append(1)
        if H=='X': board.append(2)
        if G=='': board.append(0)
        if G=='O': board.append(1)
        if G=='X': board.append(2)

        play = cpu_guess(board)
        space_empty=True

        try:
            if play=='A':
                if A=='': 
                    A='O'
                else: space_empty=False 
            if play=='B':
                if B=='': 
                    B='O'
                else: space_empty=False 
            if play=='C':
                if C=='': 
                    C='O'
                else: space_empty=False 
            if play=='D':
                if D=='': 
                    D='O' 
                else: space_empty=False
            if play=='E':
                if E=='': 
                    E='O'
                else: space_empty=False     
            if play=='F':
                if F=='': 
                    F='O' 
                else: space_empty=False
            if play=='G':
                if G=='': 
                    G='O' 
                else: space_empty=False
            if play=='H':
                if H=='': 
                    H='O' 
                else: space_empty=False
            if play=='I':
                if I=='': 
                    I='O' 
                else: space_empty=False
        except:
            pass

        if space_empty==False:

            try:
                play = random.choice(empty_spaces)

                if play=='A': A='O' 
                if play=='B': B='O' 
                if play=='C': C='O' 
                if play=='D': D='O' 
                if play=='E': E='O' 
                if play=='F': F='O' 
                if play=='G': G='O' 
                if play=='H': H='O' 
                if play=='I': I='O' 
            except:
                pass


def check(): # check wich marked places with X and O and print then 
    global A,B,C,D,E,F,G,H,I,O,X

    if A=='X':
        screen.blit(X,(20,20))
    elif A=='O':
        screen.blit(O,(20,20))
    if B=='X':
        screen.blit(X,(160,20))
    elif B=='O':
        screen.blit(O,(160,20))
    if C=='X':
        screen.blit(X,(300,20))
    elif C=='O':
        screen.blit(O,(300,20))
    if D=='X':
        screen.blit(X,(20,160))
    elif D=='O':
        screen.blit(O,(20,160))
    if E=='X':
        screen.blit(X,(160,160))
    elif E=='O':
        screen.blit(O,(160,160))
    if F=='X':
        screen.blit(X,(300,160))
    elif F=='O':
        screen.blit(O,(300,160))
    if G=='X':
        screen.blit(X,(20,300))
    elif G=='O':
        screen.blit(O,(20,300))
    if H=='X':
        screen.blit(X,(160,300))
    elif H=='O':
        screen.blit(O,(160,300))
    if I=='X':
        screen.blit(X,(300,300))
    elif I=='O':
        screen.blit(O,(300,300))

    pygame.display.update()

def event_reader():

    global A,B,C,D,E,F,G,H,I, playing, turno

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_on=False
                playing=False
                pygame.quit() 
                sys.exit(0)
            
            if turno==0:
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = pygame.mouse.get_pos()
                    
                    if 0<click_y<399:
                        
                        if click_x<130:
                            if click_y<130:
                                if A=='':
                                    A='X'
                                    turno=1
                            elif 130<click_y<260:
                                if D=='':
                                    D='X'
                                    turno=1
                            elif 260<click_y<400:
                                if G=='':
                                    G='X'
                                    turno=1
                        if 130<click_x<263:
                            if click_y<130:
                                if B=='':
                                    B='X'
                                    turno=1
                            elif 130<click_y<260:
                                if E=='':
                                    E='X'
                                    turno=1
                            elif 260<click_y<400:
                                if H=='':
                                    H='X'
                                    turno=1
                        if 265<click_x<400:
                            if click_y<130:
                                if C=='':
                                    C='X'
                                    turno=1
                            elif 130<click_y<260:
                                if F=='':
                                    F='X'
                                    turno=1
                            elif 260<click_y<400:
                                if I=='':
                                    I='X'
                                    turno=1

            if turno==1:
                turno=0
                
                cpu_play()
                blackout()
                board()
                check()
                
                print_game_mode()
                
                

def winner_check(): # check who won the game and print 
    global A,B,C,D,E,F,G,H,I, winner, playing

    if A!='' and (A==B and A==C or A==D and A==G or A==E and A==I):
        winner=A
        text = fonte30.render(winner, 1, preto)
        screen.blit(text, (225,413))
        pygame.display.update()
        playing=False
        
    if C!='' and (C==E and C==G or C==F and C==I):
        winner=C
        text = fonte30.render(winner, 1, preto)
        screen.blit(text, (225,413))
        pygame.display.update()
        playing=False
    if H!='' and (H==G and H==I or H==E and B==H):
        winner=H
        text = fonte30.render(winner, 1, preto)
        screen.blit(text, (225,413))
        pygame.display.update()
        playing=False
    if D!='' and (D==E and D==F):
        winner=D
        text = fonte30.render(winner, 1, preto)
        screen.blit(text, (225,413))
        pygame.display.update()
        playing=False
        
def reload_game(): # reload the game and read the "game mode" button
    global playing, game_mode
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_on=False
                playing=False
                pygame.quit() 
                sys.exit(0)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_x, click_y = pygame.mouse.get_pos()

                if (5<click_x<138) and (408<click_y<435):
                    playing=True
                    blackout()
                    board()
                    print_game_mode()

                if (5<click_x<138) and (444<click_y<471):
                    if game_mode==1: game_mode=2
                    elif game_mode==2: game_mode=1
                    print_game_mode()

def print_game_mode():
    global game_mode

    erase = pygame.Surface((85,25))
    erase.fill(cinza)
    screen.blit(erase,(55,445))
    if game_mode==1: 
        text = fonte30.render('Random', 1, preto)
        screen.blit(text, (57,450))
    elif game_mode==2:
        text = fonte30.render('ML', 1, preto)
        screen.blit(text, (65,450))

    pygame.display.update()

def limpar(text): # removes unnecessary characters
    text = str(text)
    text = text.replace("\n",'')
    text = text.replace('"' , '')
    text = text.replace('[' , '')
    text = text.replace(']' , '')
    text = text.replace(' ' , '')
    text = text.replace("'" , '')
    text = text.replace("," , '')
    return text

def cpu_guess(spaces): # ML to preview moves
    features = [] # amostras
    labels = [] # legenda das amostras

    with open(r'feature.csv', 'r') as csv_file: # open csv
        csv_info = list(csv.reader(csv_file, delimiter='\n')) # read csv info
        for line in csv_info:
            x=str(line)
            x=list(limpar(x))
            features.append(x)
    csv_file.close()
    
    with open(r'label.csv', 'r') as csv_file: # open csv
        csv_info = list(csv.reader(csv_file, delimiter='\n')) # read csv info
        for line in csv_info:
            text=str(line)
            text=limpar(text)
            labels.append(text)
    csv_file.close()

    # o classificador encontra padrões nos dados de treinamento
    clf = tree.DecisionTreeClassifier() # instância do classificador
    clf = clf.fit(features, labels) # fit encontra padrões nos dados

    # previsão
    ans = (clf.predict([spaces]))
    ans = limpar(str(ans))
    return ans

game_on = True
playing = True
game_mode=2
blackout()
board()
print_game_mode()
while game_on:

    turno=randint(0,1)
    winner=''
    A=''
    B=''
    C=''
    D=''
    E=''
    F=''
    G=''
    H=''
    I=''
    
    while playing:

        event_reader()
        winner_check()
        
    
    reload_game()

pygame.quit() 
sys.exit(0)