
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

                    response.raise_for_status()  
    except asyncio.TimeoutError as e:
        print(f"Erro de timeout ({timeout} seconds)")
        raise e
    except aiohttp.ClientError as e:
        print(f"Erro na requisicao http: {e}")
        raise e

