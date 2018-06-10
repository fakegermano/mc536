def get_partidas(qn_id, qtipo_doc, qpais):
    """
    Funcao que retorna uma string com a query sql para as partidas que um comentarista narrou
    :param qn_id: int
    :param qtipo_doc: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT pais1,pais2,rodada
      FROM narra
      WHERE n_id=\"{n_id}\" AND tipo_doc=\"{tipo_doc}\" AND pais=\"{pais}\"
    """
    sql_cmd = format_str.format(n_id=qn_id, tipo_doc=qtipo_doc, pais=qpais)
    return sql_cmd


# TODO(rodrigograca): assume que todos os comentaristas que estao no db estao na copa (?)
def get_all():
    """
    Funcao que retorna uma string com a query sql para todos os comentaristas da copa
    :return: str
    """
    format_str = """
      SELECT * FROM comentarista
    """
    sql_cmd = format_str.format()
    return sql_cmd