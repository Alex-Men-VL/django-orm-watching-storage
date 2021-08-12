# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Сияние".
Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, 
т.к. у вас нет доступа к БД, но можете свободно использовать код верстки или
посмотреть, как реализованы запросы к БД.

Пуль охраны - это сайт, который можно подключить к удаленной базе данных с визитами и
карточками пропуска сотрудников нашего банка.

## Как устаноить

* Скачайте код;
* Установите Python пакеты из `requirements.txt`:
```bash
$ pip install -r requirements.txt
```
* Введите свои данные в файл `.env`:
```bash
DB_ENGINE=<enter engine>
DB_HOST=<enter host>
DB_PORT=<enter port>
DB_NAME=<enter name>
DB_BANK_USER=<enter username>
DB_PASSWORD=<enter password>
DB_SECRET_KEY=<enter secret key>
DB_DEBUG=<enter true/false>
```
* Запустите код командой:
```bash
$ python3 manage.py runserver 0.0.0.0:8000
```
