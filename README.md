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
HOST=<enter host>
NAME=<enter name>
BANK_USER=<enter username>
PASSWORD=<enter password>
SECRET_KEY=<enter secret key>
DEBUG=<enter true/false>
```
* Запустите код командой:
```bash
$ python3 manage.py runserver 0.0.0.0:8000
```