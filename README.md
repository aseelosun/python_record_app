# Records app

Проект на Flask с подключением к PostgreSQL, запуском через Docker и маршрутизацией через Nginx с поддержкой HTTPS.
## API Endpoints

- **GET /addrecord**  
  Добавляет случайную запись в базу данных.  
  Возвращает: `record added`

- **GET /deleterecord**  
  Удаляет первую по номеру запись из базы данных.  
  Возвращает: `record deleted`

- **GET /testdb**  
  Проверяет соединение с базой данных.  
  Возвращает: `PostgreSQL connection successful` или ошибку подключения.
## 📦 Стек технологий

- Python 3.11
- Flask
- PostgreSQL
- Docker & Docker Compose
- Nginx (reverse proxy)
- HTTPS (через собственные сертификаты)

---

## 🚀 Быстрый старт

1. **Клонировать репозиторий**

```bash
git clone https://github.com/aseelosun/python_record_app.git
cd python_record_app
```

2. **Создать .env файл**
```bash
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
```

3. **Создать директорию для сертификатов**
Убедитесь, что в папке certs/ находятся ваши SSL-сертификаты:

- nginx.crt

- nginx.key

4. **Собрать и запустить контейнеры**
```bash
docker-compose build --no-cache
docker-compose up -d
```

5. **Проверка**
```
curl -k https://localhost/addrecord
curl -k https://localhost/deleterecord
```


