"""
Command-line interface for the summarization tool.
"""

import click
from pathlib import Path
from .summarizer import Summarizer
from .file_processor import FileProcessor


@click.command()
@click.option(
    '--input', '-i',
    type=click.Path(exists=True),
    required=True,
    help='Path to input file (txt, docx, or pdf)'
)
@click.option(
    '--output', '-o',
    type=click.Path(),
    help='Path to output file (optional, prints to stdout if not specified)'
)
@click.option(
    '--language', '-l',
    type=click.Choice(['en', 'ru', 'de', 'auto'], case_sensitive=False),
    default='auto',
    help='Language of the text (en, ru, de, or auto for auto-detection)'
)
@click.option(
    '--compression', '-c',
    type=click.Choice(['20', '30', '50'], case_sensitive=False),
    default='30',
    help='Compression level (20%%, 30%%, or 50%%)'
)
@click.option(
    '--key-points', '-k',
    is_flag=True,
    help='Also extract and display key points'
)
def main(input, output, language, compression, key_points):
    """
    Educational Material Summarization Tool
    
    Automatically summarize educational materials with support for multiple languages.
    """
    try:
        # Read input file
        click.echo(f"Reading file: {input}")
        file_processor = FileProcessor()
        text = file_processor.read_file(input)
        
        if not text.strip():
            click.echo("Error: Input file is empty", err=True)
            return
        
        click.echo(f"Input text length: {len(text)} characters")
        
        # Initialize summarizer
        summarizer = Summarizer(language=language.lower())
        
        # Convert compression level
        compression_ratio = float(compression) / 100.0
        
        # Summarize
        click.echo(f"Summarizing with {compression}% compression...")
        summary, detected_lang = summarizer.summarize(text, compression_ratio, language.lower() if language != 'auto' else None)
        
        click.echo(f"Detected language: {detected_lang}")
        click.echo(f"Summary length: {len(summary)} characters")
        
        # Extract key points if requested
        result = f"SUMMARY:\n{'='*50}\n{summary}\n\n"
        
        if key_points:
            points = summarizer.extract_key_points(text, num_points=5)
            result += f"KEY POINTS:\n{'='*50}\n"
            for i, point in enumerate(points, 1):
                result += f"{i}. {point}\n"
            result += "\n"
        
        # Output result
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
            click.echo(f"Summary saved to: {output}")
        else:
            click.echo("\n" + result)
            
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()


if __name__ == '__main__':
    main()

