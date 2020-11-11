## Check list de boas práticas e deploy Heroku

1. [Separar Elementos da instacia X projetos](#Separar-Elementos-da-instacia-X-projetos)  
    Variáveis de instancia a serem configuradas:  
    * `SECRET_KEY`  
    * `DEBUG`  
    * `DATABASESE`
        * Usar módulo `dj-database-url`  
    * `ALLOWED_HOSTS`  
1. [Separar staticfiles]()  
    * Usar módulo `dj-static`
    * adicionar `STATIC_ROOT` em settings.py  
    * configurar wsgi.py  
1. [Registrar dependencias do projeto](#Registrando-dependencias-do-projeto)
    * Criar requirementes.txt
1. [Criar arquivo de inicialização heroku](#arquivo-de-inicialização-heroku)
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
1. [Criar conta](https://www.heroku.com/)  
1. [Heroku toolbelt](#Heroku-toolbelt)  
1. [Criar heroku app](#Heroku-app)  
1. [Configurar variáveis de ambiente Heroku](#Configurar-variáveis-de-ambiente-Heroku)  
1. [Fazendo o push do projeto ao Heroku](#Fazendo-o-push-do-projeto-ao-Heroku)  
1. [Atualizando o django](#Atualizando-o-Django)  

## Separar Elementos da instacia X projetos  
Python-decouple permite ter um código único para várias instancias ao permitir a separação do codigo-fonte dos elementos de configuração das diferentes instancias (`.env`).  

**Resumo da etapa**:    
Sempre que o projeto for inicializado e a função config for usada pasando a chave `SECRET_KEY`, por exemplo, o decouple busca uma variável do ambiente com esse nome. ao não encontrar, irá carregá-la do arquivo `.env`;  

No caso do `DEBUG`, é o mesmo. Se adicionamos um valor padrão para o caso de não haver essa variavel de ambiente e o cast para que a string vazia seja identificada como booleana;  
> :warning: Deixar DEBUG como True é um enorme erro, por expoem vulnerabilidades do sistema ao indicar os erros encontrados. Contudo é interessante tê-lo como True na instancia de desenvolvimento para poder identificr as fontes de erros e corrigi-las. Por isso, deixaremos como valor padrão `DEBUG=False` e no `.env` `DEBUG=True`.  

:warning: Ao usar o `DEBUG=False` no localhost, será necessário rodar o `collectstatic`:
```
manage collectstatic
```

Em `ALLOWED_HOSTS` devemos incluir uma lista de endereços de requisição aos quais o sistema atenderá o request.
Ao colocá-lo como `[*]`, o sistema atenderá aos chamadaos dde todos e qualquer host. No django o padrão é uma lista vazia `[]`. essa definição de `ALLAWED_HOSTS` está relacionada ao `DEBUG` pelo fato de, ao termos este ultimo como `False`, o Django nos força a configurar o `ALLOWED_HOSTS` nos impedindo de manter a aplicação rodando. Vamos configurar indicando o IP do localhost e do herokuapp.com, no arquivo `.env`, usando o Csv do decouple para converter os dados.
> :bulb: A definição dos domínimos de requisição permitidos é uma configuração de instância.  

Sobre base de dados, vamos fazer com que o Django busque a variável de ambiente `DATABASE_URL` que, caso não exista, será buscada no `.env`. E caso não seja encontrado no `.env`, será usado o `default_dburl` (que possui a url para o db de desenvolvimento) que será passada ao `dburl` do modulo dj-database_url.  

`Cling` é uma app wsgi já do padrão python, assim como o `get_wsgi_aaplication()`. Ao envonver-los, o servidor web passará pelo `Cling` que depois o passará ao `get_wsgi_apppllication()` servindo, dessa forma os arquivos estáticos antes de chegar a requisição do Django.  

### Instalando Python-decouple  

```
pip install python-decouple
pip install dj-database-url
pip install dj-static
```

### Incorporando às confirgurações  

**settings.py**
```
from decouple import config, Csv
from dj_database_url import parse as dburl

...

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

default_uburl_ = 'sqlite:///' + os.path.join(BASE_DIR, 'd.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}

...

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv()

...

STATIC_ROOT = os.path.join(BASE_DIS, 'staticfiles')
```

**.env**  

:warning: Garantir que não há espaços vazios;  

```
SECRET_KEY=!a3rçkds...sdsd?
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .localhost, .herokuapp.com
```  

**wsgi.py**:  

```
from dj-static import Cling

...

application = Cling(get_wsgi_application())
```  

## Registrando dependencias do projeto:  

```
pip freeze > requirements.txt
```  

Depois, adicionar alguns módulos manualmente no `requirements.txt`:

```
gunicorn==19.8.1
psycopg2-binary==2.8.6
```  

## Criar arquivo de inicialização heroku  

Criar `Procfile` no diretorio de trabalho.

```
web: gunicorn nome_proj_django.wsgi --log-file -
# exemplo
# web: gunicorn eventex.wsgi --log-file -
```

## [Heroku toolbelt](https://devcenter.heroku.com/articles/heroku-cli)  
Instalando as ferramentas necessarias para o deploy (instalação automática):
* Heroku;  
* git;  
* ssh;  

Comando:
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
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com
```

## Fazendo o push do projeto ao Heroku

```
git push heroku master -- force
```

## Atualizando o Django  

>não ter medo de atualizado o django.  

Ler as *release notes* para saber o que foi alterado e tentar antever alguns possíveis problemas.

Para atualizar:
```
pip install --upgrade django
```

:warning: não esquecer de atualizar o `requirements.txt`.  

O Django disponibiliza uma ferramenta para testar se tudo está funcionando como deveria:
```
manage check
```

Basta ir olhando o *trace back* para identificar o erro. Se necessário, buscar no google como solucioná-lo.
Ao final, teremos todas as **checagens padrão** do django funcionando. Mas pode ser que o projeto ainda apresente problemas.

```
manage runserver
```

Para identificar os problemas finais e buscar solucioná-los.

Por ultimo, rodar os testes do projeto... :warning: TATFT :warning:  
