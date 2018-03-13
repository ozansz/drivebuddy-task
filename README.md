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

## API

The RESTful API implements CRUD functionality for the `Driver` model.

### The Driver Model

The `Driver` model has three fields:

<ul>
  <li><b>name</b>  - Name of the driver</li>
  <li><b>email</b> - Unique email of the driver</li>
  <li><b>score</b> - Score of the driver</li>
</ul>

### API Endpoints

The API endpoints for the `Driver` model are under the `/drivers` path.

#### Create driver

Request: `POST`

Path:    `/drivers/`


Request body:


&nbsp;&nbsp;&nbsp;&nbsp;`name`: <driver_name>,

&nbsp;&nbsp;&nbsp;&nbsp;`email`: <driver_email>,

&nbsp;&nbsp;&nbsp;&nbsp;`score`: <driver_score>


Response: `201 - Created`

#### Read driver

Request: `GET`

Path:    `/drivers/<pk>`

Response: `200 - Created`


Response body:

&nbsp;&nbsp;&nbsp;&nbsp;`url`: <unique_path_of_driver_record>,

&nbsp;&nbsp;&nbsp;&nbsp;`name`: <driver_name>,

&nbsp;&nbsp;&nbsp;&nbsp;`email`: <driver_email>,

&nbsp;&nbsp;&nbsp;&nbsp;`score`: <driver_score>


#### Update driver



#### Delete driver



## Tests

There are 6 tests implemented to test the CRUD functionality of the API.

You can run the tests running the command below:

```bash
python manage.py test
```
