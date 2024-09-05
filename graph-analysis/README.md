# Teste Prático: Desenvolvimento Backend com Go e Banco de Dados Neo4J

## Objetivo:
Avaliar a proficiência da pessoa candidata a vaga na linguagem Go, manipulação de bancos de dados e a capacidade de trabalhar com grandes volumes de dados e algoritmos de grafos utilizando o Neo4J.

## Descrição Geral:
A pessoa candidata a vaga deve baixar um conjunto de dados em formato CSV, realizar a carga desses dados no banco de dados Neo4J de forma eficiente, e criar uma API REST em Go que permita a consulta ao banco de dados usando cypher query e algoritmos de grafos.
Testes devem ser implementados para a garantia da qualidade da entrega.

## Instruções

### 1. Preparação dos Dados

**Download dos Dados:**
- Baixar o conjunto de dados em formato CSV do link a seguir: [Daily COVID-19 Data (2020-2024)](https://www.kaggle.com/datasets/abdoomoh/daily-covid-19-data-2020-2024?resource=download)

**Processamento e Carga no Neo4J:**
- Com base no modelo anexo ao final do descritivo:
- Realizar a carga desses dados para o Neo4J, considerando que no dia a dia da empresa trabalhará com grandes volumes.
- Não é permitido utilizar o comando `LOAD CSV` diretamente via Cypher. A pessoa candidata a vaga deve utilizar uma abordagem mais eficiente, como utilizar o `neo4j-admin` para a carga direta dos arquivos CSV ou desenvolver uma ferramenta para tal tarefa que ele mesmo implemente.
- Deverá fornecer a documentação de como planejou e executou a carga dos dados, justificando as escolhas tomadas.

### 2. Criação da API REST em Go

**API REST:**
- Desenvolver uma API REST em Go que permita a consulta ao banco de dados Neo4J. A API deve expor endpoints que respondam algumas perguntas de forma parametrizável.

**Perguntas:**
1. Qual foi o total acumulado de casos e mortes de Covid-19 em um país específico em uma data determinada?
2. Quantas pessoas foram vacinadas com pelo menos uma dose em um determinado país em uma data específica?
3. Quais vacinas foram usadas em um país específico?
4. Em quais datas as vacinas foram autorizadas para uso?
5. Qual foi o aumento de novos casos em um país específico durante os últimos 7 dias de um mês?
6. Quantas doses de reforço foram administradas em um país específico?
7. Quais países usaram uma vacina específica?
8. Quais foram as vacinas usadas em um determinado país e em que data elas começaram a ser aplicadas?
9. Qual país registrou o maior número de casos acumulados até uma data específica?
10. Qual foi a vacina mais utilizada em uma região específica?
11. Qual é o menor caminho temporal de disseminação do vírus entre dois países considerando os primeiros registros de casos em cada um?

**Descrição:**
- Queremos determinar a rota mais rápida de disseminação do vírus entre dois países com base nas datas dos primeiros registros de casos. 
- Assumimos que a disseminação segue uma sequência temporal, onde a doença se espalha de um país para outro com base na proximidade temporal dos primeiros registros de casos.
- Use um algoritmo de caminho mais curto, como o algoritmo de Dijkstra, para calcular a rota de disseminação que minimiza o tempo total (em dias) necessário para que o vírus se espalhasse do país de origem até o país de destino.
- Verifique onde que o vírus começou a ser registrado pela primeira vez.
- Seu objetivo é encontrar o menor caminho temporal de disseminação do vírus entre a origem e outros países.
- Leve em consideração apenas os países que registraram casos de Covid-19.
- A diferença de dias entre o primeiro caso em dois países deve ser usada como o peso dos relacionamentos entre esses países no grafo.
- Construa o grafo de maneira que ele represente adequadamente a propagação do vírus através das datas dos primeiros registros de casos.
- Imagine que o primeiro caso na China foi registrado em 15 de janeiro de 2020, e o primeiro caso na Itália foi registrado em 31 de janeiro de 2020. Se o Irã registrou seu primeiro caso em 25 de janeiro de 2020, você deve considerar que a disseminação do vírus pode ter seguido o caminho `China -> Irã -> Itália`.
- Calcule o número total de dias que teria levado para o vírus se espalhar seguindo esse caminho, e compare com outras possíveis rotas para determinar o caminho mais rápido.

- A API deve ser bem estruturada e seguir as melhores práticas em Go. a pessoa candidata a vaga deve se preocupar com a performance e a escalabilidade da solução.
- A pessoa candidata a vaga deve implementar testes unitários e opcionalmente de integração para os endpoints da API.

### 3. Entrega e Documentação

**Código-Fonte:**
- Para a entrega do teste, deverá ser feito um fork deste repositório para a conta da pessoa candidata a vaga, no github. 
- A pessoa deve adicionar um arquivo markdown ou orgmode ao seu repositório fornecendo instruções claras de como rodar o ambiente de desenvolvimento e realizar os testes necessários.

**Artefatos de Software:**
- A REST API e demais programas desenvolvidos devem ser encapsulados em containers Docker. 
- Recomenda-se o uso de docker compose e Makefile para a orquestração de tudo, API, Neo4J, ETL, etc.

**Documentação:**
- A pessoa candidata a vaga deve incluir uma documentação detalhada explicando a abordagem tomada para a carga dos dados, como a API foi implementada, e as decisões técnicas mais importantes. 
- Devem ser fornecidos exemplos de uso dos endpoints da API. Recomenda-se o uso de OpenAPI.

**Considerações de Performance:**
- A pessoa candidata a vaga deve evidenciar como garantiria a performance e escalabilidade da API em um ambiente de produção, considerando o volume de dados e as consultas realizadas.

## Avaliação
O teste será avaliado considerando os seguintes critérios:

- **Proficiência Técnica:** Qualidade e clareza do código em Go, uso adequado de técnicas e ferramentas.
- **Eficiência:** Abordagem adotada para carregar grandes volumes de dados no Neo4J.
- **Conhecimento de Grafos:** Implementação correta e eficiente dos algoritmos de grafos.
- **Qualidade de Código** Cobertura de testes e técnicas utilizadas.
- **Documentação:** Qualidade da documentação e clareza na explicação das escolhas técnicas.
- **Escalabilidade:** Considerações sobre performance e escalabilidade.

## Considerações Finais
Este teste simula um cenário real que a pessoa candidata a vaga poderá enfrentar na posição. O foco não está apenas na solução técnica, mas também na habilidade em justificar suas decisões e produzir um código que seja eficiente e escalável.

## Anexos: 
[Especificação do modelo](./spec/README.md)

