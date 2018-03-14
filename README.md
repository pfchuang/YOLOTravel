# TripCollector 主程式
- - -

## 初始化套件 ##

    pip install -r requirements.txt

## 初始化設定 ##

建立資料表所需之 migrate 文件

    ./manage.py makemigrations

透過 migrate 建立資料表

    ./manage.py migrate

建立後台管理員

    ./manage.py createsuperuser

## 啟用Server ##

    ./manage.py runserver 0.0.0.0:8000
