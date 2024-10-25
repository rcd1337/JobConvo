## tecnologias utilizadas:
- **Python** 3.12 e **Django** 5.0.9
- **Django REST framework** - api
- **PorstgreSQL** - database
- **Docker** - containers
- **JWT** - autenticação
- **Swagger** - documentação endpoints
- **IPython** - console iterativo
- **Node.js** e **npm** - frontend
- **Recharts** - gerar o gráfico

## pré-requisitos:
- docker (27.2.0)
- node.js v18.19.1 e npm 9.2.0


## inicialização:
### back-end:
Clonar este repositório.
```
git clone https://github.com/rcd1337/JobConvo.git
cd JobConvo
```
Certifíque-se que está na pasta raiz do projeto `JobConvo`.

Para subir o container e inicializar o servidor do projeto: 
```
docker compose up
```
Para popular database com dados iniciais:
```
docker compose exec django python manage.py loaddata config/fixtures/fixtures.json
```
### front-end:
Certifíque-see que está na pasta front-end (`cd front-end`)

rode `npm install --force`

rode `npm run dev`

acesse a aplicação através da url:
```
http://localhost:3000/
```

Obs: O front da aplicação não ficou 100%, alguns problemas:
- `sign in` e `sign up` não tem avisos de sucesso.
- caso errar as credenciais do sign in, necessário dar hard refresh na página (ctrl+f5).
- caso der f5, necessário logar novamente


## mais informações
- conta superuser p/ poder utilizar o painel do django admin `http://localhost:8000/admin/`:

email: `admin`

senha: `admin`

- listar todos os usuarios cadastrados inicialmente (endpoint p/ auxiliar testes): `http://localhost:8000/api/v1/users/`

senha de todos é: `teste`

- swagger p/ visualizar os endpoints da api: `http://localhost:8000/swagger/`
- postman collection se encontra em `config/doc/JobConvo.postman_collection.json`
