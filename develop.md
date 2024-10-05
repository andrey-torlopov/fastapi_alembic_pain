# Ставим зависимости
```
pip install -r requirements.txt
```

# Ставим базу
```
docker run --name db_demo -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```
