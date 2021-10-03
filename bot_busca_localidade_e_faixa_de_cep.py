from bs4 import BeautifulSoup as bs
import requests
import json
import os
import logging

os.system("cls")

def request(UF):
    """
    Essa função tem a responsabilidade de executar um método post no endereço da url.
    Já que o intuito é apenas para a url específica, não houve intenção de exigir a declaração
    desse parâmetro na chamada da função.
    Para assegurar o parse de uma estrutura previsível, foi utilizado como User-Agent o navegador firefox
    na versão 5. Conforme informações de header abaixo. 
    """

    #informações de cabeçalho
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}

    #Dados necessário para o post. Também é possível especificar a cidade
    #Adicionando uma segunda segunda chave de nome Localidade. 
    #Ex: dados_post = {'UF':'SP','Localidade':'sao paulo'}
    dados_post = {'UF':UF}
    try:
        r = requests.post("https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm", data=dados_post, headers=header)
        html_parser = bs(r.content, 'html.parser')
    except TypeError:
        print("Passe como parâmetro uma sigla de estado válida.")
    except:
        print("Não foi possível fazer a requisição. Status diferente de 200. Status:{status}".format(status=r.status_code))

    return html_parser

def retornar_tabela(html_parser):
    """
    Essa função tem a resposabilidade de buscar todas as tabelas do html que
    sejam da classe tmptabela.
    Retorno: Lista de todas as tabelas que satisfaçam os requisitos mencionados.
    """
    try:
        html_find_all_table = html_parser.find_all("table", class_='tmptabela')
    except:
        print("Não foi possível fazer o find_all por table e class tmptabela. Reveja os parâmetros de busca.")
        
    return html_find_all_table

def retornar_uf(html_find_all_table):
    """
    Essa função tem a resposabilidade de capturar a sigla da estado/unidade federativa
    na qual fizemos a busca.

    Como existem 2 tabela de classe tmptabela. A primeira tabela, de index 0, é a tabela que se encontra
    a sigla da UF.
    """
    try:
        #html_find_all_table é um objeto do tipo ...
        #o métrodo itera e retorna as tags filhas como objetos do tipo ... ou ...
        #como os objetos do tipo... não trazem informações pertinentes elas são despresadas.
        tag_table_children = [linha for linha in html_find_all_table[0].children if linha.__class__.__name__!='NavigableString']
        
        #Em cada linha (objeto do tipo ...) filtrados por todas tags td (célula da tabela)
        tag_tb = [td_tag.find_all('td') for td_tag in tag_table_children]

        #o atributo string retorna o nome da tag/celula selecionada.
        UF = tag_tb[1][0].string
        return UF
    except (UnboundLocalError, IndexError) as e:
        print(\
            "Não foi possível iterar sobre o objeto tag ou a lista está vazia. \n\
Reveja o tipo e o tamanho do parâmetro de entrada")
    

def retornar_json(html_find_all_table, UF):

    """
    Essa função tem a resposabilidade de capturar as linhas da segunda tabela.
    Na primeira list comprehensions, apenas os objetos do tipo ... são extraídos.
    Os objetos NavigableString não contém as informações de localidade e faixa de cep.
    """
    try:
        #retona todas as tags filhas da tabela
        tag_table_children = [linha for linha in html_find_all_table[1].children if linha.__class__.__name__!='NavigableString']
        #retona uma lista de todas as tags td (células) contradas nas tags filhas (linhas das tabela)
        tag_tb = [td_tag.find_all('td') for td_tag in tag_table_children]

        #armazena cada cojunto localidade e faixa de cep como um dicionário em uma lista.
        #OBS: lstrip() foi acionado para remover um espaço em branco presente em todos registros
        #de faixa de cep.
        obj_estado_cep_lista = [\
            {"localidade":tab_tb_string[0].string,\
                "faixa_de_cep":tab_tb_string[1].string.lstrip()} \
                    for tab_tb_string in tag_tb if len(tab_tb_string)!=0]
        
        obj_estado_cep_Lista_unica = {elemento_estado_cep["localidade"]:elemento_estado_cep \
            for elemento_estado_cep in obj_estado_cep_lista}.values()
        #dicionário que será convertido em json
        dict_obj_cidade_cep = {}
        
        #Valor inicial do id
        id = 1
        
        #UF recebe a UF retornada pela função ....
        ID_UF = UF
        
        #itera sobre a lista dos objetos {localidade:estado,faixa_de_cep: cep_inicial a cep_final}
        for elemento_estado_cep_unico in obj_estado_cep_Lista_unica:

            #o ID é concatenado com a sigla para formar uma chave composta única identificadora localidade
            dict_obj_cidade_cep[ID_UF+str(id)] = elemento_estado_cep_unico
            
            #o id é incremental em 1
            id+=1
        
        #cria o json exigido como requisito
        #o argumento indet=4 formata o json com espaçamento 4
        #ensure_ascii mantém os caracteres látinos pós dump
        json_final = json.dumps(dict_obj_cidade_cep, indent=4, ensure_ascii=False)
        
        #retorna o json
        return json_final
    except (UnboundLocalError, IndexError) as e:
        print(\
            "Não foi possível iterar sobre o objeto tag, lista está vazia ou sigla inválida. \n\
Reveja o tipo e o tamanho dos parâmetros de entrada")
    
def gravar_json(path, file_name, obj_json):
    with open(path+file_name, mode='w', encoding='utf-8') as open_json:
        open_json.write(obj_json)


# --------------------------- BUSCA PARA SP ---------------------
request_SP = request('SP')
tabelas = retornar_tabela(request_SP)
ID_UF = retornar_uf(tabelas)
obj_json_final = retornar_json(tabelas, ID_UF)
print(obj_json_final)
gravar_json(r'.\\',"faixas_cep_SP.txt",obj_json_final)

# --------------------------- BUSCA PARA RJ -----------------------
request_SP = request('RJ')
tabelas = retornar_tabela(request_SP)
ID_UF = retornar_uf(tabelas)
obj_json_final = retornar_json(tabelas, ID_UF)
print(obj_json_final)
gravar_json(r'.\\',"faixas_cep_RJ.txt",obj_json_final)

# --------------------------- BUSCA VAZIA - TESTE ------------------
# request_SP = request(1.2)
# tabelas = retorna_tabela(request_SP)
# ID_UF = retorna_uf(tabelas)   
# obj_json_final = retorna_json(tabelas, ID_UF)
# print(obj_json_final)