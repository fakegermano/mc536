def get_comentaristas_narrando_brasil():
    format_str = """
      SELECT "num_ID","tipo_ID","pais"
      FROM narra
      WHERE "pais1"={pais} OR "pais2"={pais}

    """
    sql_cmd = format_str.format(pais='Brazil')
    return sql_cmd


def get_torcedores_nao_assistiram_brasil():
    format_str = """
      SELECT "num_ID","tipo_ID","pais"
      FROM assiste
      WHERE "pais1"!={pais} AND "pais2"!={pais}
    """
    sql_cmd = format_str.format(pais='Brazil')
    return sql_cmd


# FIXME(dgtravieso) pega jogadores de ataque e defesa.
def get_defesa_sem_cartao():
    format_str = """
      SELECT "num_ID","tipo_ID","pais"
      FROM jogador
      WHERE "cartoes_amarelos"=0 AND "cartoes_vermelhos"=0
    """
    sql_cmd = format_str.format(pais='Brazil')
    return sql_cmd


# FIXME (fakegermano) : Funcao count nao funciona com 3 argumentos
def get_partida_menos_2000_assistiram():
    format_str = """
      SELECT "pais1", "pais2", "rodada", count("pais1", "pais2", "rodada") as "num_torcedores"
      FROM assiste
      WHERE "num_torcedores" > 2000
      GROUP BY "pais1", "pais2", "rodada";
    """
    sql_cmd = format_str.format()
    return sql_cmd


# TODO(fakegermano): Esta query retorna a cidade/estado com menos de 2 partidas e nao o estadio
# FIXME(fakegermano): funcao count nao funciona com 2 argumentos
def get_estadio_menos_2_partidas():
    format_str = """
      SELECT cidade,estado,count(cidade,estado) as num_partidas
      FROM partida
      WHERE num_partidas > 2
      GROUP BY cidade,estado;
    """
    sql_cmd = format_str.format()
    return sql_cmd


# FIXME(fakegermano): E.pais1, E.pais2 e E.rodada nao existem
def get_estadio_arbitro_brasileiro_apita():
    format_str = """
      SELECT *
      FROM estadio AS E
        INNER JOIN apita AS A ON E."pais1"=A."pais1" AND E."pais2"=A."pais2" AND E."rodada"=A."rodada";
      WHERE "pais"={pais}
    """
    sql_cmd = format_str.format(pais='Brazil')
    return sql_cmd


# TODO(fakegermano): mudei a query para ser cartoes_vermelhos >= 1
# TODO(fakegermano): query retorna vazio pois nao temos jogadores com mais de 0 cartoes vermelhos no bd
# estava cartoes_vermelhos=1 OR cartoes_vermelhos=2 (?)
def get_jogadores_com_cartao_vermelho():
    format_str = """
      SELECT "num_ID","tipo_ID","pais"
      FROM jogador
      WHERE "cartoes_vermelhos">=1
    """
    sql_cmd = format_str.format()
    return sql_cmd


# TODO(fakegermano): query retorna vazio pois nao temos jogadores com mais de 0 gols no bd
def get_jogador_com_mais_de_3_gosl():
    format_str = """
      SELECT "num_ID","tipo_ID","pais"
      FROM jogador_ataque
      WHERE "gols">=3
    """
    sql_cmd = format_str.format()
    return sql_cmd


# TODO(fakegermano): query retorna vazio pois nao temos estadios com menos que 35212 lugares (minimo do bd)
def get_estadio_com_capacidade_menor_30000():
    format_str = """
      SELECT *
      FROM estadio
      WHERE capacidade<30000
    """
    sql_cmd = format_str.format()
    return sql_cmd


def get_times_com_menos_10_cartoes_amarelos():
    format_str = """
      SELECT "pais" FROM
        (SELECT "pais", SUM("cartoes_amarelos") AS "soma_amarelos"
          FROM jogador
          GROUP BY "pais"
        ) AS cartoes_somados
      WHERE "soma_amarelos"<10
"""
    sql_cmd = format_str.format()
    return sql_cmd


def get_arbitro_mais_de_3_bandeirinha():
    format_str = """
      SELECT "num_ID", "tipo_ID", "pais" FROM
        (SELECT arbitro."num_ID", arbitro."tipo_ID", arbitro."pais", count(apita."num_ID") as "contagem"
          FROM arbitro
          INNER JOIN apita ON arbitro."num_ID" = apita."num_ID" AND arbitro."tipo_ID" = apita."tipo_ID" AND arbitro."pais" = apita."pais"
          WHERE funcao='Bandeirinha'
          GROUP BY arbitro."num_ID",arbitro."tipo_ID", arbitro."pais") AS "com_contagem"
      WHERE "contagem">3
    """
    sql_cmd = format_str.format(funcao='Bandeirinha')
    return sql_cmd


# FIXME(fakegermano) query completamente confusa, nao consegui testar e nem confirmar como pode estar correto
def get_comentaristas_narraram_partidas_4_4_3():
    format_str = """
      SELECT TN.num_ID, TN.tipo_ID, TN.pais, TN.formacao as formacao1, T2.formacao as formacao2
      FROM (narra as N inner join time_futebol as T1 on N.pais1 = T1.pais as pais1) as TN 
        INNER JOIN time_futebol as T2 on TN.pais2 = T2.pais as pais2
      WHERE formacao1 = {formacao} OR formacao2 = {formacao}
    """
    sql_cmd = format_str.format(formacao="4-4-3")
    return sql_cmd