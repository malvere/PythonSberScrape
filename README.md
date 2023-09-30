# SberScrape

Парсинг товаров с СберМегаМаркета

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/yourproject/blob/main/LICENSE)

## Содержание

- [Введение](#Введение)
- [Фичи](#фичи)
- [Инструкции](#инструкция)
  - [Требования](#требования)
  - [Установка проекта](#установка-проекта)

## Введение

Скрипт собирает данные с СберМегаМаркета и выводит список товаров в консоль
Поможет купить что-то с ммаксимальной выгодой

## Фичи

Что может:

- Вывод артиклов товаров
- Получение размера скидок в виде бонусов Спасибо


## Инструкция

Provide instructions on how to get started with your project.

### Требования

- Python 3.10 или новее
- Браузер для Playwright

### Установка проекта

Следуйте этим инструкциям, чтобы установить и запустить проект локально.

1. Сначала убедитесь, что у вас установлен Python. Вы можете скачать его с [официального сайта Python](https://www.python.org/downloads/windows/).

2. Склонируйте репозиторий на свой компьютер с помощью команды Git:

   ```bash
   git clone https://github.com/malvere/SberScrape
   ```
3. Перейдите в каталог проекта:
    ```bash
    cd SberScrape
    ```
4. Установите зависимости проекта с помощью pip:
    ```bash
    pip install -r requirements.txt
    ```
5. Установить браузер для PlayWright:
    ```bash
    playwright install webkit
    ```
6. Запустите скрипт:
    ```bash
    python main.py
    ```

## Смена каталога

Смена каталога происходит путём замены ссылки в файле main.py
```python
url = 'https://megamarket.ru/catalog/smartfony-android/'
```




