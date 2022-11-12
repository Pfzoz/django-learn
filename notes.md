# DJANGO

## Intro

Getting started with a Django project: django-admin startproject 'name'

Running server: python3 manage.py runserver  
Creating apps: python3 manage.py startapp 'name'

### Apps

Are like different specific django structures of your web page, such as the home page, the members database, etc.  
Django will require you to specify that new apps are 'installed'.

### Views

Are python functions/actions that take http responses as arguments and also returns http responses, such as HTML documents.  
For an instance, returning HttpResponse with a string will write directly into the web page's html.

*urls.py* holds the paths for the urls, and in the apps it is possible to specify the view that will manipulate the HttpResponse of such urls.  
On the main urls.py created you can specify apps' urls by adding include("app_urls_path")

### Templates

Are HTML or alike structures that can be loaded by Django. The templates .html files are located in the templates folder in the specific app.

### Models

Are Django's way of manipulating relational databases, such as SQLite and Postgres.

They can be easily created with classes inheriting Django's *models.Model* class.

### Migrations

Migrations are Django's way of propagating changes made to the models (adding a field, deleting a model, etc.) into the database schema.

Migration-related commands:

> makemigrations: creates new migrations based on the changes made to the models  
> migrate: applies/unapplies migrations.  
> sqlmigrate: displays SQL statements for migration.

## Models & QuerySets


Are collections of data from a database.