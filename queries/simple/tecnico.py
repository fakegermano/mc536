

# TODO(rodrigograca): se o pais do tecnico eh o time que ele torce (?)
# TODO(fixme): so retornar o qpais tambem eh solucao?
# FIXME(fakegermano): remover atributos nao usados
def get_time(qn_id, qtipo_doc, qpais):
    """
    Funcao que retorna string com a sql query para o time que o tecnico treina
    :param qn_id: int
    :param qtipo_doc: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT pais
      FROM tecnico
      WHERE pais={pais}
    """
    sql_cmd = format_str.format(pais=qpais)
    return sql_cmd


# FIXME(fakegermano): remover atributos nao usados
def get_jogadores(qn_id, qtipo_doc, qpais):
    """
    Funcao que retorna string com a sql query para os jogadores que o tecnico treina
    :param qn_id: int
    :param qtipo_doc: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT n_id,tipo_doc,pais
      FROM jogador
      INNER JOIN (
        SELECT pais
        FROM tecnico
        WHERE pais={pais}
      ) ON pais.jogador=pais.tecnico
    """
    sql_cmd = format_str.format(pais=qpais)
    return sql_cmd


# TODO(rodrigograca): assume todos os tecnicos cadastrados estao na copa (?)
def get_all():
    """
    Funcao que retorna string com sql query para todos os tecnicos da copa
    :return: str
    """
    format_str = """
      SELECT * FROM tecnico
    """
    sql_cmd = format_str.format()
    return sql_cmd
