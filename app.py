import os
import platform

usuario = os.environ.get('USERNAME')

print(f'Sistema Operacional: {platform.system()} {platform.release()}.')
print(f'Nome do Usuário: {usuario}.')
# ou sem declarar a variavel
print(f'Nome de usuário: {os.environ.get('USERNAME')}')