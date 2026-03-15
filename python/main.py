#Roda toda a pipeline de uma vez.

import subprocess

print('Iniciando pipeline...')
subprocess.run(['python', 'extractor/download_data.py'])
print('Executando download...')
subprocess.run(['python', 'transform/transformar_csv.py'])
print('Executando transformação e carga...')
print('Pipeline finalizado com Sucesso!')