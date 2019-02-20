Exercício
=========

Objetivo
--------

O objetivo desse exercício é nos ajudar a conhecer melhor as suas
habilidades de desenvolvimento, bem como lhe apresentar um pouco dos
desafios que você enfrentará no dia a dia na missão de ajudar o time
de *Analytics* ser mais produtivo.

O Problema
----------

O time de *Product Data Science* desenvolveu dezenas de modelos que
rodam mensalmente em *batch*, o processo de classificação é disparado
utilizando um *scheduler*, no caso o [apache
airflow](https://airflow.apache.org).

Cada classificador de modelo (job) é responsável em acessar variadas
fontes de dados, executar a classificação de fato, e gerar arquivos
json no sistema de arquivos do scheduler. A convenção
[jsonlines](http://jsonlines.org) é utilizada em todos os projetos. Um
exemplo desse arquivo é:

```json
{ "pk": "123", "score": "100" }
{ "pk": "321", "score": "1" }
{ "pk": "50", "score": "98" }
```

Para que o resultado do esforço dos cientistas de dados ganhe valor,
esses dados devem ser injetados na plataforma para que outras
aplicações façam uso desses indicadores. O meio de persistência é de
sua escolha: apenas em memória *RAM* durante a execução, arquivo de
texto ou um banco de dados como *SQLite* ou *PostgreSQL*. Mas note que
aprioridade desse teste é a integração do pipeline proposto.

A Missão
--------

* Desenvolver o serviço http que receberá esses dados e irá
  persistí-los. O serviço também deverá permitir a consulta
  dos valores previamente guardados.

* Desenvolver um cliente pra esse serviço que receba como entrada um
  diretório contendo arquivos com os dados e envie para o serviço
  http. Deverá conter um comando a parte também para consulta baseado
  no atributo `pk`.

Considerações
-------------

Atente para algumas considerações importantes:


* Não existe resposta correta, o que procuramos é entender a sua
  capacidade de solucionar o problema e sua criatividade.

* A linguagem de programação comumente utilizada pelo time é
[python3](https://www.python.org), utilizar python vai facilitar a
manutenção do software, mas se você for mais versado em outra
linguagem como Go ou outras, fique à vontade.

* [Docker](https://www.docker.com/) é largamente utilizado e
gostaríamos muito de ver as suas habilidades com essa ferramenta.

* Testar é legal! :) Gostamos de testes unitários.

* Mostre-nos também tudo o que você sabe sobre boas práticas de
  [git](https://git-scm.com).

* Pense sempre na qualidade do código, tenha a manutenibilidade,
legibilidade esimplicidade em mente. Lute contra
[overengineering](https://en.wikipedia.org/wiki/Overengineering)!

* Lembre que são vários modelos, e cada modelo gera uma grande volume
  de dados, temos um recorde de cerca de 4,5 GB.

* É desejável que consigamos executar o seu trabalho em laboratório,
  portanto, portabilidade do seu software é algo essencial.
