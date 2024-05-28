import os
import aiohttp
import asyncio
import nest_asyncio


from download import download_file
from extract_zip import extract_csv_from_zip
from etl import etl_reclamacoes
from upload_storage import upload_csv

nest_asyncio.apply()

#local
path_root = os.path.dirname(os.path.abspath(__file__))
zip_file  = os.path.join(path_root, "consumidor_reclamacoes.zip")
file_to_extract  = "reclamacoes_contexto.csv"
extracted_folder = os.path.join(path_root, "reclamacao")
nm_file = os.path.join(path_root, extracted_folder,file_to_extract)
save_file = os.path.join(extracted_folder,"Anatel_Consumidor_Reclamacoes.csv")

#gcp
bucket_name = 'fibrasil-manual'
gcs_folder_path='dados_abertos/'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ.get('key_dev')

url = "https://www.anatel.gov.br/dadosabertos/paineis_de_dados/consumidor/consumidor_reclamacoes.zip" 


async def main():

    try:
        await download_file(url, zip_file)
        print("Download completo.")
    except Exception as e:
        print(f"Erro ao baixar: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    extract_csv_from_zip(zip_file, file_to_extract, extracted_folder)
    dados = etl_reclamacoes(nm_file)
    dados.to_csv(save_file, index=False)
    upload_csv(bucket_name, extracted_folder, gcs_folder_path)

    print(dados.size)