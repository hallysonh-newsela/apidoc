# Django

Start server with: `make django` or `cd django && python manage.py runserver 0.0.0.0:8000`

Open JSON: [http://localhost:8000/docs](http://localhost:8000/schema.json)
Swagger URL: [http://localhost:8000/docs](http://localhost:8000/docs)
Redoc: [http://localhost:8000/docs](http://localhost:8000/redoc)

## Create users

```sh
python manage.py createsuperuser --username=admin --email=admin@example.com
```

## Create initial data

```sh
python manage.py dumpdata auth.user -o fixtures/initial_data.json
```

## Create migration file

```sh
python manage.py makemigrations --empty users --name load_initial_data
```
