#!/bin/bash


# Проверка на наличие Poetry
if ! command -v poetry &> /dev/null; then
    echo "Poetry не обнаружен. Устанавливаем Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    
    # Добавление Poetry в PATH, если это еще не сделано
    export PATH="$HOME/.local/bin:$PATH"
fi

# Инициализация нового проекта с помощью Poetry (если еще не выполнено)
poetry init --no-interaction

# Установка зависимостей в dev окружение
echo "Установка dev-зависимостей..."
poetry add --dev click mypy flake8 black
poetry add fastapi pydantic uvicorn dishka

echo "Установка завершена!"
