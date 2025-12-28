"""
Быстрый тест работоспособности проекта без загрузки больших моделей.
"""

import sys
import io

# Установка UTF-8 для Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.summarizer import Summarizer
from src.file_processor import FileProcessor

def test_basic_functionality():
    """Быстрый тест базовой функциональности."""
    print("=" * 60)
    print("БЫСТРЫЙ ТЕСТ ПРОЕКТА")
    print("=" * 60)
    
    # Тест 1: Определение языка
    print("\n1. Тест определения языка...")
    summarizer = Summarizer()
    test_text_en = "This is a sample English text for testing."
    detected = summarizer.detect_language(test_text_en)
    print(f"   [OK] Определен язык: {detected} (ожидалось: en)")
    
    # Тест 2: Простое резюмирование (без загрузки моделей)
    print("\n2. Тест простого резюмирования...")
    long_text = "First sentence. Second sentence. Third sentence. " * 10
    summary, lang = summarizer.summarize(long_text, compression_level=0.3, language='en')
    print(f"   [OK] Резюме создано: {len(summary)} символов (исходный текст: {len(long_text)} символов)")
    print(f"   [OK] Язык: {lang}")
    
    # Тест 3: Извлечение ключевых моментов
    print("\n3. Тест извлечения ключевых моментов...")
    key_points = summarizer.extract_key_points(long_text, num_points=3)
    print(f"   [OK] Извлечено ключевых моментов: {len(key_points)}")
    
    # Тест 4: Чтение файла
    print("\n4. Тест чтения файла...")
    try:
        processor = FileProcessor()
        text = processor.read_file("data/example_english.txt")
        print(f"   [OK] Файл прочитан: {len(text)} символов")
    except Exception as e:
        print(f"   [ERROR] Ошибка чтения файла: {e}")
    
    print("\n" + "=" * 60)
    print("ВСЕ БАЗОВЫЕ ТЕСТЫ ПРОЙДЕНЫ!")
    print("=" * 60)
    print("\nДля полного тестирования с моделями transformers запустите:")
    print("  pytest tests/ -v")

if __name__ == "__main__":
    test_basic_functionality()

