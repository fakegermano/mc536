def get_time(qn_id, qtipo_doc, qpais):
    """
    Funcao que retorna string com sql query para o time que o torcedor torce para
    :param qn_id: int
    :param qtipo_doc: str
    :param qpais: str
    :return: str
    """
    format_str = """
    SELECT torce_pais
    FROM torcepara
    WHERE n_id=\"{n_id}\" AND tipo_doc=\"{tipo_doc}\" AND pais=\"{pais}\"
    """
    sql_cmd = format_str.format(n_id=qn_id, tipo_doc=qtipo_doc, pais=qpais)
    return sql_cmd


def get_partidas_assistidas(qn_id, qtipo_doc, qpais):
    """
    Funcao que retorna string com sql query para as partidas assistidas pelo torcedor
    :param qn_id: int
    :param qtipo_doc: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT pais1,pais2,rodada
      FROM assiste
      WHERE n_id=\"{n_id}\" AND tipo_doc=\"{tipo_doc}\" AND pais=\"{pais}\"
    """
    sql_cmd = format_str.format(n_id=qn_id, tipo_doc=qtipo_doc, pais=qpais)
    return sql_cmd


# TODO(rodrigograca): assume que todos os torcedores no bd estao nao copa (?)
def get_all():
    """
    Funcao que retorna string com sql query para todos os torcedores da copa
    :return: str
    """
    format_str = """
    SELECT * FROM torcedores
    """
    sql_cmd = format_str.format()
    return sql_cmd
