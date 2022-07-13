### version

- python: 3.8.10
- django: 4.0.6

### venv

- cd django-sample/
- python -m venv venv
- source venv/bin/activate

### pip install

- pip install django
- pip install djangorestframework
- pip install django-filter


### postgres起動

- docker-compose up -d

### migration

- python manage.py makemigrations --settings=config.env.development
- python manage.py migrate --settings=config.env.development

### 起動(localhost:8000)
- python manage.py runserver --settings=config.env.development

### create superuser
- python manage.py createsuperuser --settings=config.env.development

### api example

- curl -XPOST localhost:8000/api/users/ -H 'Content-Type: application/json' -d '{"name": "asd", "mail": "asd@asd.com"}'
- curl localhost:8000/api/entires/
  - jqを入れるとresponseのjsonが整形されて見やすい
  - ex) curl localhost:8000/api/entires/ | jq

### run batch

- python manage.py fetch_title 1 2 --settings=config.env.development
  - データがある場合、引数のIDのtitleをprintする

- python manage.py export_entries --settings=config.env.development
  - データをcsvに出力
