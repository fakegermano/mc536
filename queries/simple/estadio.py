def get_partidas(qcidade, qestado):
    """
    Funcao que retorna uma string com a sql query para todas as partidas que ocorreram no estadio
    :param qcidade: str
    :param qestado: str
    :return: str
    """
    format_str = """
      SELECT "pais1","pais2","rodada"
      FROM partida
      WHERE "cidade"={cidade} AND "estado"={estado}
    """
    sql_cmd = format_str.format(cidade=qcidade, estado=qestado)
    return sql_cmd


def get_all():
    """
    Funcao que retorna uma string com a sql query para todos os estadios da copa
    :return: str
    """
    format_str = """
        SELECT * FROM estadio
    """
    sql_cmd = format_str.format()
    return sql_cmd
