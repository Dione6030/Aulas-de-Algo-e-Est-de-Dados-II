# Busca em Grafos num Labirinto: DFS, BFS e Gulosa
 
Atividade da disciplina de Algoritmos e Estrutura de Dados II. O programa (`Labirinto.py`) modela um labirinto como um grafo e compara três estratégias de busca para ir do ponto de partida até a saída.
 
Para executar: `python Labirinto.py`
 
---
 
## 1. O labirinto
 
O labirinto é uma grade de 10 x 10 caracteres:
 
| Símbolo | Significado |
|---------|-------------|
| `#` | parede (não pode passar) |
| `.` | casa livre |
| `I` | início, na posição (2, 0) |
| `F` | saída, na posição (7, 4) |
 
```
.########.
........#.
I####.#.#.
##..#.#.#.
......#...
#####.#.##
...#..#.#.
.#..F##...
.#.###..#.
.......#..
```
 
As posições são `(linha, coluna)`, contadas a partir de zero.
 
**Modelagem como grafo.** Cada casa livre (qualquer uma diferente de `#`) é um vértice (59 na versão final). Duas casas livres vizinhas, nas quatro direções (↑ → ↓ ←), são ligadas por uma aresta. A função `montar_grafo` constrói esse grafo como um dicionário de listas de adjacência, e a função `livre` garante que a busca não saia da grade nem atravesse paredes. A ordem das direções (`↑ → ↓ ←`) é fixa e influencia o comportamento das buscas, principalmente da DFS.
 
**Desenho do labirinto.** Ele tem becos sem saída e um caminho "de volta": o início só sai para cima, e a saída, apesar de ficar perto do início em linha reta, exige dar a volta pela direita e por baixo. Na versão original, a única passagem entre a metade de cima e a de baixo é a casa `(5, 7)`. A versão final tem uma abertura extra em `(5, 5)`, que cria um atalho até perto da saída.
 
**Busca na mão.** Antes das buscas, um caminho foi traçado manualmente no labirinto original, escrito como lista de coordenadas, com 26 casas. Ele serve de referência visual. Como a passagem `(5, 7)` continua aberta, esse caminho ainda é válido na versão final, mas deixa de ser o mais curto por causa do atalho.
 
---
 
## 2. Implementações
 
As três buscas recebem o grafo, a casa inicial e a saída, e guardam as casas na ordem em que foram visitadas. A função `desenhar` marca essas casas com `*` no labirinto.
 
| Busca | Estrutura usada | Qual casa visita em seguida | Garante o menor caminho? |
|-------|-----------------|-----------------------------|--------------------------|
| **DFS** (profundidade) | recursão (pilha de chamadas) + conjunto de visitados | a primeira vizinha ainda não visitada, seguindo a ordem das direções | Não |
| **BFS** (largura) | fila (`deque`) + conjunto de visitados | a mais antiga da fila, ou seja, explora por camadas de distância | Sim (grafo sem pesos) |
| **Gulosa** | fila de prioridade (`heapq`) + conjunto de visitados | a de menor distância estimada até a saída | Não |
 
### DFS (busca em profundidade)
Segue por um caminho o mais fundo possível. Quando chega a um beco sem saída (ou a casas já visitadas), volta e tenta a próxima vizinha. Para assim que encontra a saída. Como a ordem das direções decide por onde ela começa, um caminho longo pode ser encontrado antes de um curto.
 
### BFS (busca em largura)
Visita primeiro todas as casas a um passo do início, depois as a dois passos, e assim por diante. Por explorar em camadas, a primeira vez que alcança a saída é pelo caminho mais curto. O custo é explorar casas em todas as direções, inclusive as que se afastam da saída.
 
### Busca Gulosa
Usa uma fila de prioridade ordenada por uma heurística `h`, a **distância de Manhattan** até a saída: `|linha - linha_saída| + |coluna - coluna_saída|`. Sempre expande a casa que *parece* mais perto da saída e ignora quanto já andou até ela. Por isso costuma visitar poucas casas, mas não garante o menor caminho: o resultado depende de a heurística apontar bem para a saída.
 
---
 
## 3. Resultados
 
**Como ler as tabelas:** "Casas visitadas" é a quantidade de casas exploradas até encontrar a saída (é o valor impresso como "Passos até a saída"). Ela mede o esforço da busca, e não o tamanho do caminho final. Na DFS, a contagem não inclui a casa inicial. O tempo é o "Tempo de execução" impresso em milissegundos.
 
Resultados no labirinto final (mostrado acima):
 
| Busca | Casas visitadas | Tempo de execução |
|-------|-----------------|-------------------|
| DFS | 45 | 0,05 ms |
| BFS | 28 | 4,10 ms |
| Gulosa | **15** | 0,09 ms |
 
Casas visitadas por cada busca (`*`):
 
**DFS**
```
*########*
********#*
I####.#*#*
##..#.#*#*
......#***
#####.#*##
***#..#*#*
*#**F##***
*#*###**#*
*******#**
```
 
**BFS**
```
*########.
********#.
I####*#*#.
##.*#*#*#.
..****#***
#####*#*##
...#**#*#.
.#..F##...
.#.###..#.
.......#..
```
 
**Gulosa**
```
.########.
******..#.
I####*#.#.
##..#*#.#.
....**#...
#####*#.##
...#**#.#.
.#..F##...
.#.###..#.
.......#..
```
 
### Análise
 
- **DFS:** em `(1, 5)` a ordem das direções faz ela ir para a direita (→) antes de descer (↓), então não passa pelo atalho da coluna 5. Ela percorre boa parte do labirinto, passando por vários becos sem saída, até achar a saída (45 casas).
- **BFS:** visitou 28 casas, mais que a gulosa, porque explora em todas as direções ao redor do início, camada por camada. Em troca, o caminho que ela encontra é o mais curto.
- **Gulosa:** visitou só 15 casas, e quase todas fazem parte do trajeto até a saída. Aqui a distância de Manhattan aponta bem para a saída e o atalho da coluna 5 está alinhado com ela, então a heurística funciona muito bem.
### Efeito do atalho na parede da linha 5
 
Além do labirinto final, foram testadas outras versões mudando só a abertura na linha 5. Cada célula mostra as casas visitadas e o tempo médio das execuções:
 
| Versão do labirinto | Execuções | DFS | BFS | Gulosa |
|---------------------|-----------|-----|-----|--------|
| Original (única passagem em `(5, 7)`) | 4 | 45 (0,06 ms) | 54 (4,11 ms) | 37 (0,09 ms) |
| Abertura em `(5, 1)` | 2 | 56 (0,09 ms) | 53 (4,99 ms) | 22 (0,12 ms) |
| Abertura em `(5, 5)` (**final**) | 1 | 45 (0,05 ms) | 28 (4,10 ms) | 15 (0,09 ms) |
 
- No labirinto original, a **BFS** visitou 54 das 58 casas livres: como a saída está longe do início em número de passos, ela precisa explorar quase tudo antes de chegar.
- A **BFS** e a **Gulosa** melhoram quando existe um atalho no caminho até a saída (de 54 para 28 e de 37 para 15 casas).
- A **DFS** não "enxerga" o atalho: o resultado depende da ordem das direções. Na abertura em `(5, 1)` ela até piorou (56), porque entrou pela abertura vindo de baixo e vasculhou a região de cima antes de chegar à saída.
- Os tempos mudam um pouco a cada execução: DFS e Gulosa ficaram abaixo de 0,15 ms, e a BFS ficou em torno de 4 a 5 ms. Como o labirinto é pequeno, servem como ordem de grandeza, e não como comparação definitiva.
---
 
## 4. Conclusão
 
- **DFS:** simples e a mais rápida nas medições, mas não garante o menor caminho e pode visitar casas demais.
- **BFS:** sempre encontra o menor caminho, ao custo de explorar mais casas.
- **Gulosa:** foi a que menos visitou casas nas três versões do labirinto (37, 22 e 15), graças à heurística, mas não tem garantia de caminho ótimo.
