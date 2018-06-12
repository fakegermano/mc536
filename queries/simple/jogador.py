

# FIXME(fakegermano): se tem qpais, eh so retornar qpais
def get_time(qnum_ID, qtipo_ID, qpais):
    format_str = """
    SELECT "pais"
    FROM jogador
    WHERE "num_ID"={num_ID} AND "tipo_ID"={tipo_ID} AND "pais"={pais}
    """
    sql_cmd = format_str.format(num_ID=qnum_ID, tipo_ID=qtipo_ID, pais=qpais)
    return sql_cmd


# FIXME(fakegermano): query funciona mas retorna uma coluna a mais com o pais repetido
def get_tecnico(qnum_ID, qtipo_ID, qpais):
    """
    Funcao que retorna uma string com a sql query para o tecnico que treina o jogador
    :param qnum_ID: int
    :param qtipo_ID: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT *
      FROM tecnico
      INNER JOIN (
        SELECT pais
        FROM jogador
        WHERE "num_ID"={num_ID} AND "tipo_ID"={tipo_ID} AND "pais"={pais}
      ) ON jogador."pais"=tecnico."pais"
    """
    sql_cmd = format_str.format(num_ID=qnum_ID, tipo_ID=qtipo_ID, pais=qpais)
    return sql_cmd


def get_all():
    """
    Funcao que retorna uma string com a sql query para todos os jogadores da copa
    :return: str
    """
    format_str = """
      SELECT * FROM jogador
    """
    sql_cmd = format_str.format()
    return sql_cmd
