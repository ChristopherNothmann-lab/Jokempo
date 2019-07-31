# Disputa de Jokempô versão 1.0 - 31/07/2019

O programa "Disputa de Jokempô" tem como objetivo implementar o jogo jokempô, ou como também é conhecido Pedra, papel e tesoura.  Este é um jogo de mãos recreativo, que e pode ser jogado entre duas ou mais pessoas, no caso do programa foi configurado para aceitar apenas duas, entre um jogador humano e o computador. <br>

O jogo consiste em um método de seleção entre pedra, papel e tesoura. Os jogadores devem simultaneamente escolher uma opção atráves um sinal com a mão. Então, os jogadores comparam os resultados para verificar o ganhador.

#### Regras: 
    
   * Mesma escolha empata a partida    
   * Pedra ganha da tesoura 
   * Tesoura ganha do papel 
   * Papel ganha da pedra
    
Neste jogo o usuário escolhe uma das opções (0 para escolher Pedra, 1  para Papel e 2 para Tesoura) e através de um método randômico o computador selecionará a opção dele. Cada partida vale 1 ponto, ganha a disputa quem pontuar 3 pontos primeiro.

### Tabela de conteúdo
1. [Autor](#Autor)
2. [Arquivos existentes no projeto](#ArquivosExistentesProjeto)
3. [Decisões de design do projeto](#DecisõesDesignProjeto)
4. [Instalação](#Instalação)
5. [Instrução de uso](#Instrução)
6. [Contatos](#Contatos)

<div id='Autor'/>

### Autor
* Christopher Nothmann Tumenas Cabral da Costa -  <christopher.nothmann@gmail.com>

<div id='ArquivosExistentesProjeto'/>

### Arquivos existentes no projeto:
* Jokempo/jokempo/Jogar.py
* Jokempo/jokempo/modulos/Jogador.py
* Jokempo/jokempo/modulos/Placar.py


<div id='DecisõesDesignProjeto'/>

### Decisões de design do projeto:

#### Classe Jogador 
 Jogador é um módulo responsável por instânciar os objetos que executaram as ações dos personagens ao decorrer do algorítmo.
 
#### Importando a biblioteca
Nesta classe foi necessário a importação da *Lib/random.py*. Esta biblioteca nos permite gerar elememtos aleátorios e precisaremos deste comportamento para que o computador possa efetuar uma jogada ao acaso.

```python
import random 
```
#### O objeto Jogador
Ao instânciar um objeto do tipo Jogador deveremos informar o nome do jogador, pois ao retornar o objeto o mesmo estará pronto para o uso, seus atribuitos estaram preenchido. Sem ter a possibilidade de criar objetos com informações incompletas.<br>
Este objeto possui duas funções que são responsáveis por mostrar o nome do jogador e  outra de receber e aplicar no objeto jogador um nome, sendo respectivamente o __get_name()__ e o __set_name()__. Por serem get e set de um atributo privado as determinamos como sendo a propriedade _nome_.

``` python
 def __init__(self, value):
        self._nome = value
        self._possiveisJogadas = {'0':'Pedra', '1': 'Papel', '2': 'Tesoura'}
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self,value): 
        self._nome = value
    
    nome = property(get_nome, set_nome)
```
#### Efetuando jogadas
Nesta classe possuímos duas formas de se efetuar uma jogada. <br>
O __jogar()__ que é uma função que efetuará as jogadas do computador, através dos recursos da biblioteca __random__ importada previamente geramos um número aleatório que esteja entre 0 e 2, na qual retornamos o valor armazenado no dicionário de possíveis jogadas.<br>
O __set_jogadas()__ é a função responsável por capturar do terminal a jogada efetuada pelo usuário, nela possui uma validação para que o usuário escolha entre as opções(0, 1 e 2), caso escolhe um valor diferente ele deverá repetir a ação até vir um valor válido. Em seguida a função retornará o valor armazenado no dicionário de possíveis jogadas.

``` python 
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
```     

#### Classe Placar 
Placar é um reponsável por instaciar o objeto que controlará as regras e os pontos do jogo, além de ser responsável por iniciar a partida e anunciar o vencedor.

#### O objeto Placar
Ao instanciar um objeto do tipo Placar nos iniciarmos os atributos privados, o atributo de jogadores está com a lista vazia e a lista de dicionário __Regra__ estará preenchida com as regras de pontuação do jogo.<br>
Este objeto possui duas funções que são responsáveis por mostrar os jogadores cadastrados e outra de receber e aplicar jogador na lista de jogadores, sendo respectivamente o __get_jogadores()__ e o __set_jogadores()__, nesta segunda função possui uma validação para determinar que apenas dois jogadores joguem (o Usuário e o computdor). Por serem get e set de um atributo privado as determinamos como sendo a propriedade _jogadores_.

```python
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
```
```python
 def get_jogadores(self):
        return self._jogadores
    
    def set_jogadores(self, value):
        if (len(self._jogadores) < 2 ):
            jogador = {'nome':str(value),'placar': 0}
            self._jogadores.append(jogador)
            
    jogadores = property(get_jogadores, set_jogadores)   
```
#### Iniciar uma partida
Neste método recebemos duas jogadas a primeira sendo a jogada efetuada pelo jogador 1 e a outra pelo jogador 2, informamos ao terminal do Linux os jogadores e as jogadas efetuadas e efetua o comparativo das jogadas informadas.<br>
Na comparação verificamos se possuimos um empate, caso positivo ninguem pontuará, caso negativo verificamos os valores sobre a ótica do jogador 1, pois se ele não pontuar, o jogador 2 deve pontuar, já que o empate ja foi verificado.<br>
Após o comparativo, será adicionado um ponto no placar do pontuador e informado quem pontuou.

```python
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
```
#### Anunciar o vencedor
Neste método de anúncio do vencedor verificamos quem pontuou o 3 ponto e, caso encontre, será informado o placar final e o nome do jogador vencedor em destaque.

```python
def anunciarVencedor(self):
        vencedor = next(item['nome'] for item in self._jogadores if item['placar'] == 3)
        if(vencedor != 'none'):
            print('Placar {0} - {1} x {2} - {3}  \n O vencedor é \033[32m{4}\033[0m \n'
                  .format(self._jogadores[0]["nome"],
                          self._jogadores[0]["placar"],
                          self._jogadores[1]["nome"],
                          self._jogadores[1]["placar"],
                          vencedor))
```
#### Classe Jogar 
Esta classe é a responsável por utilizar a lógica implementada nos módulos anteriores e executar o jogo no terminal Linux 

#### Importando o módulos
Nesta parte são importado os módulos que foram explicados anteriormente, para que a classe Jogar possa ter acesso aos recursos que estes módulos fornecem.

```python
from modulos import Jogador as jgr
from modulos import Placar as plc
```
#### Execução do Programa
Quando executado o programa primeiramente será questionado o nome para o jogador 1, que será o usuário no terminal, sendo informado é instanciado um objeto que o represente e após será instanciado outro objeto, responsável por representar o computador. <br>
Posteriormente os jogadores são registrados na lista de jogadores, esta nas classe Placar e temos início a disputa de jokempô.
A disputa esta configurada para ocorrer partidas até que um dos dois jogadores obter 3 pontos no placar.
Para cada partida o terminal questionará ao usuário qual jogada ele quer efetuar, deverá ser informado o número correspondente a jogada. Após a escolha do usuario, o computador escolherá a sua jogada de forma aleatória e por fim o placar comparará e informará a pontuação. <br> 
Quando um dos dois participantes obter o terceiro ponto o jogo será interrompido e será informado o vencedor da disputa.

```python
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
```


<div id='Instalação'/>

### Instalação

*  Este programa não requer instalacão para o seu funcionamento.

<div id='Instrução'/>

### Instrução de uso

*  Para executar o programa deve-se:
   1. Abrir o terminal apontando para a pasta onde foi salvo os arquivos
   2. executar no terminal Linux o seguinte comando:   <br> <br>
    
   ```    
   python3 Jogar.py 
   ```
<div id='Contatos'/>

### Contatos 
git-hub: https://github.com/ChristopherNothmann-lab/Jokempo/ <br>
e-mail: christopher.nothmann@gmail.com
