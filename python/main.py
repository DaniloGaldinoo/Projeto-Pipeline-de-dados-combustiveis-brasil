import subprocess

print('Iniciando Download...')
subprocess.run(['python', 'extractor/download_data.py'])
print('Transformando dados...')
subprocess.run(['python', 'transform/transformar_csv.py'])
print('Enviando dados ao MySQL...')
print('Enviado com Sucesso!')