"""
Core summarization module with support for multiple languages and compression levels.
"""

import re
from typing import List, Tuple
from langdetect import detect, LangDetectException
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class Summarizer:
    """Main summarization class supporting multiple languages and compression levels."""
    
    # Model mapping for different languages
    MODELS = {
        'en': 'facebook/bart-large-cnn',
        'ru': 'IlyaGusev/rut5_base_sum_gazeta',
        'de': 'facebook/mbart-large-50-many-to-many-mmt'
    }
    
    def __init__(self, language: str = 'auto'):
        """
        Initialize the summarizer.
        
        Args:
            language: Target language ('en', 'ru', 'de', or 'auto' for auto-detection)
        """
        self.language = language
        self.model = None
        self.tokenizer = None
        self.summarizer_pipeline = None
        self._device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    def detect_language(self, text: str) -> str:
        """
        Detect the language of the input text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Detected language code ('en', 'ru', 'de')
        """
        try:
            detected = detect(text)
            # Map langdetect codes to our supported languages
            lang_map = {
                'en': 'en',
                'ru': 'ru',
                'de': 'de'
            }
            return lang_map.get(detected, 'en')  # Default to English
        except LangDetectException:
            return 'en'  # Default to English if detection fails
    
    def _load_model(self, language: str):
        """Load the appropriate model for the specified language."""
        model_name = self.MODELS.get(language, self.MODELS['en'])
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            self.summarizer_pipeline = pipeline(
                "summarization",
                model=self.model,
                tokenizer=self.tokenizer,
                device=0 if self._device == 'cuda' else -1
            )
        except Exception as e:
            # Fallback to simple extraction-based method
            print(f"Warning: Could not load model {model_name}. Using simple method. Error: {e}")
            self.summarizer_pipeline = None
    
    def _simple_summarize(self, text: str, compression_ratio: float) -> str:
        """
        Simple extraction-based summarization method as fallback.
        
        Args:
            text: Input text
            compression_ratio: Target compression ratio (0.2, 0.3, 0.5)
            
        Returns:
            Summarized text
        """
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return text
        
        # Calculate number of sentences to keep
        num_sentences = max(1, int(len(sentences) * compression_ratio))
        
        # Simple approach: take first N sentences
        # In a more sophisticated version, we could score sentences
        selected_sentences = sentences[:num_sentences]
        
        return '. '.join(selected_sentences) + '.'
    
    def summarize(
        self,
        text: str,
        compression_level: float = 0.3,
        language: str = None
    ) -> Tuple[str, str]:
        """
        Summarize the input text.
        
        Args:
            text: Input text to summarize
            compression_level: Compression level (0.2, 0.3, or 0.5)
            language: Language code ('en', 'ru', 'de') or None for auto-detection
            
        Returns:
            Tuple of (summarized_text, detected_language)
        """
        if not text or not text.strip():
            return "", "unknown"
        
        # Detect or use specified language
        if language is None:
            if self.language == 'auto':
                detected_lang = self.detect_language(text)
            else:
                detected_lang = self.language
        else:
            detected_lang = language
        
        # Load model if not already loaded or language changed
        if self.summarizer_pipeline is None or detected_lang != getattr(self, '_current_lang', None):
            self._load_model(detected_lang)
            self._current_lang = detected_lang
        
        # Calculate max and min length based on compression level
        text_length = len(text.split())
        max_length = int(text_length * compression_level)
        min_length = max(1, int(max_length * 0.5))
        
        # Use transformer model if available
        if self.summarizer_pipeline is not None:
            try:
                # For some models, we need to handle differently
                if detected_lang == 'de':
                    # mBART requires special handling
                    result = self.summarizer_pipeline(
                        text,
                        max_length=max_length,
                        min_length=min_length,
                        do_sample=False
                    )
                else:
                    result = self.summarizer_pipeline(
                        text,
                        max_length=max_length,
                        min_length=min_length,
                        do_sample=False
                    )
                
                if isinstance(result, list) and len(result) > 0:
                    summary = result[0].get('summary_text', '')
                    if summary:
                        return summary, detected_lang
            except Exception as e:
                print(f"Error in transformer summarization: {e}. Falling back to simple method.")
        
        # Fallback to simple method
        summary = self._simple_summarize(text, compression_level)
        return summary, detected_lang
    
    def extract_key_points(self, text: str, num_points: int = 5) -> List[str]:
        """
        Extract key points from the text.
        
        Args:
            text: Input text
            num_points: Number of key points to extract
            
        Returns:
            List of key point sentences
        """
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return []
        
        # Simple heuristic: longer sentences often contain more information
        # In a more sophisticated version, we could use TF-IDF or other methods
        scored_sentences = [(len(s.split()), s) for s in sentences]
        scored_sentences.sort(reverse=True)
        
        key_points = [s for _, s in scored_sentences[:num_points]]
        return key_points

