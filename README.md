# Пульт охраны банка

Приложение  которое показывает общее количество выданных пропусков и сколько из них сейчас активировано.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

### Как установить
#### 1) Клонируем проект
`git clone https://github.com/bast1989/django-orm-watching-storage-part-1`

#### 2) Создаём и активируем виртуальное окружение
`python -m venv .venv`

Чтобы использовать это окружение, его нужно "активировать":
* На Windows: `.venv\Scripts\activate`
* На macOS/Linux: `source .venv/bin/activate`

#### 3) Ставим зависимости
`pip install -r requirements.txt`

#### 4) Создаём .env по образцу:
В файле .env используются следующие переменные:
```
DATABASE_URL=postgresql://user:pass@host:1433/name
CRYPTO_KEY = секретный ключ
```
#### 5) Запускаем крипт
python main.py

Результатом работы скрипта будет вывод в консоль общего количества пропуском и количества пропусков которые сей час активированы.

<img width="2107" height="247" alt="image" src="https://github.com/user-attachments/assets/a8772ce3-e55f-4ef0-bbcc-b392c0a2128f" />
