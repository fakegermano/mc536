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
      SELECT jogador."num_ID",jogador."tipo_ID",jogador."pais"
      FROM jogador
      INNER JOIN jogador_defesa ON jogador."num_ID"=jogador_defesa."num_ID" AND jogador."tipo_ID"=jogador_defesa."tipo_ID" AND jogador."pais"=jogador_defesa."pais"
      WHERE "cartoes_amarelos"=0 AND "cartoes_vermelhos"=0
    """
    sql_cmd = format_str.format(pais='Brazil')
    return sql_cmd


# FIXME (fakegermano) : Query funcional mas todas as partidas que temos tem 23 torcedores
def get_partida_menos_2000_assistiram():
    format_str = """
      SELECT * FROM (
        SELECT "pais1", "pais2", "rodada", count("num_ID") as num_torcedores
        FROM assiste
        GROUP BY "pais1", "pais2", "rodada"
      ) AS torcedores_contados
      WHERE torcedores_contados.num_torcedores < 2000
      ORDER BY "rodada"
    """
    sql_cmd = format_str.format()
    return sql_cmd


# TODO(fakegermano): Esta query retorna a cidade/estado com menos de 2 partidas e nao o estadio
def get_estadio_menos_2_partidas():
    format_str = """
      SELECT * FROM (
        SELECT cidade,estado,count(cidade) as num_partidas
        FROM partida
        GROUP BY cidade,estado
      ) AS partidas_contadas
      WHERE partidas_contadas."num_partidas" < 2
    """
    sql_cmd = format_str.format()
    return sql_cmd


def get_estadio_arbitro_brasileiro_apita():
    format_str = """
      SELECT cidade,estado
FROM partida
INNER JOIN ( SELECT "pais1","pais2",rodada
FROM apita
WHERE "pais"={pais}
)AS aux ON partida."pais1"=aux."pais1" AND partida."pais2"=aux."pais2" AND partida."rodada"=aux."rodada"
GROUP BY cidade, estado
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


# FIXME(fakegermano) acredito que essa query agora funcione. nao temos times com formacao 4-4-3 no bd
# mas testei com 5-3-2 e funcionou (95 resultados aparentemente corretos)
def get_comentaristas_narraram_partidas_4_4_3():
    format_str = """
      SELECT N."num_ID", N."tipo_ID", N."pais"
        FROM narra AS N INNER JOIN time_futebol AS tf1 ON N."pais1"=tf1."pais"
                        INNER JOIN time_futebol AS tf2 ON N."pais2"=tf2."pais" 
      WHERE tf1."formacao"={formacao} OR tf2."formacao"={formacao} 
      GROUP BY tf1."pais", tf2."pais", N."num_ID", N."tipo_ID", N."pais";
    """
    sql_cmd = format_str.format(formacao="4-4-3")
    return sql_cmd