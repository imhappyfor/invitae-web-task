Invitae Coding Task
==========
This task is meant to help us get a feeling for your coding style,
to assess your ability to write maintainable Python and JavaScript,
to gauge your familiarity with Django, and to give you a little
glimpse of the sort of problem domain that we deal with at Invitae.
After performing the setup steps below, you'll be presented with the
instructions for your task. The requirements are intentionally
kept to a minimum, so as to allow you to show off your particular
strengths.

#### Prerequisites
- Python 3.7
- pip
- Mozilla Firefox web browser (for running tests)
- Mozilla geckodriver (for running tests; on Mac, `brew install geckodriver`)

#### Setup
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Visit the running application at http://127.0.0.1:8000/ to get started on your task!

#### Testing
```
python manage.py test
```

#### Third-Party Documentation
- https://docs.djangoproject.com/en/3.0/
- http://getbootstrap.com/docs/3.3/
- https://pypi.python.org/pypi/selenium
