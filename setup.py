"""
Setup configuration for the Educational Material Summarization Tool.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="edu-summarizer",
    version="1.0.0",
    author="Educational Material Summarization Tool",
    description="Инструмент для автоматического резюмирования учебных материалов с поддержкой нескольких языков",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/edu-summarizer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "transformers>=4.35.2",
        "torch>=2.1.1",
        "sentencepiece>=0.1.99",
        "protobuf>=4.25.1",
        "nltk>=3.8.1",
        "spacy>=3.7.2",
        "langdetect>=1.0.9",
        "numpy>=1.24.3",
        "pandas>=2.1.3",
        "click>=8.1.7",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.12.0",
            "black>=23.11.0",
            "flake8>=6.1.0",
            "mypy>=1.7.1",
        ],
        "docx": [
            "python-docx>=1.1.0",
        ],
        "pdf": [
            "PyPDF2>=3.0.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "edu-summarize=src.cli:main",
        ],
    },
)

