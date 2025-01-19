# Personal Site

This is the public repo for my personal site, created using the [Django Web Framework](https://www.djangoproject.com/).


## Helpful Commands

### Delete Pycache 

```sh
$ python manage.py delete_migrations
```

### Delete Migrations

```sh
$ python manage.py delete_migrations
```

### Livereload (using [django-livereload-server](https://github.com/tjwalch/django-livereload-server))

Start the livereload server:

```sh
$ python manage.py livereload
```

```sh
$ python manage.py runserver
```

In the browser's address bar access your web app by doing:

```sh
127.0.0.1:8000 or localhost:8000
```

### Tailwind Build Process

```sh
$ npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```