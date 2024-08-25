### 1ª etapa:
#### Usage:
**Para rodar o modelo otimizado:**

1. Navegue até o diretório `src`:

    ```bash
    $> cd src
    ```

2. Execute o script Python:

    ```bash
    $> ./ml_run.py
    ```
**Para rodar uma comparação entre o modelo fornecido e o modelo otimizado:**

1. Navegue até o diretório `time_battery`:

    ```bash
    $> cd time_battery
    ```

2. Execute o script Python:

    ```bash
    $> ./time_battery.py
    ```
**Para rodar uma comparação entre iterar por uma `lista` e por um `vetor` *(numpy array)*:**

1. Navegue até o diretório `draft`

    ```bash
    $> cd draft
    ```

2. Execute o script Python:

    ```bash
    $> ./vector.py
	```

#### Perguntas:
```
Se tivessemos um arquivo muito grande, qual tipo de arquivo você escolheria para armazenar os dados e por quê?
```
O arquivo **parquet** seria uma boa alternativa.
1. Suporte em quase todas as linguagens.
2. Sistema de armazenamento e representação culunar que aumenta a eficiência na busca de dados.
3. Suporta esquemas eficientes de compressão, diminuindo consideravelmente o espaço de armazenamento.

[parquet documentation](https://parquet.apache.org/docs/overview/motivation/)\
[parquet performance](https://www.linkedin.com/pulse/impressive-csv-vs-parquet-performance-file-size-niraj-hirachan/)\
[dremel paper](https://static.googleusercontent.com/media/research.google.com/pt-BR//pubs/archive/36632.pdf)

```
O que é vetorização e por quê ela diminui o tempo de processamento de grandes volumes de dados?
```
Quando usamos estruturas de datos vetorizadas, temos as seguintes vantagens:
1. O dado é armazenado de maneira sequencial na memória, facilitando percorrer pela estrutura.
2. Os dados de um vetor serão sempre do mesmo tipo *(restrição)* facilitando as operações feitas neles *(vantagem)*.
3. Um vetor tira vantagem da arquitetura computacional *(multi-core)* para paralelizar o processamento.

Esses três motivos garantem um tempo menor no processamento dessa estrutura de dados.\
[exemplo](./draft/vector.py)

### 2ª etapa:
#### Usage:
**Para servir e testar o modelo na API:**

1. Navegue até o diretório `api`:

    ```bash
    $> cd api
    ```

2. Inicialize a API no *localhost* na porta *5000* rodando o script Python:

    ```bash
    $> ./app.py
    ```

3. Teste todas as *requests* automaticamente rodando o script Python:

    ```bash
    $> ./request_script.py
    ```

#### Perguntas:
```
Se uma API REST não estiver sendo rápida o suficiente, qual outra abordagem podemos utilizar?
```
Pensando em alternativas para melhorar o desempenho da aplicação, até mudar a própria aplicação, temos, do mais viável ao menos viável:

1. Uma primeira alternativa poderia ser a de criar **caches** a partir de requests, para que, num próximo request, seu programa primeiro procure os dados localmente, antes de fazer o request.

2. Uma segunda alternativa seria fazer uma revisão no código e buscar entender o porque da demora e, se for possível e vantajoso, alterar o código.

3. Uma terceira alternativa poderia ser a de procurar algum melhoramento no acesso ao banco de dados (otimizar as Queries).

4. Uma alternativa possível mas bem menos viável seria a de rearranjar a distribuição dos servidores, aproximando o cliente da aplicação.

5. Uma outra solução seria estabelecer um tipo de conexão **contínua** e **assíncrona** entre servidor e cliente, evitando o tempo gasto para estabelecer e reestabelecer a conexão. Esse tipo de abordagem reponde pelo nome de **WebSocket** e é usado em programas de *trading quantitativo*. Penso que essa seria a menos viável porque fazer essa mudança (de uma REST API para um WebSocket) implicaria num refazimento muito grande da aplicação.

[speed-obsessed traders](https://www.forbes.com/forbes/2010/0927/outfront-netscape-jim-barksdale-daniel-spivey-wall-street-speed-war.html)

```
Quais métricas de performance da API você monitoraria para garantir que seu sistema está funcionando bem?
```
1. **Response Time:** O tempo que a API leva para responder a uma solicitação.
2. **Latency:** O atraso entre o envio de uma solicitação e o recebimento do primeiro byte da resposta.
3. **Failed Request Rate:** A porcentagem de solicitações que resultam em erro ou falha.
4. **Throughput:** O número de solicitações bem-sucedidas processadas pela API por unidade de tempo.
5. **Availability:** A porcentagem de tempo em que a API está operacional e acessível aos usuários.

Essas são algumas métricas de monitoramento da API, mas definitivamente não são as únicas. Seria possível dizer que, mesmo no caso de essas 5 métricas estarem respondendo conforme o esperado, sua API não está funcionando bem. É importante lembrar que a métrica final de uma aplicação é a satisfação do cliente, e que, mesmo se uma API está *performando* bem, não significa que ela está *funcionando* bem, uma vez que sua funcionalidade e usabilidade não está agradando o usuário.

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
#### Usage:
**Para rodar a API usando Docker:**

sudo systemctl start docker

1. Use o comando `systemctl` para ativar o Docker:

    ```bash
    $> sudo systemctl start docker
    ```

2. Navegue até o diretório `api`:

    ```bash
    $> cd api
    ```

3. Construa a imagem Docker:

    ```bash
    $> docker build -t my-flask-app .
    ```

4. Rode o container mapeando a porta *5000:5000*:

    ```bash
	$> docker run -d -p 5000:5000 my-flask-app
	```

5. Se preferir, construa a imagem e rode o conteinar de uma vez rodando o shell script:

    ```bash
    $> ./run_docker.sh
	```

6. Teste a aplicação com o script Python:

    ```bash
    $> ./request_script.py
    ```

**Comandos adicionais do Docker:**

- Listar containers ativos:

    ```bash
    $> docker ps
    ```

- Listar containers ativos e não ativos:

    ```bash
    $> docker ps -a
    ```

- Desativar container:

    ```bash
    $> docker stop <container id>
    ```

- Ativar container:

    ```bash
    $> docker start <container id>
    ```

- Remover container:

    ```bash
    $> docker rm <container id>
    ```

- Listar imagens:

    ```bash
    $> docker images
    ```

- Remover imagem:

    ```bash
    $> docker rmi <image id>
    ```

**Para rodar o comando `docker` sem sudo:**

```bash
$> sudo groupadd docker
$> sudo usermod -aG docker $USER
$> newgrp docker
```

---

### python virtual environments

**Para criar um ambiente virtual do python**

1. Crie uma pasta destino:

```bash
$> mkdir <venv>
```

2. Ative o ambiente virtual:

```bash
$> source <venv>/bin/activate
```

3. Instale os pacotes necessários para a aplicação:

```bash
$> pip install -r requirements.txt
```

4. Para desativar o ambiente virtual:

```bash
$> deactivate
```