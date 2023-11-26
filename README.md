# indigolab_test

## Инструкция по запуску

Чтобы запустить проект локально выполните следующие шаги

### Переменные окружения

Создайте копию файла example.env и переименуйте его в .env, затем измените параметры переменных окружения по необходимости

### Запуск docker-compose
Compose для разработки
```
docker-compose -f docker-compose.dev.yml up --build
```
Compose для продовой среды
```
docker-compose -f docker-compose.prod.yml up --build
```
### Создание тестового пользователя и получение токена

Заходим в контейнер

```
docker exec -it capibara_app sh
```

Создаем пользователя

```
python manage.py createsuperuser
```

Выдаем токен пользователю

```
python manage.py drf_create_token <user_name>
```

### Тестирование приложения

Для тестирования приложения воспользуйтесь postman коллекцией: Capibara.postman_collection.json