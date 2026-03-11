# Este script faz a ingestão inicial dos dados de preços de
# combustíveis disponibilizados pela ANP (Agência Nacional
# do Petróleo) através do portal de dados abertos.
#
# Etapas executadas pelo script:
# 1. Define os caminhos das pastas do projeto utilizando pathlib
# 2. Verifica se o arquivo .zip já existe na pasta /data/zip
# 3. Caso não exista, realiza o download do arquivo a partir da URL da ANP
# 4. Salva o arquivo .zip no diretório do projeto
# 5. Abre o arquivo .zip utilizando a biblioteca zipfile
# 6. Extrai o arquivo CSV para a pasta /data/raw

import requests
from pathlib import Path
import zipfile

rota_zip = Path(__file__).parent.parent.parent
arq_zip = rota_zip / "data" / "zip"
arquivo_zip = arq_zip / "ca-2025-02.zip"
arq_raw = rota_zip / "data" / "raw"
url_zip = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-2025-02.zip'


arq_zip.mkdir(exist_ok=True)
arq_raw.mkdir(exist_ok=True)

if arquivo_zip.exists():
    print('Arquivo já existente!')

else:
    print('Baixando novo arquivo . . .')
    response = requests.get(url_zip)
    if response.status_code == 200:
        print ('Requisição bem sucedida. Iniciando o Download!')
        with open(arquivo_zip, "wb") as f:
            f.write(response.content)
        print('Download Concluido!')
        with zipfile.ZipFile(arquivo_zip, "r") as zip_ref:
            zip_ref.extractall(arq_raw)

    elif response.status_code == 404:
        print('Arquivo não encontrado. De uma olhada se a url esta correta!')
    else:
        print('Erro de servidor! Tente novamente.')







