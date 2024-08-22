### 1ª etapa:


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

```
Qual caso de uso você imagina para a rota adjust?
```
1. Seguindo o sentido do nome da própria rota, reformulo a pergunta para: *o que exigiria um ajuste da média de um sensor?*\
Um ajuste de um valor coletado implica, em algum momento do contato sensor-máquina, um erro.\
O erro poderia ser detectado pela diminuição da precisão do modelo.\
Sua causa poderia estar atrelado ou à mudança da sensibilidade do sensor ou à alguma modificação do fenômeno que ele mede (ex: temperatura da máquina).\
Em ambos os casos, um ajuste de seus dados poderia ser feito. O sucesso desse ajuste poderia ser testado observando novamente a precisão do modelo.

### 3ª etapa:
