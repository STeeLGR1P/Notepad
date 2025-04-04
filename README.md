# Notepad

Простой текстовый редактор, написанный на Python с использованием tkinter и принципов SOLID.

## Особенности

- Создание, открытие и сохранение текстовых файлов
- Операции с текстом (копировать, вырезать, вставить)
- Современный интерфейс
- Docker поддержка

## Требования

- Python 3.9+
- tkinter (входит в стандартную библиотеку Python)
- Docker (для запуска в контейнере)

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/notepad.git
cd notepad
```

2. Запустите приложение:
```bash
python notepad.py
```

### Запуск в Docker

1. Соберите Docker образ:
```bash
docker build -t notepad-app .
```

2. Для Windows:
   - Установите VcXsrv
   - Запустите XLaunch
   - Выберите "Multiple windows"
   - В настройках дисплея выберите "Start no client"
   - Отметьте "Disable access control"

3. Запустите контейнер:
```bash
docker run -it --rm -e DISPLAY=host.docker.internal:0.0 notepad-app
```

## Структура проекта

- `notepad.py` - основной файл приложения
- `interfaces.py` - интерфейсы (SOLID)
- `text_area.py` - работа с текстовой областью
- `file_operations.py` - операции с файлами
- `text_operations.py` - операции с текстом
- `Dockerfile` - сборка Docker образа

## Лицензия

MIT 