from modulos import Jogador as jgr
from modulos import Placar as plc

def Jogar():
    jogador1 = jgr.Jogador(input("Digite o nome do jogador 1: "))
    jogador2 = jgr.Jogador('Computador') 

    p = plc.Placar()
    p.jogadores = jogador1.nome
    p.jogadores = jogador2.nome
      
    while(p.jogadores[0]['placar'] < 3 and p.jogadores[1]['placar'] < 3):
        jogada1, jogada2 = jogador1.set_jogada(),jogador2.jogar()
        p.iniciarPartida(jogada1, jogada2)
    p.anunciarVencedor()

Jogar()
