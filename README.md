# Пытаемся понять как FastApi работает.


# Ставим зависимости

```
pip install -r ./api/requirements.txt
```

# Ставим базу
```
docker run --name fa_v2 -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

# Запуск
```
uvicorn api.main:app --reload
```

# Алембик миграции

```
alembic revision --autogenerate -m "create tables"
alembic upgrade head
```

# .env файлик
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
```
