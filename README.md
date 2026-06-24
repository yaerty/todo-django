To-Do List на Django

Простое веб-приложение для управления задачами.

Функционал
-  Добавление задач
-  Отметка задач как выполненных
-  Удаление задач
-  Просмотр списка всех задач

Запуск проекта

1. Клонируйте репозиторий:

git clone https://github.com/irinashmeleva/todo-django.git

cd todo-django

2. Создайте и активируйте виртуальное окружение:

python -m venv venv

venv\Scripts\activate  # Windows

source venv/bin/activate  # Mac/Linux

3. Установите зависимости:

pip install django

4. Примените миграции:

python manage.py migrate

5. Запустите сервер:

python manage.py runserver

6. Откройте http://127.0.0.1:8000