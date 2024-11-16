import pandas as pd
import os
import glob

# caminho para ler os arquivos
folder_path = 'src\\data\\raw'

# listar todos os arquivos csv
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

if not csv_files:
    print('Nenhum arquivo csv encontrado')

else:
    
    # dataframe = tabela na memória para guardar o conteúdo dos arquivos
    dfs = []

    for csv_file in csv_files:

        try:
            # lendo o arquivo csv
            df_temp = pd.read_csv(csv_file, delimiter=',')

            # pegar o nome do arquivo
            file_name = os.path.basename(csv_file)
            
            if '1960' in file_name:
                df_temp['year_competition'] = '1960'
            elif '1964' in file_name:
                df_temp['year_competition'] = '1964'
            elif '1968' in file_name:
                df_temp['year_competition'] = '1968'
            elif '1972' in file_name:
                df_temp['year_competition'] = '1972'
            elif '1976' in file_name:
                df_temp['year_competition'] = '1976'
            elif '1980' in file_name:
                df_temp['year_competition'] = '1980'
            elif '1984' in file_name:
                df_temp['year_competition'] = '1984'
            elif '1988' in file_name:
                df_temp['year_competition'] = '1988'
            elif '1992' in file_name:
                df_temp['year_competition'] = '1992'
            elif '1996' in file_name:
                df_temp['year_competition'] = '1996'
            elif '2000' in file_name:
                df_temp['year_competition'] = '2000'
            elif '2004' in file_name:
                df_temp['year_competition'] = '2004'
            elif '2008' in file_name:
                df_temp['year_competition'] = '2008'
            elif '2012' in file_name:
                df_temp['year_competition'] = '2012'
            elif '2016' in file_name:
                df_temp['year_competition'] = '2016'
            elif '2020' in file_name:
                df_temp['year_competition'] = '2020'
            elif '2024' in file_name:
                df_temp['year_competition'] = '2024'

            # guarda dados tratados dentro de um dataframe
            dfs.append(df_temp)
    
        except Exception as e:
            print(f'Erro ao ler o arquivo {csv_file} : {e}')

if dfs:

    # concatena todas as tabelas salvas no dfs em uma unica tabela
    result = pd.concat(dfs, ignore_index=True)

    # caminho de saída
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')

    # configura o motor de escrita
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # leva os dados do resultado a serem escritos no motor de excel configurado
    result.to_excel(writer, index=False)

    # salva o arquivo excel
    writer.close()
else:
    print('Nenhum dado para ser salvo')