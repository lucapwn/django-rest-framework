# Django REST Framework
Projeto utilizando o [*Django REST Framework*](https://www.django-rest-framework.org/) como trabalho da disciplina de Tópicos Especiais em Desenvolvimento Web.

Através da API, você poderá acessar todos os métodos HTTP para a realização de um CRUD em uma aplicação.

## Executando
>Instale as dependências do projeto
~~~shell
$ pip install -r requirements.txt
~~~
>Aplique as alterações das tabelas no SQLite
~~~shell
$ python manage.py migrate
~~~
>Crie um usuário administrador
~~~shell
$ python manage.py createsuperuser
~~~
>Execute a aplicação
~~~shell
$ python manage.py runserver
~~~
Agora você pode acessar a API do *Django REST Framework* em [```http://127.0.0.1:8000/```](http://127.0.0.1:8000/).

## Autenticação JWT

A aplicação utiliza o [JWT](https://jwt.io/) como autenticação, ou seja, será necessário obter o *token* através de uma requisição ```POST``` para a rota [```http://127.0.0.1:8000/token/```](http://127.0.0.1:8000/token/) e enviá-lo no cabeçalho da requisição. Exemplo:

~~~python3

import json
import requests

class Token:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_token(self):
        payload = {
            'username': self.username,
            'password': self.password
        }

        response = requests.post("http://127.0.0.1:8000/token/", data=payload)

        return response.text

    def get_users(self):
        token = json.loads(self.get_token())['access']

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

        response = requests.get("http://127.0.0.1:8000/users/?format=json", headers=headers)

        return response.text

def main():
    # Consider the user "admin" and password "admin" in the Django admin panel.
    # http://127.0.0.1:8000/admin/

    api = Token(username='admin', password='admin')

    print(api.get_token())
    print(api.get_users())

if __name__ == "__main__":
    main()

~~~

Em breve, será adicionado outros métodos para a realização do CRUD.

## Rotas
Através da rota [```http://127.0.0.1:8000/users/```](http://127.0.0.1:8000/users/), você poderá acessar os seguintes métodos HTTP:

* GET
* POST
* HEAD
* OPTIONS

E por fim, através da rota [```http://127.0.0.1:8000/users/<id>```](http://127.0.0.1:8000/users/<id>), você poderá acessar os seguintes métodos HTTP:

* PUT
* DELETE

Onde ```<id>``` é o ID do usuário cadastrado no banco de dados. Exemplo:

[```http://127.0.0.1:8000/books/1/```](http://127.0.0.1:8000/books/1/)
