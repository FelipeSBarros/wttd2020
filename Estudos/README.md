## Check list de boas práticas e deploy Heroku

1. [Separar Elementos da instacia X projetos](#Separar-Elementos-da-instacia-X-projetos)  
    * `SECRET_KEY` deve ir ao arquivo `.env`
    * `DEBUG`  
    * `DATABASESE`  
    * `ALLOWED_HOSTS`  
    
1. [Separar staticfiles]()  
    * dj-static
    * adicionar `STATIC_ROOT`  
    * configurar [wsgi.py]()
1. Registrar dependencias do projeto
    * Criar [requirementes.txt]()
1. Criar [arquivo de inicialização heroku]()
1. Criar repositório GIT  
    * Criar repositório (`git init`)  
    * Criar `.gitignore`  
        * .env
        * .idea
        * .wttd
        * *.sqlite3
        * *pyc
        * \_\_pycache__  
    * Adicionar arquivos para versionamento e commit
    *
1. [Criar conta](https://www.heroku.com/)  
1. [Heroku toolbelt](#Heroku-toolbelt)  
1. [Criar heroku app](#Heroku-app)  
1. [Configurar variáveis de ambiente Heroku]()  
1. [Fazendo o push do projeto ao Heroku]()  

## Separar Elementos da instacia X projetos  
Python-decouple permite ter um código único para várias instancias ao permitir a separação do codigo-fonte dos elemntos de configuração das diferentes instancias.  

### Instalando Python-decouple  

```
pip install python-decouple
pip install dj-database-url
pip install dj-static
```

### Incorporando às confirgurações  

**settings.py**
```
from decouple import config
from dj_database_url import parse as dburl

...

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

default_uburl_ = 'sqlite:///' + os.path.join(BASE_DIR, 'd.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}

ALLOWED_HOSTS = [*]

STATIC_ROOT = os.path.join(BASE_DIS, 'staticfiles')
```

**.env**  
Não manter os espaços!
```
SECRET_KEY=!a3rçkds...sdsd?
DEBUG=True
```  

**wsgi.py**:  

```
from dj-static import Cling

...

application = Cling(get_wsgi_application())
```

**Resumo do processamento**:    
Sempre que o projeto for inicializado e a função config for usada pasando a chave `SECRET_KEY`, o decouple busca uma variável do ambiente com esse nome. ao não encontrar, irá carregá-la do arquivo `.env`;  
No caso do `DEBUG`, é o mesmo. So adicionamos um valor padrão para o caso de não haver essa variavel de ambiente e o cast para que a strin vazia seja identificada como booleana;  
Sobre base de dados, vamos fazer com que o Django busque a variável de ambiente `DATABASE_URL` que, caso não exista, será buscada no `.env`. E caso não seja encontrado no `.env`, será usado o `default_dburl` (que possui a url para o db de desenvolvimento) que será passada ao `dburl` do modulo dj-database_url. 
`ALLOWED_HOSTS` atenderá a todos os chamados ([*]).  
`Cling` é uma app wsgi já do padrão python, assim como o `get_wsgi_aaplication()`. Ao envonver-los, o servidor web passará pelo `Cling` que depois o passará ao `get_wsgi_apppllication()` servindo, dessa forma os arquivos estáticos antes de chegar a requisição do Django.  

## Registrando dependencias d projeto:  

```
pip freeze > requirements.txt
```  
Depois, adicionar alguns módilos de forma manual:
```
gunicord==19.8.1
psycopg2-binary==2.8.6
```  

## Criar [arquivo de inicialização heroku]  

Criar `Procfile` no diretorio de trabalho.

```
web: gunicorn nome_proj_django.wsgi --log-file -
# exemplo
# web: gunicorn eventex.wsgi --log-file -
```

## [Heroku toolbelt](https://devcenter.heroku.com/articles/heroku-cli)  
Instalando as ferramentas necessarias par ao deploy:
* Heroku;  
* git;  
* ssh;  

```
sudo snap install --classic heroku
```

## Heroku login  
Vinculando usuario do heroku com o software instalado  

```
heroku login
```

Confirmando configuração

```
heroku login -i
```
## Heroku app  
A app é criada e já é adicionado um remote git para deploy
```
heroku apps:create nome_app
# verificar
git remote -v
# teste 3
heroku open
```

# Configurar variáveis de ambiente Heroku


```
cat .env # para identificar o que precisa ser configurado

heroku config:set SECRET_KEY='!a3rçkds...sdsd?'
heroku config:set DEBUG=True
```

## Fazendo o push do projeto ao Heroku

```
git push heroku master -- force
```