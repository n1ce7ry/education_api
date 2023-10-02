# Not implemented:
 * Unit test for stats app
 * Second api
 * I haven't found an optimal way how to output status information and viewing time for the first api

## Working api endpoints:
 * api/lessons/
 * api/stats/ (Partially)

## ERD
![alt text](docs/images/education_erd.png)

## Quick start

Install poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Clone the project
```bash
git clone https://github.com/n1ce7ry/education_api
```

Install the dependencies
```bash
poetry shell
poetry install
```

Edit env.example, rename it to env.sh, and run it:
```bash
vim env.example
mv env.example env.sh
. ./env.sh
```

Apply migrations
```bash
./manage.py migrate
```

Run server 
```bash
./manage.py runserver
```



