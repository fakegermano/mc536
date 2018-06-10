def get_partidas(qnum_ID, qtipo_ID, qpais):
    """
    Funcao que retorna uma string com a query sql para as partidas que um comentarista narrou
    :param qnum_ID: int
    :param qtipo_ID: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT "pais1","pais2","rodada"
      FROM narra
      WHERE "num_ID"={num_ID} AND "tipo_ID"={tipo_ID} AND "pais"={pais}
    """
    sql_cmd = format_str.format(num_ID=qnum_ID, tipo_ID=qtipo_ID, pais=qpais)
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