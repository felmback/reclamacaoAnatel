
import aiohttp
import asyncio
import nest_asyncio
import os 

nest_asyncio.apply()

async def download_file(url, save_path, timeout=5000, max_retries=2):
    print('Baixando')
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=timeout) as response:
                if response.status == 200:
                    with open(save_path, "wb") as file:
                        while True:
                            chunk = await response.content.read(9000)
                            await asyncio.sleep(0)
                            if not chunk:
                                break
                            file.write(chunk)
                else:
                    print(f"Erro ao baixar o arquivo: Status {response.status}")
                    # gera um excessão para o retorno != 200
                    response.raise_for_status()  
    except asyncio.TimeoutError as e:
        print(f"Erro de timeout ({timeout} seconds)")
        raise e
    except aiohttp.ClientError as e:
        print(f"Erro na requisicao http: {e}")
        raise e


async def main():
    # url = "https://www.anatel.gov.br/dadosabertos/paineis_de_dados/consumidor/consumidor_reclamacoes.zip" 
    # # salva arquivo na raiz do script
    # script_folder = os.path.dirname(os.path.abspath(__file__))
    # save_path = os.path.join(script_folder, "consumidor_reclamacoes.zip")
    
    try:
        await download_file(url, save_path)
        print("Download completo.")
    except Exception as e:
        print(f"An error occurred: {e}")

# # if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
