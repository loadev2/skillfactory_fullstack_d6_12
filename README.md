Приложение на heroku - https://mighty-retreat-51870.herokuapp.com/
<br>
Локальный запуск. <br>
1) Создать папку на локальном компьютере и выполнить <br>
2) В settings.py перенастроить данные для своей базы postgresql или раскоментить <br>
DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.sqlite3',<br>
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),<br>
    }<br>
}<br>
для использования sqlite3(вход в админку - admin - 123456) (также нужно закоментить настройки базы postgresql)<br>
3) Запустить локальный сервер. <br>
