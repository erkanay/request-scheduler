# Request Scheduler

This project allows you to schedule requests at a given time.

# Installation

It would be easy to manage packages on `virtualenvwrapper`.
```
$ pip install virtualenvwrapper
...
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv --python=/usr/local/bin/python3 perdoo 
```
Then please install the requirements and apply migrations.

```
$ pip install -r requirements.txt
$ python manage.py migrate
```
You can also create to super user to schedule a request on `adminsite`.

```
$ python manage.py createsuperuser
```
Finally run following commands in 2 different tabs.
```
$ python manage.py runserver
$ python tasks.py
```

# Manage The Requests

After installation instructions above, 
please use either `http://0.0.0.0:8000/admin` or `http://0.0.0.0:8000/api/v1/scheduler/` to manage scheduled requests.
