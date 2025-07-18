# instalando o pipx
pip install --user pipx

# Adiciona o diretório dos ambientes virtuais do pipx ao PATH do sistema.Reiniciar o shell após executá-lo.
pip install --user pipx

# instalando o Poetry (Cria um ambiente virtual isolado para poetry e o deixa disponível no sistema)
pipx install poetry 

# O comando inject instala um pacote em um ambiente virtual "global" já criado. Neste caso, estamos injetando o comando poetry shell, que nos permite entrar nos ambientes virtuais.
pipx inject poetry poetry-plugin-shell 


# Instala uma versão específica do python
poetry python install 3.13  

# Cria um pacote python chamado fast_zero no formato flat. Por padrão, o poetry utiliza o formato src. Mais informações sobre isso aqui
poetry new --flat fast_zero 
cd fast_zero

# Informa ao Poetry qual versão será utilizada no projeto
poetry env use 3.13

# No 'pyproject.toml', informar qual versões são permitidas 
    [project]
    # ...
    requires-python = ">=3.13,<4.0" 
    > A expressão ">=3.13,<4.0" significa que qualquer versão maior ou igual a 3.13 e menor que 4.0 será válida para o projeto.

# Instalando bibliotecas com o Poetry
poetry install 

# Adiciona o FastAPI no nosso projeto e ambiente virtual
poetry add 'fastapi[standard]' 

# Aciona ambient4 virtual
poetry shell

# Rodando o comando para subir o servidor dentro do shell do poetry
fastapi dev .\fast_api_0\app.py   

# rodando o comando se não estiver dentro do shell do poetry
poetry run fastapi dev .\fast_api_0\app.py 

# rodando o comando para subir o servidor com o uvicorn
uvicorn fast_zero.app:app

# Ferramentas para desenvolvimento:

* taskipy: ferramenta usada para criação de comandos. Como executar a aplicação, rodar os testes, etc.
* pytest: ferramenta para escrever e executar testes
* ruff: Uma ferramenta que tem duas funções no nosso código:
  - Um analisador estático de código (um linter), para dizer se não estamos infringindo alguma boa prática de programação;
  - Um formatador de código. Para seguirmos um estilo único de código. Vamos nos basear na PEP-8.

poetry add --group dev pytest pytest-cov taskipy ruff

# Trabalhando com sqlalchemy
poetry add sqlalchemy

# variáveis de ambiente
poetry add pydantic-settings

# migrações do banco de dados
poetry add alembic
alembic init migrations
alembic revision --autogenerate -m "create users table"
alembic upgrade head
alembic downgrade -1 // voltar uma migração 
alembic revision --autogenerate -m "exercicio 02 aula 04"


# ver BD de forma gráfica
pipx run harlequin .\database.db