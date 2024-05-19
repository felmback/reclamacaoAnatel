import zipfile
import os

# path_root = os.path.dirname(os.path.abspath(__file__))
# zip_file  = os.path.join(path_root, "consumidor_reclamacoes.zip")
# file_to_extract  = "reclamacoes_contexto.csv"
# extracted_folder = os.path.join(path_root, "reclamacao")

def extract_csv_from_zip(zip_file, file_to_extract, extracted_folder):
    if not os.path.exists(zip_file):
        print(f"O arquivo zip '{zip_file}' não existe.")
        return
    
    if not os.path.exists(extracted_folder):
        os.makedirs(extracted_folder,exist_ok=True)

    try:
        # Abre o arquivo zip
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extract(file_to_extract, path=extracted_folder)
            print(f"Arquivo '{file_to_extract}' extraído com sucesso para '{extracted_folder}'.")
    except Exception as e:
        print(f"Erro ao extrair o arquivo CSV: {e}")

# extract_csv_from_zip(zip_file, file_to_extract, extracted_folder)
