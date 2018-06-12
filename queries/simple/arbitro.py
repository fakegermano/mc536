

def get_partidas(qnum_ID, qtipo_ID, qpais):
    """
    Retorna uma string com a query sql para as partidas que o arbitro apitou
    :param qnum_ID: int
    :param qtipo_ID: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT "pais1","pais2","rodada"
      FROM apita
      WHERE "num_ID"={num_ID} AND "tipo_ID"={tipo_ID} AND "pais"={pais}
    """
    sql_cmd = format_str.format(num_ID=qnum_ID, tipo_ID=qtipo_ID, pais=qpais)
    return sql_cmd


def get_all():
    """
    Retorna uma string com a query sql para todos os arbitros da copa
    :return: str
    """
    format_str = """
      SELECT * FROM arbitro
    """
    sql_cmd = format_str.format()
    return sql_cmd

