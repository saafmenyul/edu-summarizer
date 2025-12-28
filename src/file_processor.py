"""
File processing module for handling different file formats.
"""

import os
from typing import Optional
from pathlib import Path


class FileProcessor:
    """Handle file reading for different formats."""
    
    @staticmethod
    def read_text_file(file_path: str) -> str:
        """
        Read a plain text file.
        
        Args:
            file_path: Path to the text file
            
        Returns:
            File contents as string
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Try with different encoding
            with open(file_path, 'r', encoding='latin-1') as f:
                return f.read()
    
    @staticmethod
    def read_docx(file_path: str) -> str:
        """
        Read a DOCX file.
        
        Args:
            file_path: Path to the DOCX file
            
        Returns:
            Extracted text content
        """
        try:
            from docx import Document
            doc = Document(file_path)
            paragraphs = [p.text for p in doc.paragraphs]
            return '\n'.join(paragraphs)
        except ImportError:
            raise ImportError("python-docx is required for DOCX support. Install it with: pip install python-docx")
    
    @staticmethod
    def read_pdf(file_path: str) -> str:
        """
        Read a PDF file.
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            Extracted text content
        """
        try:
            import PyPDF2
            text = ""
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return text
        except ImportError:
            raise ImportError("PyPDF2 is required for PDF support. Install it with: pip install PyPDF2")
    
    @staticmethod
    def read_file(file_path: str) -> str:
        """
        Automatically detect file type and read it.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Extracted text content
            
        Raises:
            ValueError: If file type is not supported
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        extension = file_path.suffix.lower()
        
        if extension == '.txt':
            return FileProcessor.read_text_file(str(file_path))
        elif extension == '.docx':
            return FileProcessor.read_docx(str(file_path))
        elif extension == '.pdf':
            return FileProcessor.read_pdf(str(file_path))
        else:
            # Try as text file
            try:
                return FileProcessor.read_text_file(str(file_path))
            except Exception:
                raise ValueError(f"Unsupported file type: {extension}")

