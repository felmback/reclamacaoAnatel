#https://posit-dev.github.io/great-tables/examples/

import pandas as pd
from great_tables import GT, system_fonts



dados = pd.read_csv(r'pipeline\reclamacao\reclamacoes_contexto.csv', sep=';')

df = dados.copy()
ano = '2023'
servico = 'SCM'
atedimento = 'Reclamação'

df.query(f"Ano == {ano} and Serviço == '{servico}' and TipoAtendimento == '{atedimento}'", inplace=True)

#tabela de marca vs mes
df_op_ano = df.pivot_table(index='Marca', columns='Mês', values='SOLICITAÇÕES', aggfunc='sum')


df_op_ano['Total'] = df_op_ano.sum(axis=1)

df_op_ano = (df_op_ano.sort_values(by='Total', ascending=False) )
df_op_ano['%'] = ((df_op_ano['Total'] / df_op_ano['Total'].sum()) * 100)
df_op_ano['%'] = df_op_ano['%'].map('{:.2f}'.format).str.replace('.', ',') + '%'

col_df_op_ano = df_op_ano.columns.to_list()

tbl_periodo = (

    GT(df_op_ano.reset_index(),rowname_col='Marca')
        .fmt_number(columns=col_df_op_ano[0],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[1],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[2],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[3],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[4],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[5],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[6],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[7],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[8],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[9],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[10],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[11],locale='pt',decimals=0)
        .fmt_number(columns=col_df_op_ano[12],locale='pt',decimals=0)

        .data_color(
                columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                domain=[12000, 1],
                palette=["#EC6C6C", "#ECAC6C", "#ECDE6C", "white"],
                na_color="white",
            )
         .data_color(
                columns=["Total"],
                domain=[105000,0],
                palette= ["#EC6C6C", "#ECAC6C", "#ECDE6C", "#9CCEAF"],
                na_color="white",
            )

         .data_color(
                columns=["%"],
                # domain=[105000,0],
                palette=["red", "orange", "yellow", "green"],
                na_color="white",
            )
        .tab_options(
                source_notes_font_size='x-small',
                source_notes_padding=3,
                table_font_names=system_fonts("humanist"),
                data_row_padding_horizontal=3,
                column_labels_padding_horizontal=58
        ) 
        .tab_header(
            title="Volume de Solicitações registradas na Anatel - SCM (Banda Larga)",
            subtitle="Solicitações por Operadora e Mês no Ano 2023",
            )
        .cols_align(
            columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "Total"],
            align="center",
        )
         .cols_align(
            columns=["Marca"],
            align="right",
        )
)


#tabla de assuntos
df_assunto= df.pivot_table(index='Marca', columns='Assunto', values='SOLICITAÇÕES', aggfunc='sum')

df_assunto['Total'] = df_assunto.sum(axis=1)

df_assunto = (df_assunto.sort_values(by='Total', ascending=False) )
df_assunto['%'] = ((df_assunto['Total'] / df_assunto['Total'].sum()) * 100)
df_assunto['%'] = df_assunto['%'].map('{:.2f}'.format).str.replace('.', ',') + '%'

col_assunto = df_assunto.columns.to_list()

tbl_assunto = (
    GT(df_assunto.reset_index(),rowname_col='Marca')
        .fmt_number(columns =col_assunto[0] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[1] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[2] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[3] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[4] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[5] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[6] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[7] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[8] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[9] ,locale='pt',decimals=0)
        .fmt_number(columns =col_assunto[10] ,locale='pt',decimals=0)
        .data_color(
                columns= col_assunto,
                domain=[46000, 0],
                palette=["#EC6C6C", "#ECAC6C", "#ECDE6C", "white"],
                na_color="white",
            )
         .data_color(
                columns=["Total"],
                domain=[105000,0],
                palette= ["#EC6C6C", "#ECAC6C", "#ECDE6C", "#9CCEAF"],
                na_color="white",
            )

         .data_color(
                columns=["%"],
                # domain=[105000,0],
                palette=["red", "orange", "yellow", "green"],
                na_color="white",
            )
        .tab_options(
                source_notes_font_size='x-small',
                source_notes_padding=3,
                table_font_names=system_fonts("humanist"),
                data_row_padding_horizontal=3,
                column_labels_padding_horizontal=58
        ) 
        .tab_header(
            title = "Volume de Solicitações registradas na Anatel - SCM (Banda Larga)",
            subtitle = "Tipo de Solicitação feita na entrevista",
            )
        .cols_align(
            columns = col_assunto,
            align="center",
        )
         .cols_align(
            columns = ["Marca"],
            align="right",
        )
)


#grafico de barras , solicitações por uf
ufs = df.groupby(['UF'])['SOLICITAÇÕES'].sum().sort_values(ascending=False)
ufs.plot(kind='bar',cmap='viridis')

# teste = df.pivot_table(index='Marca', columns='Mês', values='SOLICITAÇÕES', aggfunc='sum')
# teste.corr( method='pearson' )





































# dados = pd.read_csv(r'pipeline\reclamacao\reclamacoes_contexto.csv', sep=';')

# df = dados.copy()

# df_op_ano = df.pivot_table(index='Marca', columns='Ano', values='SOLICITAÇÕES', aggfunc='sum')

# df_op_ano['TOTAL_SOLICITACOES'] = df_op_ano.sum(axis=1)

# df_op_ano = (df_op_ano.sort_values(by='TOTAL_SOLICITACOES', ascending=False) )


# df_op_ano = df_op_ano.drop(columns='TOTAL_SOLICITACOES')