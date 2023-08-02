# Caleb's Blog


## Installation

Download or Clone this repo.
Загрузите или клонируйте этот репозиторий

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Caleb's blog.

```cd``` into BLOG

create a virtual environment.

```virtualenv venv```

or use [pipenv](https://pipenv.pypa.io/en/latest/) - recommend.

for [pipenv](https://pipenv.pypa.io/en/latest/) use: 

```bash 
pipenv install
```
this should create a virtual environment and install all the dependency

activate it by running ```pipenv shell```

run migration
```bash 
python manage.py migrate
```
create a superuser: ```python manage.py createsuperuser```

## Usage
 
start the dev server: ```python manage.py runserver```

Create an account, login and create a post.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
