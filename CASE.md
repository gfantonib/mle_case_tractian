### 1ª etapa:
```
Se tivessemos um arquivo muito grande, qual tipo de arquivo você escolheria para armazenar os dados e por quê?
```
O arquivo **parquet** seria uma boa alternativa.
1. Suporte em quase todas as linguagens.
2. Sistema de armazenamento e representação culunar que aumenta a eficiência na busca de dados.
3. Suporta esquemas eficientes de compressão, diminuindo consideravelmente o espaço de armazenamento.

[referência-1](https://parquet.apache.org/docs/overview/motivation/)\
[referência-2](https://www.linkedin.com/pulse/impressive-csv-vs-parquet-performance-file-size-niraj-hirachan/)

```
O que é vetorização e por quê ela diminui o tempo de processamento de grandes volumes de dados?
```
Quando usamos estruturas de datos vetorizadas, temos as seguintes vantagens:
1. O dado é armazenado de maneira sequencial na memória, facilitando percorrer pela estrutura.
2. Os dados de um vetor serão sempre do mesmo tipo *(restrição)* facilitando as operações feitas neles *(vantagem)*.
3. Um vetor tira vantagem da arquitetura computacional *(multi-core)* para paralelizar o processamento.

Esses três motivos garantem um tempo menor no processamento dessa estrutura de dados.

[exemplo](./vector_test/vector.py)

### 2ª etapa:
```
Se uma API REST não estiver sendo rápida o suficiente, qual outra abordagem podemos utilizar?
```
1. Uma primeira alternativa poderia ser a de criar **caches** a partir de requests, para que, num próximo request, seu programa primeiro procure os dados localmente, antes de fazer o request.

2. Uma outra solução seria estabelecer um tipo de conexão **contínua** e **assíncrona** entre servidor e cliente, evitando o tempo gasto para estabelecer e reestabelecer a conexão. Esse tipo de abordagem reponde pelo nome de **WebSocket** e é usado em programas de *trading quantitativo*.

```
Quais métricas de performance da API você monitoraria para garantir que seu sistema está funcionando bem?
```
1. **Response Time:** O tempo que a API leva para responder a uma solicitação.
2. **Latency:** O atraso entre o envio de uma solicitação e o recebimento do primeiro byte da resposta.
3. **Failed Request Rate:** A porcentagem de solicitações que resultam em erro ou falha.
4. **Throughput:** O número de solicitações bem-sucedidas processadas pela API por unidade de tempo.
5. **Availability:** A porcentagem de tempo em que a API está operacional e acessível aos usuários.

[referência](https://www.catchpoint.com/api-monitoring-tools/api-performance-monitoring)

```
Qual caso de uso você imagina para a rota adjust?
```
1. Seguindo o sentido do nome da própria rota, reformulo a pergunta para: *o que exigiria um ajuste da média de um sensor?*\
Um ajuste de um valor coletado implica um erro em algum momento do contato sensor-máquina.\
O erro poderia ser detectado pela diminuição da precisão do modelo.\
Sua causa poderia estar atrelado ou à mudança da sensibilidade do sensor ou à alguma modificação do fenômeno que ele mede (ex: temperatura da máquina).\
Em ambos os casos, um ajuste de seus dados poderia ser feito. O sucesso desse ajuste poderia ser testado observando novamente a precisão do modelo.

### 3ª etapa:
