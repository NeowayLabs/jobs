# Data Pirates challenge

Welcome to Data Pirates challenge.


## Scenario

Hello! We have a small adventure to explore your skills. In this task you have to scrape data from a website and write the results to a file. You will collect data from 'correios' website.


## Requirements

*  Use the http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm URL;
*  Get data at least two UFs. The more, the better;
*  For each UF, capture at least 200 records (when they exist);
*  Each record **must** contain 3 fields: "localidade", "faixa de cep" and a generated "id" to deduplicate records;
*  The output format must be [JSONL](http://jsonlines.org)

## Deliverable

* :heavy_check_mark: The code should be sent through github with at least a README documentation explaining how to test and run it.

* :heavy_check_mark: It would be REALLY nice if it was hosted in a git repo of your **own**. You can create a new empty project, create a branch and Pull Request it to the new master branch you have just created. Provide the PR URL for us so we can discuss the code :grin:. BUT if you'd rather, just compress this directory and send it back to us.

* :x: **Do not** start a Pull Request to this project.

References:

http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm

http://jsonlines.org

## Pay atention
 * There is no right answer, we want to see how you solve problems.
 * We work mainly with [Python 3](https://www.python.org) and [Go](https://golang.org/), but feel free to use any language you feel more confortable.
 * We use [Docker](https://www.docker.com/) a lot, not required but is a plus.
 * Unit tests are mandatory.
 * Show us that you can use all the git good pratices.
 * Think in the quality of your code, maintenability, legibility and simplicity, avoid overengineering.
 * Its important we can execute your project, so make clear what steps we need to take to run your project.
