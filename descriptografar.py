import os
import pyaes


## Abrir o arquivo Criptografado
file_name = 'teste_entrega.txt.ransomwarehacker'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remover o arquivo Criptografado
os.remove(file_name)

## Setar a Chave de Encriptação
key = b'ransomwaretestes'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Criar um novo arquivo Descriptografado
new_file = 'teste_entrega.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()

