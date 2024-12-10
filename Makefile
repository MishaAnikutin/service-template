.PHONY: all format typecheck lint clean

all: format typecheck lint 

format:
	@echo "Форматируем код ..."
	python -m black .
	@echo "Форматирование прошло успешно!"

typecheck:
	@echo "Проверка типов ..."
	python -m mypy .
	@echo "Проверка типов прошла успешно!"

lint:
	@echo "Запуск линтера ..."
	python -m flake8 .
	@echo "Линтинг прошел успешно!"
clean:
	@echo "Удаляем временные файлы..."
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

