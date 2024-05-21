import zipfile
import os

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
            print(f"Arquivo extraído: {file_to_extract}")
    except Exception as e:
        print(f"Erro ao extrair o arquivo CSV: {e}")
