

# TODO(rodrigo): assume que pais eh o time (?)
# FIXME(fakegermano): se tem qpais, eh so retornar qpais
def get_time(qn_id, qtipo_doc, qpais):
    format_str = """
    SELECT pais
    FROM jogador
    WHERE n_id={n_id} AND tipo_doc={tipo_doc} AND pais={pais}
    """
    sql_cmd = format_str.format(n_id=qn_id, tipo_doc=qtipo_doc, pais=qpais)
    return sql_cmd


# FIXME(fakegermano): se tenho qpais nao precisa da query pra pegar o pais
def get_tecnico(qn_id, qtipo_doc, qpais):
    """
    Funcao que retorna uma string com a sql query para o tecnico que treina o jogador
    :param qn_id: int
    :param qtipo_doc: str
    :param qpais: str
    :return: str
    """
    format_str = """
      SELECT *
      FROM tecnico
      INNER JOIN (
        SELECT pais
        FROM jogador
        WHERE n_id={n_id} AND tipo_doc={tipo_doc} AND pais={pais}
      ) ON pais.jogador=pais.tecnico
    """
    sql_cmd = format_str.format(n_id=qn_id, tipo_doc=qtipo_doc, pais=qpais)
    return sql_cmd


# TODO(rodrigograca): assume que os jogadores cadastrados todos fazem parte da copa (?)
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
