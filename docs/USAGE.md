# Руководство по использованию

## Быстрый старт

### 1. Установка

```bash
# Клонируйте репозиторий
git clone <repository-url>
cd <repository-name>

# Установите зависимости
pip install -r requirements.txt
```

### 2. Базовое использование

Создайте текстовый файл с учебным материалом:

```bash
# Пример: lecture.txt
echo "Machine learning is a subset of artificial intelligence..." > lecture.txt
```

Запустите резюмирование:

```bash
python -m src.cli --input lecture.txt --compression 30
```

## Примеры использования

### Пример 1: Резюмирование английского текста

```bash
python -m src.cli \
  --input english_article.txt \
  --language en \
  --compression 20 \
  --output summary.txt
```

### Пример 2: Резюмирование русского текста с ключевыми моментами

```bash
python -m src.cli \
  --input russian_lecture.txt \
  --language ru \
  --compression 30 \
  --key-points \
  --output summary_with_points.txt
```

### Пример 3: Автоматическое определение языка

```bash
python -m src.cli \
  --input multilingual_text.txt \
  --language auto \
  --compression 50
```

### Пример 4: Использование в Python коде

```python
from src.summarizer import Summarizer
from src.file_processor import FileProcessor

# Загрузка текста из файла
processor = FileProcessor()
text = processor.read_file("article.txt")

# Создание резюме
summarizer = Summarizer(language='auto')
summary, detected_lang = summarizer.summarize(
    text, 
    compression_level=0.3
)

print(f"Язык: {detected_lang}")
print(f"Резюме:\n{summary}")

# Извлечение ключевых моментов
key_points = summarizer.extract_key_points(text, num_points=5)
print("\nКлючевые моменты:")
for i, point in enumerate(key_points, 1):
    print(f"{i}. {point}")
```

## Уровни сжатия

- **20%**: Максимальное сжатие, только самые важные моменты
- **30%**: Сбалансированное сжатие (рекомендуется)
- **50%**: Минимальное сжатие, больше деталей

## Поддерживаемые форматы

### Текстовые файлы (.txt)
```bash
python -m src.cli --input document.txt --compression 30
```

### DOCX файлы
Требуется установка: `pip install python-docx`

```bash
python -m src.cli --input lecture.docx --compression 30
```

### PDF файлы
Требуется установка: `pip install PyPDF2`

```bash
python -m src.cli --input article.pdf --compression 30
```

## Советы по использованию

1. **Для длинных документов**: Используйте уровень сжатия 20-30%
2. **Для коротких текстов**: Используйте уровень сжатия 50%
3. **Автоматическое определение языка**: Работает лучше для текстов длиннее 100 символов
4. **Ключевые моменты**: Полезны для быстрого обзора содержания

## Устранение неполадок

### Проблема: Модели не загружаются

**Решение**: Убедитесь, что у вас установлены все зависимости:
```bash
pip install transformers torch sentencepiece
```

### Проблема: Медленная работа

**Решение**: 
- Используйте GPU если доступен
- Для быстрого тестирования система автоматически переключится на простой метод

### Проблема: Ошибка при чтении файла

**Решение**: 
- Проверьте формат файла (поддерживаются .txt, .docx, .pdf)
- Убедитесь, что файл не поврежден
- Для DOCX и PDF установите соответствующие библиотеки

