# TODO(rodrigograca): verificar se esta correto
def get_times_contra(qpais):
    """
    Funcao que retorna string com sql query para todos os times que um time joga contra
    :param qpais: str
    :return: str
    """
    format_str = """
    SELECT pais1
    FROM partida
    WHERE pais2={pais}
      UNION
    SELECT pais2
    FROM partida
    WHERE pais1={pais}
    """
    sql_cmd = format_str.format(pais=qpais)
    return sql_cmd


def get_tecnico(qpais):
    """
    Funcao que retorna string com sql query para o tecnico do time/pais
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT *
      FROM tecnico
      WHERE pais={pais}
    """
    sql_cmd = format_str.format(pais=qpais)
    return sql_cmd


def get_jogadores(qpais):
    """
    Funcao que retorna string com sql query para os jogadores do time/pais
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT n_id,tipo_doc,pais
      FROM jogador
      WHERE pais={pais}
    """
    sql_cmd = format_str.format(pais=qpais)
    return sql_cmd


def get_torcedores(qpais):
    """
    Funcao que retorna string com sql query para os torcedores de um time/pais
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT n_id,tipo_doc,pais
      FROM torcepara
      WHERE pais={pais}
    """
    sql_cmd = format_str.format(pais=qpais)
    return sql_cmd


# TODO(rodrigograca): assume que todos os times cadastrados estao na copa?
def get_all():
    """
    Funcao que retorna string com sql query para todos os times da copa
    :return: str
    """
    format_str = """
      SELECT * FROM time_futebol
    """
    sql_cmd = format_str.format(pais=qpais)
    return sql_cmd
