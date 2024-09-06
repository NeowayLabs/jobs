# Teste Prático: Desenvolvimento Backend com Go e Banco de Dados Neo4J

## Objetivo:
Avaliar a proficiência da pessoa candidata na linguagem Go, manipulação de bancos de dados e a capacidade de trabalhar com dados utilizando o Neo4J.

## Descrição Geral:
A pessoa candidata deve baixar um conjunto de dados em formato CSV, realizar a carga desses dados no banco de dados Neo4J de forma eficiente, e criar uma API REST que permita a consulta ao banco de dados usando cypher query.
Testes devem ser implementados para a garantia da qualidade da entrega.

## Instruções

### 1. Preparação dos Dados

**Download dos Dados:**
- Baixar o conjunto de dados em formato CSV do link a seguir: [Daily COVID-19 Data (2020-2024)](https://www.kaggle.com/datasets/abdoomoh/daily-covid-19-data-2020-2024?resource=download)

**Processamento e Carga no Neo4J:**
- Com base no modelo anexo ao final do descritivo:
- Realizar a carga desses dados para o Neo4J.
- Deverá fornecer a documentação de como planejou e executou a carga dos dados, justificando as escolhas tomadas.

### 2. Criação da API REST em Go

**API REST:**
- Desenvolver uma API REST em Go que permita a consulta ao banco de dados Neo4J. A API deve expor endpoints que respondam algumas perguntas de forma parametrizável.

**Perguntas:**
1. Qual foi o total acumulado de casos e mortes de Covid-19 em um país específico em uma data determinada?
2. Quantas pessoas foram vacinadas com pelo menos uma dose em um determinado país em uma data específica?
3. Quais foram as vacinas usadas em um determinado país e em que data elas começaram a ser aplicadas?
4. Qual país registrou o maior número de casos acumulados até uma data específica?
5. Qual foi a vacina mais utilizada em uma região específica?

### 3. Entrega e Documentação

**Código-Fonte:**
- Para a entrega do teste, deverá ser feito um fork deste repositório para a conta da pessoa candidata a vaga, no github. 
- A pessoa deve adicionar um arquivo markdown ou orgmode ao seu repositório fornecendo instruções claras de como rodar o ambiente de desenvolvimento e realizar os testes necessários.

**Artefatos de Software:**
- A REST API e demais programas desenvolvidos devem ser encapsulados em containers Docker. 
- Recomenda-se o uso de docker compose e Makefile para a orquestração de tudo, API, Neo4J, ETL, etc.

**Documentação:**
- A pessoa candidata deve incluir uma documentação detalhada explicando a abordagem tomada para a carga dos dados, como a API foi implementada, e as decisões técnicas mais importantes. 
- Devem ser fornecidos exemplos de uso dos endpoints da API. Recomenda-se o uso de OpenAPI.

**Considerações de Performance:**
- A pessoa candidata deve evidenciar como garantiria a performance e escalabilidade da API em um ambiente de produção, considerando o volume de dados e as consultas realizadas.

## Avaliação
O teste será avaliado considerando os seguintes critérios:

- **Proficiência Técnica:** Qualidade e clareza do código em Go, uso adequado de técnicas e ferramentas.
- **Adaptação aos Grafos:** Implementação correta e eficiente das perguntas utilizando Neo4J e cypher query.
- **Qualidade de Código** Cobertura de testes e técnicas utilizadas.
- **Documentação:** Qualidade da documentação e clareza na explicação das escolhas técnicas.

## Considerações Finais
Este teste simula um cenário real que a pessoa candidata poderá enfrentar na posição. O foco não está apenas na solução técnica, mas também na habilidade em justificar suas decisões e produzir um código que seja eficiente e escalável.

## Anexos: 
[Especificação do modelo](./spec/README.md)

