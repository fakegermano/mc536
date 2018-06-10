def get_estadio(qpaisA, qpaisB, qrodada):
    """
    Funcao que retorna string com a sql query para o estadio da partida
    :param qpaisA: str
    :param qpaisB: str
    :param qrodada: str(?) FIXME(fakegermano): procurar tipo
    :return: str
    """
    format_str = """
      SELECT nome,cidade,capacidade 
      FROM realizadano
      WHERE pais1=\"{paisA}\" AND pais2=\"{paisB}\" AND RODADA=\"{rodada}\"
    """
    sql_cmd = format_str.format(paisA=qpaisA, paisB=qpaisB, rodada=qrodada)
    return sql_cmd


def get_arbitro(qpaisA, qpaisB, qrodada):
    """
    Funcao que retorna string com a sql query para o(s) arbitro(s) que apitou(aram) a partida
    :param qpaisA: str
    :param qpaisB: str
    :param qrodada: str(?) FIXME(fakegermano): procurar tipo
    :return: str
    """
    format_str = """
      SELECT n_id,tipo_doc,pais
      FROM apita
      WHERE pais1=\"{paisA}\" AND pais2=\"{paisB}\" AND RODADA=\"{rodada}\"
    """
    sql_cmd = format_str.format(paisA=qpaisA, paisB=qpaisB, rodada=qrodada)
    return sql_cmd


def get_comentarista(qpaisA, qpaisB, qrodada):
    """
    Funcao que retorna string com a sql query para o(s) comentarista(s) que narrou(aram) a partida
    :param qpaisA: str
    :param qpaisB: str
    :param qrodada: str(?) FIXME(fakegermano): procurar tipo
    :return: str
    """
    format_str = """
      SELECT n_id,tipo_doc,pais
      FROM narra
      WHERE pais1=\"{paisA}\" AND pais2=\"{paisB}\" AND RODADA=\"{rodada}\"
    """
    sql_cmd = format_str.format(paisA=qpaisA, paisB=qpaisB, rodada=qrodada)
    return sql_cmd


def get_torcedores(qpaisA, qpaisB, qrodada):
    """
    Funcao que retorna string com a sql query para os torcedores que assistiram a partida
    :param qpaisA: str
    :param qpaisB: str
    :param qrodada: str(?) FIXME(fakegermano): procurar tipo
    :return: str
    """
    format_str = """
      SELECT n_id,tipo_doc,pais
      FROM assiste
      WHERE pais1=\"{paisA}\" AND pais2=\"{paisB}\" AND RODADA=\"{rodada}\"
    """
    sql_cmd = format_str.format(paisA=qpaisA, paisB=qpaisB, rodada=qrodada)
    return sql_cmd


def get_paises(qpaisA, qpaisB):
    """
    Funcao que retorna string com a sql query para os paises que jogaram a partida
    :param qpaisA: str
    :param qpaisB: str
    :return: str
    """
    format_str = """
      SELECT pais1,pais2
      FROM jogacontra
      WHERE pais1=\"{paisA}\" AND pais2=\"{paisB}\" 
    """
    sql_cmd = format_str.format(paisA=qpaisA, paisB=qpaisB)
    return sql_cmd


# TODO(rodrigograca): assume que todos os objetos partida ocorrem na copa
def get_all():
    """
    Funcao que retorna string com a sql query para todas as partidas da copa
    :return: str
    """
    format_str = """
      SELECT * FROM partida
    """
    sql_cmd = format_str.format()
    return sql_cmd
