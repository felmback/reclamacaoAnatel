from google.cloud import storage
import os

def upload_csv(bucket_name,local_folder_path,gcs_folder_path):
   client = storage.Client()
   try:
        bucket = client.bucket(bucket_name)
    
        # Itera sobre os arquivos na pasta local
        for filename in os.listdir(local_folder_path):
            # if( filename.endswith(".csv")):
            if filename =="Anatel_Consumidor_Reclamacoes.csv":  
                file_path = os.path.join(local_folder_path, filename)
                gcs_object_name = gcs_folder_path + filename
                blob = bucket.blob(gcs_object_name)
                blob.upload_from_filename(file_path)
                
                print(f'Arquivo {filename} inserido {bucket_name}/{gcs_folder_path}.')
   except Exception as error:
    print(error)

  