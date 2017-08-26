# django-app-quickstarter
django app quickstarter

# DO NOT FORGET TO CHANGE!
Don't forget to modify the file and directory for your Django application.

1. Please, change the app directory name: `barebone`.

    [barebone](barebone)

2. Please, change the inherited class of `AppConfig`.

    [barebone/apps.py - BareboneConfig](barebone/apps.py#L5)
    
    [barebone/apps.py - barebone](barebone/apps.py#L6)

3. Please, change the package name in [setup.py](setup.py)

    [setup.py - django-app-quickstarter](setup.py#L9)

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