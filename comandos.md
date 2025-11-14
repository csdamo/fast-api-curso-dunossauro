#___________ Instalação

# instalando o pipx
pip install --user pipx

# Adiciona o diretório dos ambientes virtuais do pipx ao PATH do sistema.Reiniciar o shell após executá-lo.
pipx ensurepath

# instalando o Poetry (Cria um ambiente virtual isolado para poetry e o deixa disponível no sistema)
pipx install poetry 

# O comando inject instala um pacote em um ambiente virtual "global" já criado. Neste caso, estamos injetando o comando poetry shell, que nos permite entrar nos ambientes virtuais. Essa extensão adiciona o comando poetry shell, que habilita o ambiente virtual no terminal.
pipx inject poetry poetry-plugin-shell 


# Instala uma versão específica do python
poetry python install 3.13  

# Cria um pacote python chamado fast_zero no formato flat. Por padrão, o poetry utiliza o formato src. (https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
poetry new --flat fast_zero 
cd fast_zero

# Informa ao Poetry qual versão será utilizada no projeto
poetry env use 3.13

# No 'pyproject.toml', informar qual versões são permitidas 
    [project]
    # ...
    requires-python = ">=3.13,<4.0" 
    > A expressão ">=3.13,<4.0" significa que qualquer versão maior ou igual a 3.13 e menor que 4.0 será válida para o projeto.

# Instalando bibliotecas com o Poetry. Cria o ambiente virtual com a versão que setamos no env use
poetry install 

# Adiciona o FastAPI no nosso projeto e ambiente virtual
poetry add 'fastapi[standard]' 


#___________ Rodando servidor

# Habilita ambient4 virtual
poetry shell

# Rodando o comando para subir o servidor dentro do shell do poetry
fastapi dev .\fast_api_0\app.py   

# rodando o comando se não estiver dentro do shell do poetry
poetry run fastapi dev .\fast_api_0\app.py 

# rodando o comando para subir o servidor com o uvicorn
uvicorn fast_zero.app:app


#___________ Ferramentas de desenvolvimento

# Ferramentas para desenvolvimento:

* taskipy: ferramenta usada para criação de comandos. Como executar a aplicação, rodar os testes, etc.
* pytest: ferramenta para escrever e executar testes
* ruff: Uma ferramenta que tem duas funções no nosso código:
  - Um analisador estático de código (um linter), para dizer se não estamos infringindo alguma boa prática de programação;
  - Um formatador de código. Para seguirmos um estilo único de código. Vamos nos basear na PEP-8.

poetry add --group dev pytest pytest-cov taskipy ruff

## Ruff

[tool.ruff]
line-length = 79  # define comprimento da linha (PEP-8)
extend-exclude = ['migrations']  # exclui arquivo do monitoramento do ruff

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

[tool.ruff.format]
preview = true
quote-style = 'single'


I (Isort): Checagem de ordenação de imports em ordem alfabética
F (Pyflakes): Procura por alguns erros em relação a boas práticas de código
E (Erros pycodestyle): Erros de estilo de código
W (Avisos pycodestyle): Avisos de coisas não recomendadas no estilo de código
PL (Pylint): Como o F, também procura por erros em relação a boas práticas de código


## Pytest

[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'


## Taskipy

[tool.taskipy.tasks]
lint = 'ruff check'
pre_format = 'ruff check --fix'
format = 'ruff format'
run = 'fastapi dev fast_api_0/app.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_api_0 -vv'
post_test = 'coverage html'




# gitignore
pipx run ignr -p python > .gitignore  



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



poetry add "psycopg[binary]"


poetry add --group dev testcontainers


 docker build -t "fastapi_zero"

 docker run -it --name fastzeroapp -p 8000:8000 fastapi_zero:latest


docker compose up --build
 docker compose up