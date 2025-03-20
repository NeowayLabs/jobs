# Teste Prático: Desenvolvimento Backend com Banco de Dados Neo4J

## Objetivo:
Avaliar a proficiência da pessoa candidata na linguagem Go, manipulação de bancos de dados e a capacidade de trabalhar com dados utilizando o Neo4J.

## Descrição Geral:
A pessoa candidata deve baixar a especificação desse projeto e realizar a carga dos dados de exemplo no banco de dados Neo4J.
Com base no modelo de grafos especificado e nos dados de exemplo carregados, a pessoa candidata deve:
    1. Implementar uma ETL para carga de dados no formato csv usando o método que desejar.
    2. Implementar uma api REST de acesso ao Neo4j para responder uma série de perguntas parametrizáveis pelo usuário.
Testes devem ser implementados para a garantia da qualidade da entrega.

## Instruções

### 1. Preparação dos Dados

**Processamento e Carga no Neo4J:**
- Com base no modelo anexo ao final do descritivo e nos dados de exemplo carregados:
- Gerar arquivos csv que preencham as condições definidas no modelo de dados. Os dados podem ser baixados de alguma fonte pública ou até mesmo gerados aleatóriamente.
- Realizar a carga desses dados para o Neo4J. Utilizando a ferramenta de ETL desenvolvida.
- Deverá fornecer a documentação de como planejou e executou a carga dos dados, justificando as escolhas tomadas.

### 2. Criação da API REST

**API REST:**
- Desenvolver uma API REST que permita a consulta ao banco de dados Neo4J. A API deve expor endpoints que respondam algumas perguntas de forma parametrizável.

**Perguntas:**
1. Qual foi o total acumulado de casos e mortes de Covid-19 em um país específico em uma data determinada?
2. Quantas pessoas foram vacinadas com pelo menos uma dose em um determinado país em uma data específica?
3. Quais vacinas foram usadas em um país específico?
4. Em quais datas as vacinas foram autorizadas para uso?
5. Quais países usaram uma vacina específica?

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
- O Banco de dados deve estar devidamente indexado para garantir a performance das consultas.

## Avaliação
O teste será avaliado considerando os seguintes critérios:

- **Proficiência Técnica:** Qualidade e clareza do código, uso adequado de técnicas e ferramentas.
- **Adaptação aos Grafos:** Implementação correta e eficiente das perguntas utilizando Neo4J e cypher query.
- **Qualidade de Código** Cobertura de testes e técnicas utilizadas.
- **Documentação:** Qualidade da documentação e clareza na explicação das escolhas técnicas.

## Considerações Finais
Este teste simula um cenário real que a pessoa candidata poderá enfrentar na posição. O foco não está apenas na solução técnica, mas também na habilidade em justificar suas decisões e produzir um código que seja simples, eficiente e escalável.

## Anexos: 
[Especificação do modelo](./spec/analyst/README.md)

