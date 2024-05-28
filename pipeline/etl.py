# https://duckdb.org/docs/guides/python/execute_sql


import pandas as pd 
import duckdb

def etl_reclamacoes(nm_file):

    query = f"""
        SELECT 
            DataExtracao AS DATA_EXTRACAO,
            SOLICITAÇÕES AS SOLICITACOES,
            Ano          AS ANO,
            Mês          AS MES,
            AnoMês       AS ANO_MES,
            UF,
            Cidade          AS CIDADE,
            CO_MUNICIPIO    AS COD_MUNICIPIO,
            CanalEntrada    AS CANAL_ENTRADA,
            Condição        AS CONDICAO,
            TipoAtendimento AS TIPO_ATENDIMENTO,
            Serviço         AS SERVICO,
            UPPER(Marca)    AS OPERADORAS,
            Assunto         AS ASSUNTO,
            Problema        AS PROBLEMA
        FROM (SELECT * FROM main.read_csv('{nm_file}'))
        WHERE (
            Ano >= 2022 
            AND Serviço ='SCM' 
            AND TipoAtendimento = 'Reclamação'
            )
    """
    try:
        dados = duckdb.sql(query).df()
        
    except ValueError as e:
        print(f'Erro ao ler o arquivo: {e}')
    return dados

