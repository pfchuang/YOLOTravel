# TripCollector 主程式
- - -

## 開發環境 ##
Ubuntu 16.04

Python 3.6.3

PostgreSQL 9.6.8

## 初始化套件 ##

    pip install -r requirements.txt

## 初始化設定 ##

建立資料表所需之 migrate 文件

    python manage.py makemigrations

透過 migrate 建立資料表

    python manage.py migrate

建立後台管理員

    python manage.py createsuperuser

## 啟用Server ##

    python manage.py runserver 0.0.0.0:8000
