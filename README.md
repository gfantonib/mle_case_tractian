# Machine Learning Engineer Case

## Contexto
As habilidade que queremos avaliar com esse case são:
- Linguagem Python;
- Arquitetura de software;
- Programação orientada a objetos;
- Modelagem de dados;
- Criação de APIs;
- Git;
- Familiariade com as etapas de treinamento e deploy de um modelo de IA;
- Senso crítico.

## O que eu preciso para fazer o case?

Todos os arquivos necessários estão nesse repositório:

- data: contém os dados que serão usados no case;
- src: contém um arquivo de contendo um código de treinamento de um modelo manual;
- api_tests: contém algumas entradas de teste para testar sua api

## Como o case deve ser entregue?

Você pode criar um fork desse repositório e começar o seu desenvolvimento no seu próprio repositório. Quando terminar o link do repositório no github deverá ser enviado para avaliação.

Se você quiser documentar o que você fez, adicionando notas, imagens, etc. Você pode criar um arquivo `CASE.md` no seu diretório e incluir qualquer informação que voc6e queira.

## Etapas

O case é composto por 3 etapas. Cada etapa tem por objetivo avaliar uma habilidade técnica.

### 1. Modelando o processo

A primeira parte do desafio é realizar uma refatoração do código presente no arquivo `src/draft.py`. Sua tarefa é entender o que está sendo feito por ele e propor uma organização alternativa.

Você é livre para fazer toda e qualquer alteração no código contanto que a lógica seja mantida. O único pré requisito é que deve haver um modo de recuperar para cada sensor se determinada coluna está em alerta ou não.

Sugestões:
- Faça otimizações relacionadas a performance. Quão mais rápido ficou?
- Pense em quais são as etapas que estão sendo feitas. Como organizá-las de forma adequada?
- Como você está organizando seus dados?

Perguntas:
- Se tivessemos um arquivo muito grande, qual tipo de arquivo você escolheria para armazenar os dados e por quê?
- O que é vetorização e por quê ela diminui o tempo de processamento de grandes volumes de dados?

### 2. Servindo o modelo

Na segunda etapa você irá a estrutura que você criou na parte 1 (fazendo as alterações que achar necessário) e criar uma API REST para servir o modelo.

Não existe um framework específico que você deve utilizar, fique à vontade para usar aquele com que você tem mais familiaridade.

#### Requisitos

A API deverá ter as seguintes rotas:

- `/{sendor_id}/fit`: essa rota recebe uma requisição POST e como corpo da requisição uma lista, chamada `values`, de *floats* e calcula a média e o desvio padrão para aquele grupo de dados. Os valores calculados devem ser armazenados e associados com o `sensor_id` informado;
- `/{sensor_id}/weights`: essa rota recebe uma requisição GET, sem corpo. O retorno da rota deve ser os valores armazenados de média e desvio padrão para aquele `sensor_id`;
- `/{sensor_id}/predict`: essa rota também recebe uma requisição POST, com o corpo contendo somente um campo `value` que é um float. O retorno dessa rota deve usar a lógica de predição de alerta da parte 1 para decidir se o sensor está em alerta ou não. O tipo de dado retornado é um *bool*.
-  [Bônus]`/{sensor_id}/adjust:`: essa rota recebe uma requisição POST sem corpo. Quando receber essa requisição ele vai aumentar o valor dá média estimada daquele sensor em 10%.

Na pasta `api_tests` existem alguns arquivos com o corpo de algumas requições para você testar. O nome dos arquivos indica qual o método e qual a rota que devem ser usadas. 


Perguntas:
- Se uma API REST não estiver sendo rápida o suficiente, qual outra abordagem podemos utilizar?
- Quais métricas de performance da API você monitoraria para garantir que seu sistema está funcionando bem?
- Qual caso de uso você imagina para a rota `adjust`?

### 3. [BÔNUS] Usando Docker

A terceira etapa é uma etapa bônus, no sentido de que não é necessária para terminar o desafio, mas é um grande adicional.

Se você decidir fazer essa etapa, você deve deverá criar um contêiner, utilizando a ferramenta docker para rodar sua API.

O que você deve entregar nessa etapa é:

- Um arquivo Dockerfile;
- Um arquivo de script com os comandos e configurações necessários para contruir e rodar a imagem. Esse arquivo pode ser qualquer coisa, desde um *shell script* até um *makefile* ou qualquer outro formato.

PS: Se vcoê escolher um formato não tão conhecido, lembre-se de incluir as instruções de instalação e execução.
