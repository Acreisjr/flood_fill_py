
# Projeto: Algoritmo Flood Fill - Mapeamento de Terrenos

## Descrição do Projeto
Este projeto implementa o algoritmo Flood Fill para identificar e preencher automaticamente todas as regiões conectadas em um grid bidimensional, representando um terreno com obstáculos.

O algoritmo é utilizado para auxiliar robôs autônomos no mapeamento de terrenos, diferenciando as regiões navegáveis separadas por obstáculos.

## Objetivo
- Identificar e preencher regiões conectadas em um grid 2D, utilizando diferentes cores (valores numéricos) para cada área livre.
- Respeitar obstáculos e regiões previamente preenchidas.
- Continuar preenchendo automaticamente até que todo o terreno esteja mapeado.

## Funcionamento do Algoritmo
1. O algoritmo inicia em uma célula fornecida.
2. Percorre todas as células ortogonalmente conectadas (acima, abaixo, direita e esquerda) que sejam navegáveis (`0`).
3. Preenche essas células com um valor de cor específico (começando por `2` e incrementando para as próximas regiões).
4. Após finalizar uma região, localiza a próxima célula navegável (`0`) e repete o processo até que todo o grid esteja preenchido.

## Como Executar
1. Clone o repositório.
2. Instale as dependências (necessário apenas `numpy` e `pandas`):
```bash
pip install numpy pandas
```
3. Execute o arquivo Python `flood_fill.py`.
4. O resultado será exibido no terminal ou notebook como uma matriz representando o grid preenchido.

## Exemplo de Funcionamento

### Entrada:
Grid inicial:
```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```
Coordenadas iniciais: `(0, 0)`

### Saída:
Grid preenchido:
```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

## Regras
- Obstáculos (`1`) não podem ser preenchidos.
- Regiões já preenchidas (`2`, `3`, ...) são preservadas.
- Apenas células ortogonalmente conectadas são consideradas.

## Autores

 - Alberto Júnior
 - Otávio Mendes
 - José Miguel
 - Gabriel Santiago
 - Lucas Barbosa
---
Desenvolvido para a disciplina de Fundamentos de Projeto e Análise de Algoritmos - Engenharia de Software - PUC Minas.
