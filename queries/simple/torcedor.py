def get_time(qnum_ID, qtipo_ID, qpais):
    """
    Funcao que retorna string com sql query para o time que o torcedor torce para
    :param qnum_ID: int
    :param qtipo_ID: str
    :param qpais: str
    :return: str
    """
    format_str = """
    SELECT "torce_pais"
    FROM torcedor
    WHERE "num_ID"={num_ID} AND "tipo_ID"={tipo_ID} AND "pais"={pais}
    """
    sql_cmd = format_str.format(num_ID=qnum_ID, tipo_ID=qtipo_ID, pais=qpais)
    return sql_cmd


def get_partidas_assistidas(qnum_ID, qtipo_ID, qpais):
    """
    Funcao que retorna string com sql query para as partidas assistidas pelo torcedor
    :param qnum_ID: int
    :param qtipo_ID: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT "pais1","pais2","rodada"
      FROM assiste
      WHERE "num_ID"={num_ID} AND "tipo_ID"={tipo_ID} AND "pais"={pais}
    """
    sql_cmd = format_str.format(num_ID=qnum_ID, tipo_ID=qtipo_ID, pais=qpais)
    return sql_cmd


def get_all():
    """
    Funcao que retorna string com sql query para todos os torcedores da copa
    :return: str
    """
    format_str = """
    SELECT * FROM torcedor
    """
    sql_cmd = format_str.format()
    return sql_cmd
