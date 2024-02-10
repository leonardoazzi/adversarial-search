# Headkicker
Implementação do Jogo da Velha e Othello com algoritmos de busca com adversários.

## Bibliotecas
```
PyTermGUI==7.7.0
typing_extensions==4.9.0
```

## Conteudo
O kit contém os seguintes arquivos (todos os `__init__.py` estao omitidos):

```text
kit_games
├── server.py              <-- servidor de jogos
├── test_minimax_tttm.py        <-- teste da poda alfa-beta no tic-tac-toe misere
├── test_othello_evaluations.py <-- teste das funcoes de avaliacao do othello p/ a poda alfa-beta
├── test_pruning.py             <-- teste da poda alfa-beta em um jogo simplificado
└── advsearch
    ├── othello
    |   ├── board.py       <-- encapsula o tabuleiro do othello
    |   └── gamestate.py   <-- encapsula um estado do othello (config. do tabuleiro e cor que joga)
    ├── tttm
    |   ├── board.py       <-- encapsula o tabuleiro do tic-tac-toe misere
    |   └── gamestate.py   <-- encapsula um estado do tic-tac-toe-misere (config. do tabuleiro e cor que joga)
    ├── randomplayer
    |   └── agent.py       <-- agente que joga aleatoriamente
    ├── humanplayer        
    |   └── agent.py       <-- agente para um humano jogar 
    ├── timer.py           <-- funcoes auxiliares de temporizacao
    └── your_agent         <-- renomeie este diretorio c/ o nome do seu agente 
      ├── minimax.py      <-- implemente a poda alfa-beta aqui
      ├── othello_minimax_count.py  <-- chame seu minimax com a heuristica de contagem 
      ├── othello_minimax_mask.py   <-- chame seu minimax com a heuristica posicional 
      ├── othello_minimax_custom.py <-- chame seu minimax com uma heuristica customizada
      ├── tttm_minimax.py           <-- chame seu minimax sem limite de profundidade aqui
      └── [vc pode adicionar outros arquivos e subdiretorios aqui]
```

## Requisitos 
O servidor foi testado em uma máquina GNU/Linux com o interpretador python 3.9.7.

Outras versões do interpretador python ou sistema operacional podem funcionar, mas não foram testados.

## Instruções

Para iniciar uma partida, digite no terminal:

`python server.py game player1 player 2 [-h] [-d delay] [-p pace]  [-o output-file] [-l log-history]`

Nos parâmetros, game é o jogo a ser jogado (othello ou tttm para tic-tac-toe misere)  'player(1 ou 2)' são o caminhos dentro de `advsearch` onde estão implementados os make_move dos jogadores.

Somente para Othello: Para ver o tabuleiro e as peças com cores, instale a biblioteca `pytermgui` (por exemplo, com `pip install pytermgui`) e execute o `server_tui.py` ao invés do `server.py`.


Os argumentos entre colchetes são opcionais, seu significado é descrito a seguir:
```text
-h, --help            Mensagem de ajuda
-d delay, --delay delay
                    Tempo alocado para os jogadores realizarem a jogada (default=5s)
-p pace, --pace pace
                    Tempo mínimo que o servidor espera para processar a jogada (para poder ver partidas muito 
                    rapidas sem se perder no terminal)
-l log-history, --log-history log-history
                    Arquivo para o log do jogo (default=history.txt)
-o output-file, --output-file output-file
                    Arquivo de saida com os detalhes do jogo (inclui historico)
```

O jogador 'random' se localiza em `advsearch/randomplayer/agent.py`. Para jogar uma partida com ele,
basta substituir player1 ou 2 por esse caminho. Como exemplo, inicie
uma partida random vs. random de othello para ver o servidor funcionando:

`python server.py othello advsearch/randomplayer/agent.py advsearch/randomplayer/agent.py -d 1 -p 0.3`

O delay pode ser de 1 segundo porque o jogador random é muito rápido (e muito incompetente). O passo é de 0.3 segundos para acompanhar o progresso da partida (pode acelerar ou reduzir conforme a necessidade).

O jogador 'human' se localiza em `advsearch/humanplayer/agent.py`. Você pode utilizar este player para jogar você mesmo e testar suas habilidades contra outro agente (inclusive o que você está construindo nesse trabalho). 

Para jogar com ele, utilize o mesmo comando acima, trocando o player1 ou 2 por `advsearch/humanplayer/agent.py`. Você terá o limite de 1 minuto para pensar na sua jogada. Digite as coorenadas da ação na ordem `<coluna> <linha>`.  

## Funcionamento 

Iniciando pelo primeiro jogador, que jogará com as peças pretas, o servidor chama a função `make_move(state)` do seu agente. A função recebe `state`, um objeto da classe `GameState` que contém um tabuleiro (objeto da classe `Board` e o jogador a fazer a jogada (um caractere) (`B` para as pretas ou `W` para as brancas). Para os detalhes, veja `gamestate.py` e `board.py` de cada jogo.

O servidor então espera o delay e recebe a tupla (x,y) com coluna e linha com a jogada do jogador. O servidor processa a jogada, exibe o novo estado no terminal e passa a vez para o próximo jogador, repetindo esse ciclo até o fim do jogo.

No fim do jogo, o servidor exibe a pontuação de cada jogador e cria um arquivo `results.xml`.
com todas as jogadas tentadas pelos jogadores (inclusive as ilegais). Um arquivo `history.txt` também contém as jogadas, e esse é criado mesmo que a partida seja interrompida no meio (e.g. crash de um agente).


## Notas
* O servidor checa a legalidade das jogadas antes de efetivá-las. A vez é devolvida para o jogador que tentou a jogada ilegal
* O jogador 'random' apenas sorteia uma jogada entre as válidas no estado recebido.
* O jogador 'human' verifica a legalidade da jogada antes de enviá-la ao servidor.
* Em caso de problemas com o servidor, reporte via moodle ou email.

## Resultados da avaliação

### Tic-Tac-Toe misere
#### (i) O minimax sempre ganha do randomplayer?
Não. Existem cenários onde o minimax e o randomplayer empatam.
    
```
Current board:
    0   1   2
            
0   B   B   W
            
1   W   B   B
            
2   B   W   W
---- Current match: advsearch/headkicker (B) x (W) advsearch/randomplayer ----
End of game reached! Scores:
Player 1 (B - advsearch/headkicker): 0
Player 2 (W - advsearch/randomplayer): 0
Draw!
```

#### (ii) O minimax sempre empata consigo mesmo?
Sim!
```
Current board:
    0   1   2
             
0   B   B   W
             
1   W   B   B
             
2   B   W   W
---- Current match: advsearch/headkicker (B) x (W) advsearch/headkicker ----
End of game reached! Scores:
Player 1 (B - advsearch/headkicker): 0
Player 2 (W - advsearch/headkicker): 0
Draw!
```

#### (iii) O minimax sempre empata contra as jogadas perfeitas?
Sim!
Em todas as vezes em que o minimax começou jogando, ele escolheu a posição do centro, que é a única que força o empate logo na primeira jogada.
Nas vezes em que um humano começou jogando e escolheu a posição central, o minimax fez todas as jogadas em posições que iriam forçar o empate.
Nas vezes em que um humano jogou em posições que abririam brecha para o minimax ganhar, o minimax escolheu jogar em posições que de fato levariam à vitória e não forçariam o empate

### Othello

- (i) Represente em uma matriz de 3 X 3 onde as linhas representam o jogador que inicia (player 1) e as colunas representam o player 2 e em cada célula, indique se a partida resultou em vitória (1), derrota (-1) ou empate (0) entre os agentes com cada uma das heurísticas.

| P1 / P2 | Count | Custom | Mask |
| ------- | ----- | ------ | ---- |
| **Count**  | +1 | -1 | +1 |
| **Custom** | +1 | +1 | +1 |
| **Mask**   | -1 | -1 | +1 |

```python
count_custom_mask = [
    [1, -1, 1],
    [1, 1, 1],
    [-1, -1, 1]
]
```

- (ii) Observe e relate qual implementação foi a mais bem-sucedida.
A implementação mais bem-sucedida foi a othello_minimax_custom.py.

- (iii) Reflita sobre o que pode ter tornado cada heurística melhor ou pior, em termos de performance.
Tanto a othello_minimax_count.py quanto a othello_minimax_mask.py utilizam heurísticas "fixas" e simples, por assim dizer.
A implementação othello_minimax_custom.py faz a mistura de 3 heuristicas diferentes e considera pesos diferentes para elas: compara a quantidade de peças que ambos os jogadores possuem no tabuleiro, conta o "score" de cada jogador baseado em uma matriz fixa de pesos para cada posição (posições melhores tem pesos maiores e posições piores tem pesos menores) e ainda compara a quantidade de movimentos legais cada jogador pode fazer naquele estado (quanto mais movimentos legais o jogador puder fazer, melhor será para ele).
As duas primeiras heurísticas citadas acima são as heuristicas utilizadas por othello_minimax_count.py e othello_minimax_mask.py, respectivamente.
Então, por levar em conta também a quantidade de movimentos legais poderá fazer nos próximos estados, othello_minimax_custom.py se saiu melhor.

## Feedback
- "Foi bem tranquilo, usei apenas o debugger e o conteúdo da disciplina. O algoritmo minimax desenvolvi a partir dos próprios slides. Eu acho que foi bem legal o trabalho em si, não tenho o que reclamar sinceramente. Não levei muito tempo pra fazer as coisas."
- "Curti bastante os trabalhos que envolvem jogos, principalmente este. É uma pena que nossos cronogramas na graduação não nos permitem tempo de qualidade para nos divertirmos e aprofundarmos mais em trabalhos como este. Utilizei além do debugger, o próprio enunciado e estrutura de documentação do trabalho. Particularmente, não utilizei e nem utilizo nenhum assistente de IA, e acredito que eles mais me atrapalham do que me ajudam. Uma LLM consegue te formular uma solução muito errada de uma forma muito convincente. Busco por documentações e fóruns como o Stack Overflow, pois são muito mais transparentes."
- "Concordo que o trabalho foi tranquilo. À partir do momento que a base do algoritmo está pronta, fazer mudanças e testes de execução fica extremamente simples. Eu particularmente utilizei o chatGPT 3.5 para ter ideias de heurísticas úteis para implementar no othello_minimax_custom.py, inclusive a mistura das 3 heurísticas usadas foi baseada em uma ideia dele. Além disso, também utilizei o chatGPT para simplificar e explicar trechos de código e entender melhor o que estava acontecendo por de baixo dos panos. Quanto ao enunciado do trabalho, achei que o item "i" do Othello ficou um pouco confuso, não ficou claro com relação a qual jogador deveria ser considerada a vitória ou a derrota. De resto, achei que o enunciado está bem claro sobre o que deve ser desenvolvido."

## Grupo
Turma A

- Alisson Claudino de Jesus
- Leonardo Azzi Martins
- Vitor Pedrollo dos Santos

---
Universidade Federal do Rio Grande do Sul

Instituto de Informática - Departamento de Informática Aplicada

Inteligência Artificial - Prof. Joel Luís Carbonera (2023/2)