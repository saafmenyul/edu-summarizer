"""
Tests for the FileProcessor class.
"""

import pytest
import tempfile
import os
from pathlib import Path
from src.file_processor import FileProcessor


class TestFileProcessor:
    """Test cases for FileProcessor."""
    
    def test_read_text_file(self):
        """Test reading a plain text file."""
        processor = FileProcessor()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write("This is a test text file.\nWith multiple lines.")
            temp_path = f.name
        
        try:
            content = processor.read_text_file(temp_path)
            assert "This is a test text file" in content
            assert "With multiple lines" in content
        finally:
            os.unlink(temp_path)
    
    def test_read_file_text(self):
        """Test automatic file reading for text files."""
        processor = FileProcessor()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write("Test content for automatic reading.")
            temp_path = f.name
        
        try:
            content = processor.read_file(temp_path)
            assert "Test content" in content
        finally:
            os.unlink(temp_path)
    
    def test_file_not_found(self):
        """Test handling of non-existent files."""
        processor = FileProcessor()
        with pytest.raises(FileNotFoundError):
            processor.read_file("nonexistent_file.txt")
    
    def test_unsupported_file_type(self):
        """Test handling of unsupported file types."""
        processor = FileProcessor()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xyz', delete=False) as f:
            f.write("test")
            temp_path = f.name
        
        try:
            # Should try to read as text or raise ValueError
            try:
                content = processor.read_file(temp_path)
                # If it succeeds, that's also fine (treated as text)
                assert isinstance(content, str)
            except ValueError:
                # Expected for truly unsupported types
                pass
        finally:
            os.unlink(temp_path)

