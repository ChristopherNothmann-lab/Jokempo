class Placar():   
    '''    
    Placar é um reponsável por instaciar o objeto que controlará as regras e os pontos do jogo.
    
    Esse módulo também  será responsável por iniciar a partida e anunciar o vencedor.
    '''
    def __init__(self):
        self._jogadores = []
        self._regras = [    
                  {'jogada':'Pedra', 'contra':'Papel', 'pontua':0},
                  {'jogada':'Pedra', 'contra':'Tesoura', 'pontua':1},
                  {'jogada':'Papel', 'contra':'Pedra', 'pontua':1},
                  {'jogada':'Papel', 'contra':'Tesoura', 'pontua':0},
                  {'jogada':'Tesoura', 'contra':'Papel', 'pontua':1},
                  {'jogada':'Tesoura', 'contra':'Pedra', 'pontua':0}
                 ]

    def get_jogadores(self):
        return self._jogadores
    
    def set_jogadores(self, value):
        if (len(self._jogadores) < 2 ):
            jogador = {'nome':str(value),'placar': 0}
            self._jogadores.append(jogador)
            
    jogadores = property(get_jogadores, set_jogadores)    
    
    
    def iniciarPartida(self,jogada1, jogada2):
        print("\n ({0}) {1} x {2} ({3})".format(self._jogadores[0]['nome']
                                             , jogada1
                                             , jogada2
                                             , self._jogadores[1]['nome']))
        if(jogada1 == jogada2):
            print ('Empate - ninguém pontua \n')
        else:
            jogador1pontua = next(item['pontua'] for item in self._regras 
                                  if item['jogada'] == jogada1 and item['contra'] == jogada2)
            
            if jogador1pontua == 1:
                 pontuador = 0 
            else:
                pontuador = 1
            
            self._jogadores[pontuador]['placar'] += 1        
            print (f'Ponto para {self._jogadores[pontuador]["nome"]} \n')
            
    def anunciarVencedor(self):
        vencedor = next(item['nome'] for item in self._jogadores if item['placar'] == 3)
        if(vencedor != 'none'):
            print('Placar {0} - {1} x {2} - {3}  \n O vencedor é \033[32m{4}\033[0m \n'
                  .format(self._jogadores[0]["nome"],
                          self._jogadores[0]["placar"],
                          self._jogadores[1]["nome"],
                          self._jogadores[1]["placar"],
                          vencedor))
