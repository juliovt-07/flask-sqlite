# Flask-Sqlite

Uma API simples para gerenciar tarefas usando Flask e SQLite.

## Requisitos

- Python 3.10
- Flask
- SQLite

## Instalação

1. Clone este repositório:

git clone https://github.com/juliovt-07/flask-sqlite.git
cd flask-sqlite


2. Crie um ambiente virtual e ative-o:

- No Windows:

  ```
  python -m venv venv
  venv\Scripts\activate
  ```

- No Linux ou macOS:

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Instale as dependências:

pip install -r requirements.txt


## Configuração

1. Inicialize o banco de dados SQLite:

python init_db.py


## Execução

1. Inicie o servidor Flask:

python app.py


2. A API estará disponível em `http://127.0.0.1:5000/`.

## Endpoints

- `GET /tarefas`: Lista todas as tarefas.
- `POST /tarefas`: Adiciona uma nova tarefa.
- `PUT /tarefas/<task_id>`: Atualiza uma tarefa existente pelo ID.
- `DELETE /tarefas/<task_id>`: Remove uma tarefa pelo ID.

## Teste

Use uma ferramenta como [Insomnia](https://insomnia.rest/) ou [Postman](https://www.postman.com/) para testar a API.
