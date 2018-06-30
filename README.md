## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone git@github.com:EtheriousNatsu/django-boards.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Setup the local configurations:

```bash
cp .env.example .env
```


Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

## License
The source code is released under the [MIT License](https://github.com/EtheriousNatsu/django-boards/tree/master/LICENSE).