# API Documentation

## Summarizer Class

Основной класс для резюмирования текста.

### `Summarizer(language: str = 'auto')`

Инициализирует объект резюмирования.

**Параметры:**
- `language` (str): Целевой язык ('en', 'ru', 'de', или 'auto' для автоматического определения)

**Пример:**
```python
summarizer = Summarizer(language='en')
```

### `detect_language(text: str) -> str`

Определяет язык входного текста.

**Параметры:**
- `text` (str): Входной текст для анализа

**Возвращает:**
- `str`: Код языка ('en', 'ru', 'de')

**Пример:**
```python
language = summarizer.detect_language("This is an English text")
# Возвращает: 'en'
```

### `summarize(text: str, compression_level: float = 0.3, language: str = None) -> Tuple[str, str]`

Резюмирует входной текст.

**Параметры:**
- `text` (str): Входной текст для резюмирования
- `compression_level` (float): Уровень сжатия (0.2, 0.3, или 0.5)
- `language` (str): Код языка ('en', 'ru', 'de') или None для автоматического определения

**Возвращает:**
- `Tuple[str, str]`: Кортеж из (резюмированный_текст, обнаруженный_язык)

**Пример:**
```python
summary, lang = summarizer.summarize(text, compression_level=0.3, language='en')
```

### `extract_key_points(text: str, num_points: int = 5) -> List[str]`

Извлекает ключевые моменты из текста.

**Параметры:**
- `text` (str): Входной текст
- `num_points` (int): Количество ключевых моментов для извлечения

**Возвращает:**
- `List[str]`: Список ключевых предложений

**Пример:**
```python
key_points = summarizer.extract_key_points(text, num_points=5)
```

## FileProcessor Class

Класс для обработки файлов различных форматов.

### `read_file(file_path: str) -> str`

Автоматически определяет тип файла и читает его.

**Параметры:**
- `file_path` (str): Путь к файлу

**Возвращает:**
- `str`: Извлеченное текстовое содержимое

**Исключения:**
- `FileNotFoundError`: Если файл не найден
- `ValueError`: Если тип файла не поддерживается

**Пример:**
```python
processor = FileProcessor()
text = processor.read_file("document.txt")
```

### `read_text_file(file_path: str) -> str`

Читает обычный текстовый файл.

**Параметры:**
- `file_path` (str): Путь к текстовому файлу

**Возвращает:**
- `str`: Содержимое файла как строка

### `read_docx(file_path: str) -> str`

Читает файл DOCX.

**Параметры:**
- `file_path` (str): Путь к файлу DOCX

**Возвращает:**
- `str`: Извлеченное текстовое содержимое

**Исключения:**
- `ImportError`: Если python-docx не установлен

### `read_pdf(file_path: str) -> str`

Читает файл PDF.

**Параметры:**
- `file_path` (str): Путь к файлу PDF

**Возвращает:**
- `str`: Извлеченное текстовое содержимое

**Исключения:**
- `ImportError`: Если PyPDF2 не установлен

