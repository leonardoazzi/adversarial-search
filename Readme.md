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
- Jogadas perfeitas recomendadas pelo https://nyc.cs.berkeley.edu/uni/games/ttt/variants/misere. Para verificar isso, use o humanplayer. No link, faça as jogadas do minimax, e no servidor do kit, faça as jogadas recomendadas (amarelo ou verde) do link.

### Othello
#### Torneio
- (i) Represente em uma matriz de 3 X 3 onde as linhas representam o jogador que inicia (player 1) e as colunas representam o player 2 e em cada célula, indique se a partida resultou em vitória (1), derrota (-1) ou empate (0) entre os agentes com cada uma das heurísticas.
- (ii) Observe e relate qual implementação foi a mais bem-sucedida.
- (iii) Reflita sobre o que pode ter tornado cada heurística melhor ou pior, em termos de performance.


## Feedback
- "Foi bem tranquilo, usei apenas o debugger e o conteúdo da disciplina. O algoritmo minimax desenvolvi a partir dos próprios slides. Eu acho que foi bem legal o trabalho em si, não tenho o que reclamar sinceramente. Não levei muito tempo pra fazer as coisas."
- "Curti bastante os trabalhos que envolvem jogos, principalmente este. É uma pena que nossos cronogramas na graduação não nos permitem tempo de qualidade para nos divertirmos e aprofundarmos mais em trabalhos como este. Utilizei além do debugger, o próprio enunciado e estrutura de documentação do trabalho. Particularmente, não utilizei e nem utilizo nenhum assistente de IA, e acredito que eles mais me atrapalham do que me ajudam. Uma LLM consegue te formular uma solução muito errada de uma forma muito convincente. Busco por documentações e fóruns como o Stack Overflow, pois são muito mais transparentes."

---
Universidade Federal do Rio Grande do Sul

Instituto de Informática - Departamento de Informática Aplicada

Inteligência Artificial - Prof. Joel Luís Carbonera (2023/2)