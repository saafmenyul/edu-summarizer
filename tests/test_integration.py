"""
Integration tests for the complete summarization workflow.
"""

import pytest
import tempfile
import os
from src.summarizer import Summarizer
from src.file_processor import FileProcessor


class TestIntegration:
    """Integration tests for the full workflow."""
    
    def test_full_workflow_english(self):
        """Test complete workflow with English text."""
        # Create a temporary text file
        text_content = """
        Artificial intelligence has become one of the most transformative technologies
        of our time. It encompasses machine learning, deep learning, natural language
        processing, and computer vision. These technologies are being applied across
        various industries including healthcare, finance, transportation, and education.
        The potential benefits are enormous, but we must also consider ethical implications
        and ensure responsible development and deployment of AI systems.
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(text_content)
            temp_path = f.name
        
        try:
            # Read file
            processor = FileProcessor()
            text = processor.read_file(temp_path)
            assert len(text) > 0
            
            # Summarize
            summarizer = Summarizer(language='en')
            summary, lang = summarizer.summarize(text, compression_level=0.3, language='en')
            
            assert lang == 'en'
            assert len(summary) > 0
            assert len(summary) < len(text)
            
            # Extract key points
            key_points = summarizer.extract_key_points(text, num_points=3)
            assert len(key_points) > 0
            
        finally:
            os.unlink(temp_path)
    
    def test_multilingual_workflow(self):
        """Test workflow with multiple languages."""
        languages = {
            'en': "Machine learning is a powerful technology.",
            'ru': "Машинное обучение - это мощная технология.",
            'de': "Maschinelles Lernen ist eine leistungsstarke Technologie."
        }
        
        for lang, text in languages.items():
            summarizer = Summarizer(language=lang)
            summary, detected_lang = summarizer.summarize(text, compression_level=0.5, language=lang)
            assert detected_lang == lang
            assert len(summary) > 0

