from bot_busca_localidade_e_faixa_de_cep import *
def test_request():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    dados_post = {'UF':'SP'}
    r = requests.post("https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm", data=dados_post, headers=header)
    assert r.status_code == 200

tipo_bs4_element_resultset = 'bs4.element.ResultSet()'
def test_retornar_tabela():
    request_SP = request('SP')
    tabelas = retornar_tabela(request_SP)
    assert (tabelas.__class__.__name__) =='ResultSet'

def test_retornar_UF():
    request_SP = request('SP')
    tabelas = retornar_tabela(request_SP)
    ID_UF = retornar_uf(tabelas)
    assert ID_UF == 'SP'

def test_retornar_json_final():
    request_SP = request('SP')
    tabelas = retornar_tabela(request_SP)
    ID_UF = retornar_uf(tabelas)
    obj_json_final = retornar_json(tabelas, ID_UF)
    assert len(obj_json_final) != 0
