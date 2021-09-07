# Othello/Reversi IA

### Integrantes do grupo
Turma A
- Alencar da Costa - 00288544
- Matheus Woeffel Camargo - 00288543
- João Vicente Lessa - 00243673

### Bibliotecas adicionais
Não é necessário adicionar nenhuma biblioteca adicional, visto que somente usamos módulos nativos do Python.

### Detalhes da implementação
#### Função de avaliação
Para avaliação dos estados foram utilizadas diversas heurísticas diferentes baseadas em estratégias conhecidas no jogo. Para cada heurística foi associado um peso/importância de forma que a função de avaliação do estado seja um combinação linear de heurísticas. Além disso, as heurísticas utilizadas e os pesos associados mudam de acordo com a fase do jogo, já que as estratégias se adaptam ao longo de uma partida. 


As fases de uma partida são definidas de acordo com o número de jogadas realizadas até o momento. Assim, o jogo pode ser dividio em 3 fases principais: early-game, mid-game e end-game. O early-game compreende a fase inicial do jogo, as primeiras 20 jogadas. Nessa fase, a estratégia é maximizar a mobilidade do player em cada jogada, fazendo com que ele tenha um maior número de jogadas possíveis, além, é claro, de dar preferência para as quinas do tabuleiro e evitar as peças adjacentes às quinas (para evitar que o ponente tenha oportunidade de conquistar uma quina). Entre a vigésima e a quadragésima jogada, a fase do jogo é dita mid-game e a partir desse momento, passamos a dar importância para o placar do jogo, bem como a paridade do número de posições do tabuleiro livre (é mais vantajoso para o player tem um número ímpar de posições livres). Por fim, o end-game compreende as últimas 20 jogadas da partida e nessa fase a paridade e o placar passam a ter maior relevância na estratégia.


Além disso, as funções implementadas para cada heurística retornam um valor entre -1 e 1. Onde 0 é um estado neutro para a heurística, valores negativos são estados prejudiciais ao jogador e valores positivos representam estados bons. Os pesos associadas a elas em cada fase do jogo podem ser vistas no arquivo `minimax.py` no método `heuristic()` da classe `MinimaxSolver`. Nessa função será possível notar o alto peso associado a heurística de obtenção de quinas, já que o controle delas é algo extremamente valioso para o jogador, dado que essas peças não podem ser perdidas. A seguir é descrito cada uma das heurísticas implementadas.
- `score_heuristic(board: Board, color)`: a porcentagem da pontuação do jogador em relação ao total de posições no tabuleiro.
- `score_difference_heuristic(board: Board, player_color)`: relação entre a diferença entre os pontos dos jogadores e o total de pontos.
- `mobility_heuristic(board: Board, player_color)`: relação entre a quantidade de movimentos possíveis do jogador e de seu oponente.
- `corners_heuristic(board: Board, player_color)`: relação entre a quantidade de quinas obtidas pelo jogador e seu oponente, buscando maximizar o número de quinas obtidas pelo jogador.
- `edges_heuristic(board: Board, player_color)`: relação entre a quantidade de peças nas bordas do tabuleiro obtidas pelo jogador e seu oponente.
- `next_to_corners_heuristic(board: Board, player_color)`: relação entre a quantidade de peças adjacentes a uma quina não conquistada que foram obtidas pelo jogador e seu oponente. Busca maximizar o número de peças do oponente nessas posições e minimizar as peças do jogador, visto que uma peças nessas posições permite ao oponente conquistar uma quina, algo que se deseja evitar.
- `parity_heuristic(board: Board, color)`: retorna -1 caso o número de peças remanescentes no tabuleiro seja par, caso contrário retorna 1. 


Para conhecer e aprender essas estratégias de jogo, foram utilizados recursos citados nas referências.

#### Estratégia de parada
A estratégia de parada utilizada durante a avaliação dos estados foi a profundidade limite através da busca com profundidade limitada e a avaliação do estado ser terminal ou não (utilizando a função `is_terminal_state()` da classe `Board`).

#### Minimax
Foi implementado o algoritmo Minimax com Alpha Beta Pruning e busca com profundidade máxima a partir dos pseudocódigos disponibilizados nos materiais de estudo. A classe `MinimaxSolver` é responsável por implementar o algoritmo. O método `minimax()` retorna o movimento com a maior utilidade, já os métodos `maxvalue()` e `minvalue()` foram adaptados para retornarem uma tupla de valores contendo o valor do estado avaliado e o melhor movimento associado a esse valor.

#### Avaliação da IA resultante
Durante o desenvolvimento do algoritmo minimax e das primeiras heurísticas, a IA foi testada unicamente com `randomplayer` com a finalidade de avaliar o comportamento. Em seguida, com a inteligência aprimorada, passamos a testar IA vs IA com heurísticas diferentes até encontrar um modelo que obtesse os melhores resultados. 

Por exemplo, implementamos as heurísticas e associamos pesos para uma IA. Em seguida, colocamos essa IA para jogar com outras IAs que utilizassem heurísticas/estratégias de jogo mais simples. Quando obtemos uma IA que seguia estratégias pré-definida e ganhava da IA mais simples com a estratégia ingênua de buscar sempre maximizar o número de peças conquistas, passamos a incrementar a IA mais simples e adaptar os pesos das heurísticas da IA estratégista conforme ela perdia para IA "mais simples". Foi através dessa forma de avaliação da IA que chegamos aos valores e heurísticas que são utilizados na versão final. Foi dessa forma também, que notamos a necessidade de adaptar a estratégia conforme o andamento do jogo através das diferentes fases.

Por fim, implementamos um "agente manual" que permitesse com que as jogadas fossem realizadas através da linha de comando. Com isso, colocamos nossa IA para jogar com IAs presentes em versões do Othello encontradas na internet. Por exemplo, nossa IA ganhou, nos três níveis de dificuldade, da IA desse site: [https://hewgill.com/othello/](https://hewgill.com/othello/).

#### Eventuais melhorias
Embora a IA desenvolvida, aparentemente, obteve bons resultados, há melhorias que podem ser feitas para aumentar sua qualidade. Por exemplo, extensões singulares para que sempre que houver uma jogada que permita a obtenção de uma quina, essa será feita sem a avaliação dos estados através das heurísticas definidas. Além disso, algo rotineiro em IAs para jogos de tabuleiro é a presença de um banco de jogadas contendo jogadas de abertura e fechamento para que jogadas elaboradas e bem conhecidas sejam aplicadas sempre que possível.

Outro ponto, é a implementação em termos de perfomance computacional, certamente há pontos na implementação poderiam ser analisados em busca de uma implementação mais eficiente que trouxesse melhorias na performance de avaliação de estados. Isso permitiria aumentar o limite de profundidade de avaliação estipulado no momento sem estourar o limite de 5 segundos para realização da jogada.

### Referências

[Introduction to Stragies for Othello](https://www.ultraboardgames.com/othello/strategy.php)

[Tips to win Othello](https://www.ultraboardgames.com/othello/tips.php)

[Strategy guide](http://radagast.se/othello/Help/strategy.html)

[How to win at Othello: Corner & Edge Strategies](https://www.youtube.com/watch?v=SvxTrjvPrSY&ab_channel=KeithGalli)

[How to win at Othello almost every time!](https://www.youtube.com/watch?v=sJgLi32jMo0&ab_channel=KeithGalli)

[“IAgo Vs Othello”: An artificial intelligence agent playing Reversi](http://ceur-ws.org/Vol-1107/paper2.pdf)