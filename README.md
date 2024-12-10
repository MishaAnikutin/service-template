# service-template

Шаблон микросервиса

## Инициализация

Сделайте файл `install.sh` исполняемым:

```shell
chmod +x ./install.sh
./install.sh
```

## Контейнеризация

```shell
docker build . -t service_tag
docker run -p 8000:8000 -t setvice_tag
```

Теперь по `localhost:8000/docs` будет Swagger


## Оценка кода

Следующая команда отформатирует код по PEP-8, запустит проверку линтера и статического анализатора типов 
```shell
make all
```

## Менеджмент сервиса через CLI

Для документации:

```shell
python manage.py --help
```
Основные скрипты:

```shell
python manage.py new-controller *название контроллера* # Создаст новый контроллер
python manage.py new-schema *название схемы*
python manage.py new-service *название сервиса*
python manage.py new-gateway *название гейтвея*
```
