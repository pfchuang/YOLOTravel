# TripCollector 主程式
- - -

## 開發環境 ##
Ubuntu 16.04

Python 3.5.2

PostgreSQL 9.5.12

## 建立虛擬環境 ##

移動至專案目錄下後

    virtualenv -p python3 venv

## 啟動虛擬環境 ##

    source venv/bin/activate

## 初始化套件 ##

    pip install -r requirements.txt

## 初始化設定 ##

依 settings.py 設定 postgresql 資料庫

    sudo -i -u postgres
    [sudo] password for <username>:
    postgres@<username>$ createdb tripDB
    postgres@<username>$ createuser -P trip
    Enter password for new role: trip
    Enter it again: trip
    postgres@<username>$ psql
    postgres=# grant all privileges on database "tripDB" to "trip";
    GRANT
    postgres=# \q
    postgres@<username>$ exit

建立資料表所需之 migrate 文件

    python manage.py makemigrations

透過 migrate 建立資料表

    python manage.py migrate

建立後台管理員

    python manage.py createsuperuser

## 啟用Server ##

    python manage.py runserver 0.0.0.0:8000
