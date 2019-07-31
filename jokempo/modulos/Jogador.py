import random 

class Jogador():  
    '''    
    Jogador é um módulo responsável por instânciar os objetos que executaram
        as ações dos personagens.
        
   Ao instanciar o módulo Jogador é necessario informar o nome que o Jogador 
   terá, ex. jogador1 = Jogador('Christopher').
   '''
    def __init__(self, value):
        self._nome = value
        self._possiveisJogadas = {'0':'Pedra', '1': 'Papel', '2': 'Tesoura'}
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self,value): 
        self._nome = value
    
    nome = property(get_nome, set_nome)

    def jogar(self):
        return self._possiveisJogadas.get(str(random.randint(0,2))) 
    
    def set_jogada(self):
        try:
            escolhaJogador = int(input("Digite a opção que gostaria de jogar \r 0 - para Pedra, 1 - para Papel e 2 - para Tesoura: "))
            if(escolhaJogador < 0 or escolhaJogador > 2):
                print("A jogada escolhida deve estar entre 0 e 2. Jogue novamente")
                return escolherJogada()
            else:
                return self._possiveisJogadas.get(str(escolhaJogador))
        except ValueError:
            print("A jogada escolhida deve ser um valor númerico de 0 a 2. Jogue novamente")
            return escolherJogada()   
