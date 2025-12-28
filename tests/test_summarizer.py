"""
Tests for the Summarizer class.
"""

import pytest
from src.summarizer import Summarizer


class TestSummarizer:
    """Test cases for Summarizer."""
    
    def test_detect_language_english(self):
        """Test language detection for English text."""
        summarizer = Summarizer()
        text = "This is a sample English text for testing language detection."
        detected = summarizer.detect_language(text)
        assert detected == 'en'
    
    def test_detect_language_russian(self):
        """Test language detection for Russian text."""
        summarizer = Summarizer()
        text = "Это пример русского текста для тестирования определения языка."
        detected = summarizer.detect_language(text)
        assert detected == 'ru'
    
    def test_detect_language_german(self):
        """Test language detection for German text."""
        summarizer = Summarizer()
        text = "Dies ist ein Beispieltext auf Deutsch zum Testen der Spracherkennung."
        detected = summarizer.detect_language(text)
        assert detected == 'de'
    
    def test_summarize_english(self):
        """Test summarization of English text."""
        summarizer = Summarizer(language='en')
        text = """
        Machine learning is a subset of artificial intelligence that focuses on the development
        of algorithms and statistical models that enable computer systems to improve their
        performance on a specific task through experience. Unlike traditional programming,
        where explicit instructions are provided, machine learning systems learn patterns
        from data. There are three main types of machine learning: supervised learning,
        unsupervised learning, and reinforcement learning. Supervised learning uses labeled
        data to train models, unsupervised learning finds patterns in unlabeled data, and
        reinforcement learning uses rewards and penalties to guide learning.
        """
        summary, lang = summarizer.summarize(text, compression_level=0.3, language='en')
        assert lang == 'en'
        assert len(summary) > 0
        assert len(summary) < len(text)
    
    def test_summarize_russian(self):
        """Test summarization of Russian text."""
        summarizer = Summarizer(language='ru')
        text = """
        Машинное обучение - это подмножество искусственного интеллекта, которое фокусируется
        на разработке алгоритмов и статистических моделей, позволяющих компьютерным системам
        улучшать свою производительность в конкретной задаче через опыт. В отличие от
        традиционного программирования, где предоставляются явные инструкции, системы
        машинного обучения изучают закономерности из данных. Существуют три основных типа
        машинного обучения: обучение с учителем, обучение без учителя и обучение с подкреплением.
        """
        summary, lang = summarizer.summarize(text, compression_level=0.3, language='ru')
        assert lang == 'ru'
        assert len(summary) > 0
        assert len(summary) < len(text)
    
    def test_summarize_german(self):
        """Test summarization of German text."""
        summarizer = Summarizer(language='de')
        text = """
        Maschinelles Lernen ist eine Teilmenge der künstlichen Intelligenz, die sich auf die
        Entwicklung von Algorithmen und statistischen Modellen konzentriert, die es Computersystemen
        ermöglichen, ihre Leistung bei einer bestimmten Aufgabe durch Erfahrung zu verbessern.
        Im Gegensatz zum traditionellen Programmieren, bei dem explizite Anweisungen bereitgestellt
        werden, lernen Systeme des maschinellen Lernens Muster aus Daten.
        """
        summary, lang = summarizer.summarize(text, compression_level=0.3, language='de')
        assert lang == 'de'
        assert len(summary) > 0
    
    def test_compression_levels(self):
        """Test different compression levels."""
        summarizer = Summarizer(language='en')
        text = "This is a test sentence. " * 20
        
        summary_20, _ = summarizer.summarize(text, compression_level=0.2)
        summary_30, _ = summarizer.summarize(text, compression_level=0.3)
        summary_50, _ = summarizer.summarize(text, compression_level=0.5)
        
        # 50% should generally be longer than 20%
        assert len(summary_50) >= len(summary_20)
    
    def test_extract_key_points(self):
        """Test key points extraction."""
        summarizer = Summarizer()
        text = """
        First important point about machine learning. Second significant concept in AI.
        Third crucial aspect of neural networks. Fourth key idea about deep learning.
        Fifth essential topic in data science. Sixth relevant point about algorithms.
        """
        points = summarizer.extract_key_points(text, num_points=3)
        assert len(points) == 3
        assert all(isinstance(point, str) for point in points)
    
    def test_empty_text(self):
        """Test handling of empty text."""
        summarizer = Summarizer()
        summary, lang = summarizer.summarize("", compression_level=0.3)
        assert summary == ""
    
    def test_auto_language_detection(self):
        """Test automatic language detection."""
        summarizer = Summarizer(language='auto')
        text = "This is an English text for automatic language detection."
        summary, lang = summarizer.summarize(text, compression_level=0.3)
        assert lang in ['en', 'ru', 'de']  # Should detect a language

