Exercício
=========

Objetivo
--------

O objetivo desse exercício é nos ajudar a conhecer melhor as suas habilidades de desenvolvimento, bem
como lhe apresentar um pouco dos desafios que você enfrentará no dia a dia na missão de ajudar o time
de analytics ser mais produtivo.

O Problema
----------

O time de product data science desenvolveu dezenas de modelos que rodam mensalmente em batch, o processo de
classificação é disparado utilizando um scheduler, no caso o [apache airflow](https://airflow.apache.org).

Cada classificador de modelo (job) é responsável em acessar variadas fontes de dados, executar a classificação
de fato, e gerar arquivos json no sistema de arquivos do scheduler. A convenção [jsonlines](http://jsonlines.org)
é utilizada em todos os projetos. Um exemplo desse arquivo é:

```json
{ "pk": "123", "score": "100" }
{ "pk": "321", "score": "1" }
{ "pk": "50", "score": "98" }
```

Para que o resultado do esforço dos data sciences ganhe valor, esses dados devem ser injetados na plataforma
para que outras aplicações façam uso desses indicadores. Isso é realizado inserindo esses dados num banco
de dados [postgresql](https://www.postgresql.org).

Mas essa banco de dados é mantido por outro time, com muito carinho e esmero, e em um ambiente extremamente
seguro, e não é possível realizar conexão diretamente com esse banco.

Para acessar esse banco de dados é necessário um serviço http, que executará em um ambiente seguro e monitorado
pelo time de **SRE**.

A Missão
--------

* Desenvolver o serviço http que receberá esses dados do modelo e efetuará a inseção no postgresql.

* Desenvolver um cliente pra esse serviço, que receba como entrada um diretório contendo arquivos com os dados
e envie para o serviço http.

Considerações
-------------

Atente para algumas considerações importantes:


* Não existe resposta correta, o que procuramos é entender a sua capacidade de solucionar o problema e sua criatividade

* A linguagem de programação comumente utilizada pelo time é [python3](https://www.python.org), utilizar python
vai facilitar a manutenção do software, mas se você for mais versado em outra linguagem, fique à vontade.

* O banco de dados também é ao seu gosto, mas ter schema é importante. 

* [Docker](https://www.docker.com/) é largamente utilizado e gostaríamos muito de ver as suas habilidades com essa
ferramenta.

* Testar é legal!

* Mostre-nos também tudo o que você sabe sobre boas práticas de [git](https://git-scm.com)
 
* Pense sempre na qualidade do código, tenha a manutenibilidade, legibilidade e simplicidade em mente e lute contra
[overengineering](https://en.wikipedia.org/wiki/Overengineering).

* Lembre que são vários modelos, e cada modelo gera uma grande volume de dados, temos um recorde de 4,5 GB.

* É desejável que consigamos executar o seu trabalho em laboratório.
