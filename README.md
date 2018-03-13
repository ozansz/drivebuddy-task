# drivebuddy-task

Driver model implementation using Django REST Framework

## Installation

Before cloning the repository, you need `django` and `djangorestframework` packages installed.

To install them, run the command below:

```bash
pip install django djangorestframework
```

Then, you can clone the repo:

```bash
git clone https://github.com/ozansz/drivebuddy-task
cd ./drivebuddy-task
```

And to run the server, run the command below:

```bash
python manage.py makemigrations drivers
python manage.py migrate
python manage.py runserver
```

## Tests

There are 6 tests implemented to test the CRUD functionality of the API.

You can run the tests running the command below:

```bash
python manage.py test
```
