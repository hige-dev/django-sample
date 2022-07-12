### version

- python: 3.8.10
- django: 4.0.6

### pip install
- pip install django
- pip install djangorestframework
- pip install django-filter


### postgres起動

- docker-compose up -d

### migration

- python manage.py makemigrations
- python manage.py migrate

### 起動(localhost:8000)
- python manage.py runserver

### create superuser
- python manage.py createsuperuser

### run batch

- python manage.py fetch_title 1 2 --settings=config.env.development
  - データがある場合、引数のIDのtitleをprintする

- python manage.py export_entries --settings=config.env.development
  - データをcsvに出力
