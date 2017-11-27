# django-app-quickstarter
django app quickstarter

# DO NOT FORGET TO CHANGE!
The default app name is `barebone`, so it must be changed before using this app template.

Don't forget to modify the file and directory for your Django application.

1. Please, change the app directory name: `barebone`.

    [barebone](barebone)

2. Please, change the inherited class of `AppConfig`.

    [barebone/apps.py - BareboneConfig](barebone/apps.py#L5)
    
    [barebone/apps.py - barebone](barebone/apps.py#L6)

3. Please, change the package name in [setup.py](setup.py)

    [setup.py - django-app-quickstarter](setup.py#L9)
    
4. Please, change the package name in [settings.py](sandbox/sandbox/settings.py)

    [sandbox/sandbox/settings.py - barebone](sandbox/sandbox/settings.py#L28)
    
5. Please, change the version and package name in [barebone/__init__.py](barebone/__init__.py)

    [barebone/__init__.py](barebone/__init__.py)

# Coverage, Tox supported

# Package build and installation
## Build
```
python setup.py sdist
```

## Install
```
python setup.py install -f
```

# Sandbox Test
```
cd sandbox
python manage.py runserver
```