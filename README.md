# Tehnostrelka

## Запуск
Перед запуском сервера необходимо подготовить виртуальную среду:
```sh
python -m venv venv

# Unix
source venv/bin/activate
# Windows
.\venv\Scripts\activate

pip install -r requirements.txt
```

И инициализировать векторную базу данных:
```sh
sudo docker run -p 6333:6333 -p 6334:6334 -v "$(pwd)/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```

Запуск сервера:
```sh
python manage.py runserver 
```


