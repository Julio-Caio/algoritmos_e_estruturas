# Estudos em Recursividade

## Data: 20/10/2024

## Autor: Júlio Caio Rodrigues

# Estudo sobre Recursividade e sua Aplicação

## O que é "Dividir e Conquistar"?

"Dividir e Conquistar" (DC) é um paradigma de design de algoritmos que consiste em dividir um problema em subproblemas menores, resolver esses subproblemas de forma recursiva e, em seguida, combinar as soluções para resolver o problema original. Esse método é amplamente utilizado em algoritmos de busca, ordenação e em várias outras áreas da ciência da computação.

## A Recursividade e sua Aplicação

A recursividade é uma técnica de programação em que uma função se chama a si mesma para resolver um problema. Essa abordagem é especialmente útil para problemas que podem ser divididos em subproblemas menores, como o cálculo de números na sequência de Fibonacci, cálculo de fatoriais, busca em estruturas de dados, entre outros.

A recursividade se encaixa perfeitamente na abordagem de "Dividir e Conquistar". Ao dividir um problema em partes menores e resolver cada uma delas, a recursividade simplifica a lógica do algoritmo e pode levar a soluções mais elegantes e eficientes.

## Funcionamento da Pilha de Chamadas

A pilha de chamadas (call stack) é uma estrutura de dados que armazena informações sobre as funções que estão sendo executadas em um programa. Cada vez que uma função é chamada, um novo registro é adicionado à pilha, e quando a função termina, o registro é removido.

### Exemplo: Cálculo do Fatorial de 4

Vamos ilustrar como a pilha de chamadas funciona ao calcular o fatorial de 4 usando a função recursiva.

```bash
def fatorial(n: int) -> int:
    if n == 0:
        return 1
    return n * fatorial(n - 1)
```

#### Fluxo de Execução

1. **Chamada Inicial**: `fatorial(4)` adiciona `fatorial(4)` à pilha.
2. **Chamada Recursiva**: `fatorial(4)` chama `fatorial(3)`, adicionando `fatorial(3)` à pilha.
3. **Chamada Recursiva**: `fatorial(3)` chama `fatorial(2)`, adicionando `fatorial(2)` à pilha.
4. **Chamada Recursiva**: `fatorial(2)` chama `fatorial(1)`, adicionando `fatorial(1)` à pilha.
5. **Chamada Recursiva**: `fatorial(1)` chama `fatorial(0)`, adicionando `fatorial(0)` à pilha.
6. **Caso Base**: `fatorial(0)` retorna `1` e remove `fatorial(0}` da pilha.
7. **Continuação**: `fatorial(1)` retorna `1 * 1 = 1` e remove `fatorial(1)` da pilha.
8. **Continuação**: `fatorial(2)` retorna `2 * 1 = 2` e remove `fatorial(2)` da pilha.
9. **Continuação**: `fatorial(3)` retorna `3 * 2 = 6` e remove `fatorial(3)` da pilha.
10. **Finalização**: `fatorial(4)` retorna `4 * 6 = 24` e remove `fatorial(4}` da pilha. A execução é concluída.

### Resumo da Pilha em Cada Etapa

- A pilha de chamadas cresce conforme as chamadas recursivas são feitas.
- Quando o caso base é alcançado, as funções começam a retornar seus valores, diminuindo a pilha até que todas as chamadas sejam resolvidas.

## Códigos Desenvolvidos

Os códigos desenvolvidos durante os estudos estão disponíveis no mesmo diretório deste arquivo. Eles incluem implementações de funções recursivas para calcular fatoriais, gerar sequências de Fibonacci, e somar listas, entre outros exemplos práticos de recursividade.