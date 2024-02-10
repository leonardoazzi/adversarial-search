# Headkicker - jogos de tabuleiro com agentes adversários

## Grupo
Turma A

- Alisson Claudino de Jesus 00246796
- Leonardo Azzi Martins 00323721
- Vitor Pedrollo dos Santos 00312948

## Bibliotecas
```
PyTermGUI==7.7.0
typing_extensions==4.9.0
```

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

---
Universidade Federal do Rio Grande do Sul

Instituto de Informática - Departamento de Informática Aplicada

Inteligência Artificial - Prof. Joel Luís Carbonera (2023/2)