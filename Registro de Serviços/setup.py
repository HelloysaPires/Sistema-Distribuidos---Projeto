from setuptools import setup, find_packages

setup(
    name='RegistroDeServicos',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Lista de dependências do projeto, mesmo que no requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'start=registro_de_servicos:iniciar_registro'
        ],
    },
)
