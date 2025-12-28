# Быстрый старт - Как запустить и проверить проект

## Шаг 1: Активация виртуального окружения

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Или Command Prompt
venv\Scripts\activate.bat
```

## Шаг 2: Проверка установки

### Вариант A: Быстрый тест (без загрузки моделей)

```bash
python quick_test.py
```

Этот скрипт проверит:
- Определение языка
- Простое резюмирование
- Извлечение ключевых моментов
- Чтение файлов

### Вариант B: Полные тесты

```bash
# Все тесты
pytest tests/ -v

# Только быстрые тесты (без загрузки моделей transformers)
pytest tests/test_file_processor.py -v
pytest tests/test_summarizer.py::TestSummarizer::test_detect_language_english -v
```

## Шаг 3: Использование CLI

### Базовый пример

```bash
# Резюмирование примера файла
python -m src.cli --input data/example_english.txt --compression 30

# С сохранением в файл
python -m src.cli --input data/example_english.txt --output summary.txt --compression 30

# С ключевыми моментами
python -m src.cli --input data/example_english.txt --compression 30 --key-points

# С указанием языка
python -m src.cli --input data/example_english.txt --language en --compression 20
```

### Справка по командам

```bash
python -m src.cli --help
```

## Шаг 4: Использование в Python коде

```python
from src.summarizer import Summarizer
from src.file_processor import FileProcessor

# Чтение файла
processor = FileProcessor()
text = processor.read_file("data/example_english.txt")

# Создание резюме
summarizer = Summarizer(language='auto')
summary, detected_lang = summarizer.summarize(text, compression_level=0.3)

print(f"Язык: {detected_lang}")
print(f"Резюме:\n{summary}")

# Извлечение ключевых моментов
key_points = summarizer.extract_key_points(text, num_points=5)
for i, point in enumerate(key_points, 1):
    print(f"{i}. {point}")
```

## Проверка структуры проекта

```bash
# Показать структуру
tree /F /A

# Или на Linux/Mac
tree -a
```

## Что проверить:

✅ `.gitignore` - существует и содержит Python-специфичные правила  
✅ `requirements.txt` - все зависимости с версиями  
✅ Структура папок: `/src`, `/tests`, `/data`, `/docs`  
✅ Тесты проходят  
✅ CLI работает  
✅ Нет нежелательных файлов (__pycache__, .pyc и т.д.)  

## Примечания

- Первый запуск с моделями transformers может занять время (загрузка моделей)
- Если модели не загружаются, используется простой метод резюмирования
- Для работы с PDF/DOCX установите дополнительные зависимости:
  ```bash
  pip install python-docx PyPDF2
  ```

