# Educational Material Summarization Tool

Инструмент для автоматического резюмирования учебных материалов с поддержкой нескольких языков (English, Russian, German).

## Описание

Этот инструмент позволяет автоматически создавать краткие резюме учебных материалов (статьи, лекции) с возможностью выбора уровня сжатия и языка. Поддерживается абстрактивное резюмирование с использованием моделей transformers.

## Основной функционал

- ✅ Загрузка учебного материала (статьи, лекции в текстовом формате)
- ✅ Выбор языка текста (English, Russian, German, или автоматическое определение)
- ✅ Выбор уровня сжатия (20%, 30%, 50%)
- ✅ Абстрактивное резюмирование (использование transformers или простые методы)
- ✅ Вывод сжатого текста с ключевыми моментами
- ✅ Поддержка различных форматов файлов (txt, docx, pdf)

## Установка

### Требования

- Python 3.8 или выше
- pip

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Дополнительные зависимости для моделей

Для работы с моделями transformers может потребоваться дополнительная настройка:

```bash
# Для работы с русскими моделями
pip install transformers[torch]

# Для работы с PDF (опционально)
pip install PyPDF2

# Для работы с DOCX (опционально)
pip install python-docx
```

## Использование

### Командная строка

```bash
# Базовое использование
python -m src.cli --input document.txt --compression 30

# С указанием языка
python -m src.cli --input lecture.txt --language en --compression 20

# С сохранением в файл и извлечением ключевых моментов
python -m src.cli --input article.txt --output summary.txt --compression 50 --key-points

# Автоматическое определение языка
python -m src.cli --input text.txt --language auto --compression 30
```

### Параметры

- `--input, -i`: Путь к входному файлу (обязательно)
- `--output, -o`: Путь к выходному файлу (опционально, по умолчанию вывод в консоль)
- `--language, -l`: Язык текста (`en`, `ru`, `de`, или `auto` для автоматического определения)
- `--compression, -c`: Уровень сжатия (`20`, `30`, или `50` процентов)
- `--key-points, -k`: Также извлечь и отобразить ключевые моменты

### Программный интерфейс

```python
from src.summarizer import Summarizer
from src.file_processor import FileProcessor

# Чтение файла
processor = FileProcessor()
text = processor.read_file("document.txt")

# Создание резюме
summarizer = Summarizer(language='auto')
summary, detected_lang = summarizer.summarize(text, compression_level=0.3)

print(f"Detected language: {detected_lang}")
print(f"Summary: {summary}")

# Извлечение ключевых моментов
key_points = summarizer.extract_key_points(text, num_points=5)
for i, point in enumerate(key_points, 1):
    print(f"{i}. {point}")
```

## Структура проекта

```
.
├── src/                    # Исходный код
│   ├── __init__.py
│   ├── summarizer.py      # Основной модуль резюмирования
│   ├── file_processor.py  # Обработка файлов
│   ├── cli.py             # Командный интерфейс
│   └── main.py            # Точка входа
├── tests/                  # Тесты
│   ├── __init__.py
│   ├── test_summarizer.py
│   ├── test_file_processor.py
│   └── test_integration.py
├── data/                   # Данные (примеры, тестовые файлы)
├── docs/                   # Документация
├── .github/
│   └── workflows/
│       └── ci.yml         # CI/CD конфигурация
├── .gitignore
├── requirements.txt
└── README.md
```

## Тестирование

Запуск всех тестов:

```bash
pytest tests/ -v
```

Запуск с покрытием кода:

```bash
pytest tests/ -v --cov=src --cov-report=html
```

Запуск тестов для конкретного языка:

```bash
pytest tests/test_summarizer.py::TestSummarizer::test_summarize_english -v
```

## CI/CD

Проект включает автоматизированное тестирование через GitHub Actions:

- Тестирование на нескольких версиях Python (3.8, 3.9, 3.10, 3.11)
- Автоматическое тестирование с разными языками
- Проверка качества кода (flake8, black, mypy)

## Поддерживаемые языки

- **English (en)**: Использует модель `facebook/bart-large-cnn`
- **Russian (ru)**: Использует модель `IlyaGusev/rut5_base_sum_gazeta`
- **German (de)**: Использует модель `facebook/mbart-large-50-many-to-many-mmt`

## Форматы файлов

- `.txt` - Текстовые файлы
- `.docx` - Документы Microsoft Word (требует python-docx)
- `.pdf` - PDF документы (требует PyPDF2)

## Ограничения

- Модели transformers требуют значительного объема памяти и могут работать медленно на CPU
- При отсутствии доступа к моделям используется простой метод извлечения предложений
- Некоторые модели могут требовать дополнительной настройки для первого запуска

## Лицензия

Этот проект создан в образовательных целях.

## Авторы

Проект разработан для автоматизации резюмирования учебных материалов.

